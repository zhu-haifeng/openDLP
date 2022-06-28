from abc import abstractmethod
from pickle import FALSE

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.regex_tree.AbstractNode.TernaryOperator import TernaryOperator


class MatchMinMax (TernaryOperator):

    Max_N_generation = 20

    def __init__(self):
        ""
        ""
    
    def buildcopy(self):
        return self

    def form(self, string, flavour, context):
        tmp = []
        child = Node
        child = self.get_first()
        index = context.incGroups();
        child.form(self, tmp, flavour, context)
        l = child.is_escaped() ? tmp.length()-1 : tmp.length()
        group = l > 1 and ~(child.is_character_class()) and ~(isinstance(child, Group)) and ~(isinstance(child,NonCapturingGroup))

        if (group):
            string.append("(?:")
            string.append(tmp)
            string.append(")")
        else:
            string.append(tmp)

        string.append("{")
        string.append(int(str(self.get_second())))
        string.append(",")
        string.append(int(str(self.get_third())))
        string.append("}+")

    def is_valid(self):
        first = self.get_first()
        validFirst = first.is_valid() and ~(isinstance(first, Concatenator) or isinstance(first,Quantifier) or isinstance(first,MatchMinMax) or isinstance(first,MatchMinMaxGreedy) or isinstance(first, Anchor) or isinstance(first, Lookaround))

        second  = self.get_second()
        third = self.get_third()

        if(isinstance(third,Constant) and isinstance(second,Constant)) :
            try :
                leftValue = int(str(self.get_second))
                rightValue = int(str(self.get_third))
            except NumberFormatException as ex :
                return FALSE
            if (leftValue < 0 and rightValue > 0):
                return False
            if(leftValue >= rightValue):
                return False

            return validFirst
        return False

    
        
        
        