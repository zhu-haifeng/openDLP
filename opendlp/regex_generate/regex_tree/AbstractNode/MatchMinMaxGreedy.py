from abc import abstractmethod
from pickle import FALSE

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.TernaryOperator import TernaryOperator

class MatchMinMaxGreedy (TernaryOperator):
    MAX_N_GENERATION = 20

    def buildcopy(self):
        return self
    
    def form(self, string, flavour, context):
        self.get_first().form(self, string, flavour, context)
        string.append("{")
        string.append(int(str(self.get_second())))
        string.append(",")
        string.append(int(str(self.get_third())))
        string.append("}")

    def is_valid(self):
        first = self.get_first()
        "检查是否之前的是否输错"
        validFirst = first.is_valid() and ~(isinstance(first,Concatenator) or isinstance(first,Quantifier) or isinstance(first,MatchMinMax) or isinstance(first,MatchMinMaxGreedy) or isinstance(first,Lookaround))
        second = self.get_second()
        third = self.get_third()

        if(isinstance(third,Constant) and isinstance(second,Constant)):
            try :
                leftValue = int(str(second))
                rightValue = int(str(third))
            except NumberFormatException  as ex:
                return False

            if(leftValue < 0 or rightValue < 0):
                return False

            if(leftValue >=rightValue):
                return False
            return validFirst

        return False



        
        
        