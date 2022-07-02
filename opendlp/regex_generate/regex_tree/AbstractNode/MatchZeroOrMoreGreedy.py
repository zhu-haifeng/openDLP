from abc import abstractmethod
from logging import root

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers

class MatchZeroOrMoreGreedy (Quantifiers):
    def buildcopy(self):
        return self

    def form(self, string, flavour, context):
        self.get_children(0).form(self, string, flavour, context)
        string +=("*")
        return string