from abc import abstractmethod
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.UnaryOperator import UnaryOperator
from opendlp.regex_generate.AbstractNode.Quantifier import Quantifiers

class MatchOneOrMore (Quantifiers):
    def buildcopy(self):
        return self
        


    def form(self, string, flavour, context):
        tmp = []
        child = Node
        child = self.get_children(0)
        index = context.incGroup()
        child.form(self, tmp, flavour, context)
        l = child.is_escaped() ? tmp.length()-1 : tmp.length()
        group = l > 1 and ~(child.is_character_class()) and  ~(isinstance(child, Group)) and ~(isinstance(child,NonCapturingGroup))

        if(group):
            string.append("(?:")
            string.append(tmp)
            string.append(")")
        else:
            string.append(tmp)
        string.append("++")

