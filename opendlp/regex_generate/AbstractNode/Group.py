from abc import abstractmethod
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.UnaryOperator import UnaryOperator


class Group (UnaryOperator) :
    def buildcopy(self):
        return self

    def form(self, string, flavour, context):
        self.append("(")
        context.incGroup();
        self.get_children(0).form(self, string, flavour, context)
        self.append(")")

    def is_valid(self):
        return self.get_children(0).is_valid()
        
        
        
        
