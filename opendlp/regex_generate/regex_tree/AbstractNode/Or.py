from abc import abstractmethod

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.regex_tree.AbstractNode.BinaryOperator import BinaryOperator

class Or(BinaryOperator):
    def buildCopy(self):
        return self

    def form(self, string, flavour, context):
        if (isinstance(self.get_parent(), Quantifier)):
            self.append("(?:")

        self.getLeft().form(self, string, flavour, context)
        self.append("|")
        self.getRight().form(self, string, flavour, context)
        if (isinstance(self.get_parent(),Quantifier)):
            self.append(")")
    
    def is_vaild(self):
        if(isinstance(self.getLeft(), Quantifier) or isinstance(self.getRight(),Quantifier)):
            return False
        
        return self.getLeft().is_valid() and self.getRight().is_valid()
        

        
        
        