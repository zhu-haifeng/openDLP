from abc import abstractmethod
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit
from pyrsistent import v

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.UnaryOperator import UnaryOperator
from opendlp.regex_generate.AbstractNode.Lookaround import Lookaround


class NegativeLookbehind (Lookaround) :
    def buildcopy(self):
        return self

    def is_valid():
        valid = super.is_valid()
        if(valid == 0):
            return valid

        return is_look_behind_valid()

    def form(self, string, flavour, context):
        self.append("(?<!")
        self.get_children(0).form(self, string, flavour, context)
        self.append(")")
            
        

        
        