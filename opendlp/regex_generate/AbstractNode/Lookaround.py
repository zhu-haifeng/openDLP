from abc import abstractmethod
from logging import root
import re

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode
from opendlp.regex_generate.AbstractNode.UnaryOperator import UnaryOperator

class Lookaround(UnaryOperator):
    def __init__(self):
     ""
     ""


    def is_valid(self):
        child = Node
        child = self.get_children(0)
        return child.is_valid() and (isinstance(child,RegexRange) or isinstance(child,Anchor) or isinstance(Backreference))
    
    
    def checkQuantifiers(root):
        numberQuantifier = 0
        hasOnlyMinMax = True
        if(isinstance(root,Quantifier)):
            hasOnlyMinMax = False
            numberQuantifier += 1
        if(isinstance(root,MatchMinMax) or isinstance(root,MatchMinMaxGreedy)) :
            numberQuantifier += 1

        child = Node
        for child in range(root.get_children()):
            checkQuantifiers(child)

    def is_look_behind_vaild(self):
        checkQuantifiers(self)
        return hasOnlyMinMax or (numberQuantifiers < 1)
        
            

        
        

