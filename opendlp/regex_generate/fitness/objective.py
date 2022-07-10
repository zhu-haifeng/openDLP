import re
import numpy as np
from opendlp.regex_generate.config.conf import RegexFlavour
from opendlp.regex_generate.regex_tree.regex_context import RegexContext
import logging
from opendlp.regex_generate.regex_tree.node import Node
LOGGER = logging.getLogger('openDLP')

class Objective:
    def __init__(self, dataset):
        self.__dataset = dataset

    def cal_fitness(self, tree:Node):
        """
        calculate fitness of a regex tree
        @param tree: a regex tree
        @return: fitness array with three value:[Ps, Pc, Lscore]
        """
        r = tree.form("", flavour=RegexFlavour.Python, context=RegexContext())
        # r = "13[3456789]\d{8}"
        LOGGER.info("===============")
        LOGGER.info(f"[regex:]")
        LOGGER.info(r)
        LOGGER.info("===============")
        # r = re.escape(r)
        pat = re.compile(r)
        len_P = len(self.__dataset.pos_examples)
        len_N = len(self.__dataset.neg_examples)

        SMALL = 1e-5/(len_P+len_N)

        match_P = np.zeros(len_P).astype('bool')
        match_N = np.zeros(len_P).astype('bool')
        count_P = np.zeros(len_N).astype('int')
        count_N = np.zeros(len_N).astype('int')
        total_len = 0


        for i in range(len_P):
            example=self.__dataset.pos_examples[i]
            total_len += len(example)
            sre = pat.search(example)
            if sre:
                start,end = sre.span()
                count_P[i] = end-start
                if start == 0 and end == len(example):
                    match_P[i] = True
        
        for i in range(len_N):
            example = self.__dataset.neg_examples[i]
            sre = pat.search(example)
            if sre:
                start,end = sre.span()
                count_N[i] = end-start
                if start == 0 and end == len(example):
                    match_N[i] = True
        # LOGGER.info(match_P)
        # LOGGER.info(match_N)
        # LOGGER.info(np.sum(match_P))
        # LOGGER.info(np.sum(match_N))
        # LOGGER.info(count_P)
        # LOGGER.info(count_N)
        # LOGGER.info(np.sum(count_P))
        # LOGGER.info(np.sum(count_N))
        P_s = (np.sum(match_P))/(np.sum(match_P)+SMALL+np.sum(match_N))
        P_c = (np.sum(match_P*count_P)) / (np.sum(match_N*count_N)+np.sum(match_P*count_P)+SMALL) + \
            (np.sum((1-match_P)*count_P)) / \
            (np.sum((1-match_P)*count_P)+SMALL+np.sum((1-match_N)*count_N))

        L_score = np.exp(-np.abs(len(r)-total_len/len_P))

        # LOGGER.info("P_s = %d/%d", np.sum(match_P),
        #             np.sum(match_P)+np.sum(match_N))
        # LOGGER.info("P_c = %d / %d + %d / %d",
        #             np.sum(match_P*count_P),
        #             np.sum(match_N*count_N)+np.sum(match_P * count_P),
        #             np.sum((1-match_P)*count_P), np.sum((1-match_P)*count_P)+np.sum((1-match_N)*count_N))
        # LOGGER.info("L_score = np.exp(-np.abs(%d-%d/%d))",
        #             len(r), total_len, len_P)
        LOGGER.info([P_s, P_c, L_score])
        return [P_s, P_c, L_score]
