from abc import abstractmethod
from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode

class TernaryOperator(AbstractNode):
    parent = Node

    def __init__(self):
        super().__init__()
        

    @abstractmethod
    def build_copy(self):
        ""
        ""
    def clone_tree(self) ->Node :
        top = self.build_copy();
        topchild = []
        topchild = top.get_children()
        child = Node
        for child in self.get_children():
                Newchild = child.clone_tree()
                Newchild.set_parent(top)
                topchild += Newchild
        return top

    def get_parent(self):
        return self.parent

    def set_parent(self,parent):
        self.parent = parent

    def get_min_children_count(self):
        return 3

    def get_max_children_count(self):
        return 3

    def get_first(self) -> Node:
        return self.get_children()[0]

    def get_second(self) -> Node:
        return self.get_children()[1]

    def get_third(self) ->Node:
        return self.get_children()[2]
        
        
        
        
        
        

        
        

        