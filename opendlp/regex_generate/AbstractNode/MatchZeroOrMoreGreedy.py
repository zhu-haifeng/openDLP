from abc import abstractmethod
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.UnaryOperator import UnaryOperator
from opendlp.regex_generate.AbstractNode.Quantifier import Quantifiers

class MatchZeroOrMoreGreedy (Quantifiers):
    def buildcopy(self):
        return self

    def form(self, string, flavour, context):
        self.get_children(0).form(self, string, flavour, context)
        string.append("*")