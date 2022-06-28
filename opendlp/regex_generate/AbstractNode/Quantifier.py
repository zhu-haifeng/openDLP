from abc import abstractmethod
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.UnaryOperator import UnaryOperator


class Quantifiers(UnaryOperator):
    def is_Valid(self):
        child = Node
        child = self.get_children(0)
        return child.is_valid() and ~(isinstance(child,Quantifier) or isinstance(child,MatchMinMax) or isinstance(child,MatchMinMaxGreedy) or isinstance(child,Anchor) or isinstance(child,Lookaround))
        