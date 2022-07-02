from abc import abstractmethod

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode

class UnaryOperator (AbstractNode):
    def __init__(self):
        parent = Node

    def get_min_child_count():
        return 1

    def get_max_child_count():
        return 1
        
    @abstractmethod
    def buildcopy():
        ""
        ""

    def clone_tree(self):
        clone = buildcopy()
        if(self.get_children().isEmpty() == 0):
            child = self.get_children(0).clone_tree()
            child.set_parent(clone)
            # clone.get_children().add(child)
            tmp = child.get_children()
            tmp += child

        return clone

    def get_parent(self):
        return self.parent

    def set_parent(self,parent):
        self.parent = parent

    
        
        
        
        
        