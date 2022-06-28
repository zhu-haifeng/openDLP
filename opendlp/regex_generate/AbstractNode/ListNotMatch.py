from abc import abstractmethod
from doctest import FAIL_FAST
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit
from regex import F

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.UnaryOperator import UnaryOperator



class ListNotMatch (UnaryOperator) :
    def buildcopy(self):
        return self

    def form(self, string, flavour, context):
        child = Node
        child = self.get_children(0)
        string.append("[^")
        child.form(self, string, flavour, context)
        string.append("]")

    def is_valid(self):
        return check_valid(self.get_children(0))

    def check_valid(root,self):
        if(~(isinstance(root,Constant) or isinstance(root,RegexRange) or isinstance(root,Concatenator))):
            return False

        for child in range(root.get_children()):
            if(~(check_valid(child))):
                return False

        return True

    def is_Character_class():
        return True
        
        
        
        
        