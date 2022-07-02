from abc import abstractmethod

from opendlp.regex_generate.config.conf import RegexFlavour
from opendlp.regex_generate.regex_tree.id_factory import IDFactory
from opendlp.regex_generate.regex_tree.regex_context import RegexContext


class Node:
    def __init__(self):
        self.id = IDFactory.next_id()
        # self.children = []

    def get_id(self):
        return self.id

    def get_children(self):
        return self.children

    def is_character_class(self):
        return False

    def is_escaped(self):
        return False


    @abstractmethod
    def get_min_children_count(self) -> int:
        """
        @return: min children count of node
        """

    @abstractmethod
    def get_max_children_count(self) -> int:
        """
        @return: max children count of node
        """

    @abstractmethod
    def get_parent(self):
        """
        @return: parent node of current node
        """

    @abstractmethod
    def set_parent(self, parent):
        """
        set parent of current node
        @return:
        """

    @abstractmethod
    def is_valid(self):
        """
        check whether the tree with current node as root is a valid regex pattern
        @return: bool
        """

    @abstractmethod
    def form(self, string : str, flavour=RegexFlavour.Python, context=RegexContext()):
        """
        form regex string
        @param string: regex string before current node
        @param flavour: regex grammar related with language
        @param context:
        @return:
        """

    @abstractmethod
    def clone_tree(self):
        """
        clone current node and it's children
        @return:
        """
