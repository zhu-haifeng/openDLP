from heapq import merge
from typing import List, Set, Dict
import re
import logging

from opendlp.regex_generate.config.conf import BPE_SPLIT_CHAR

LOGGER = logging.getLogger('openDLP')

def split(s_in: str) -> str:
    s_out = ""
    for c in s_in:
        s_out += c+BPE_SPLIT_CHAR
    return s_out[:-1]


def build_vocab(strings: List[str]) -> Dict[str, int]:
    vocab = {}
    for string in strings:
        split_str = split(string)
        if(split_str in vocab):
            vocab[split_str] += 1
        else:
            vocab[split_str] = 1
    return vocab


def pair_freq_stats(vocab: Dict[str, int]) -> Dict[str, int]:
    pair2freq = {}
    for word, freq in vocab.items():
        symbols = word.split(BPE_SPLIT_CHAR)
        for i in range(len(symbols)-1):
            pair = (symbols[i], symbols[i+1])
            if pair in pair2freq:
                pair2freq[symbols[i], symbols[i+1]] += freq
            else:
                pair2freq[symbols[i], symbols[i+1]] = freq
    return pair2freq


def merge(best, vocab_in: Dict[str, int]) -> Dict[str, int]:
    vocab_out = {}
    bigram = re.escape(BPE_SPLIT_CHAR.join(best))
    patten = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in vocab_in:
        word_out = patten.sub(''.join(best),word)
        vocab_out[word_out] = vocab_in[word]
    return vocab_out


def learn_bpe(strings: List[str], percent_threshold: float) -> Set[str]:
    """
    learn byte pair encode tokens from positive examples
    @param strings: raw string list used to learn bpe
    @param percent: proportion threshold
    @return: learned byte pair encode tokens
    """
    vocab = build_vocab(strings)
    s = set()
    percent = 1.0
    while percent > percent_threshold:
        pair2freq = pair_freq_stats(vocab)
        best = max(pair2freq, key=pair2freq.get)
        percent = pair2freq.get(best)/len(strings)
        if(percent >= percent_threshold):
            vocab = merge(best, vocab)
            s.add("".join(best))
        # print(best, percent)
    # for string in vocab:
    #     print("string")
    #     print(string)

    #     tokens = string.split(BPE_SPLIT_CHAR)
    #     print("tokens")
    #     print(tokens)
    #     for token in tokens:
            # s.add(token)
    LOGGER.info("bpe set:")
    LOGGER.info(s)
    print(s)
    return s

