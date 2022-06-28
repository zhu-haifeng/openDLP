# TODD:
# from regex_tree.abstract_node import *

class NodeFactory:
    def __init__(self):
        self.terminal_set = []
        self.function_set = []

    def build_terminal_set(self, bpe_tokens):
        """
        load default terminal set
        @return:
        """
        self.terminal_set = list(bpe_tokens)

    def build_function_set(self):
        """
        load default terminal set
        @return:
        """
        raise NotImplementedError
        # TODO:
        self.function_set = []


    def build(self, bpe_tokens=None):
        self.build_terminal_set(bpe_tokens)
        self.build_function_set()