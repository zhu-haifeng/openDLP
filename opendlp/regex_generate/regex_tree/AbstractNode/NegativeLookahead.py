from abc import abstractmethod
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator
from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class NegativeLookahead (Lookaround) :
    def buildcopy(self):
        return self

    def form(self, string, flavour, context):
        self.append("(?!")
        self.get_children(0).form(self, string, flavour, context)
        self.append(")")
        
        