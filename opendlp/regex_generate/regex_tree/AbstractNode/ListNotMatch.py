from abc import abstractmethod
from doctest import FAIL_FAST
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit
from regex import F

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator
from opendlp.regex_generate.regex_tree.leaf.constant import Constant
from opendlp.regex_generate.regex_tree.leaf.regex_range import RegexRange
from opendlp.regex_generate.regex_tree.AbstractNode.Concatenator import Concatenator




class ListNotMatch (UnaryOperator) :
    def buildcopy(self):
        return ListNotMatch()

    def form(self, string, flavour, context):
        child = Node
        child = self.get_children()[0]
        # string.append("[^")
        string += ("[^")
        child.form(self, string, flavour, context)
        string += ("]")
        return string

    def is_valid(self):
        return self.check_valid(self.get_children()[0])

    def check_valid(root,self):
        if(not(isinstance(root,Constant) or isinstance(root,RegexRange) or isinstance(root,Concatenator))):
            return False

        for child in range(root.get_children()):
            if(not(self.check_valid(child))):
                return False

        return True

    def is_Character_class(self):
        return True
        
        
        
        
        