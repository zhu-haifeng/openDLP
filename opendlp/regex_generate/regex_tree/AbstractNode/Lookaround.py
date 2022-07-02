from abc import abstractmethod
import imp
from logging import root

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator
from opendlp.regex_generate.regex_tree.leaf.regex_range import RegexRange
from opendlp.regex_generate.regex_tree.leaf.anchor import Anchor
from opendlp.regex_generate.regex_tree.leaf.back_reference import BackReference
from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifier
from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMax import MatchMinMax
from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMaxGreedy import MatchMinMaxGreedy

class Lookaround(UnaryOperator):
    
    numberQuantifiers =0
    hasOnlyMinMax = True


    def __init__(self):
        ""
        ""



    def is_valid(self):
        child = Node
        child = self.get_children(0)
        return child.is_valid() and (isinstance(child,RegexRange) or isinstance(child,Anchor) or isinstance(BackReference))
    
    
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
        
            

        
        

