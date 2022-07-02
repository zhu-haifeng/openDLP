from abc import abstractmethod
from logging import root
import re


# from opendlp.regex_generate.regex_tree.node import Node
# from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator


class Group (UnaryOperator) :
    def buildcopy(self):
        return Group()

    def form(self, string, flavour, context):
        # self.append("(")
        string += ("(")
        context.incGroup();
        self.get_children()[0].form(self, string, flavour, context)
        # self.append(")")
        string += (")")
        return string

    def is_valid(self):
        return self.get_children()[0].is_valid()
        
        
        
        
