from abc import abstractmethod

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.AbstractNode.AbstractNode import AbstractNode

class TernaryOperator(AbstractNode):
    def __init__(self):
       self.parent = []
    
    def buildcopy() ->TernaryOperator:
        ""
        ""
    def clone_tree() ->Node :
        top = buildcopy();
        topchild = []
        topchild = top.get_children()
        child = Node
        for child in range(this.get_children()):
                Newchild = child.clone_tree()
                Newchild.set_parent(top)
                topchild.add(Newchild)
        return top

    def get_parent(self):
        return self.parent

    def set_parent(self,parent):
        self.parent = parent

    def get_min_child_count():
        return 3

    def get_max_child_count():
        return 3

    def get_first(self) -> Node:
        return self.get_children(0)

    def get_second(self) -> Node:
        return self.get_children(1)

    def get_third(self) ->Node:
        return self.get_children(2)
        
        
        
        
        
        

        
        

        