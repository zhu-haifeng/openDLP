from abc import abstractmethod
from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode



class BinaryOperator (AbstractNode):
    parent = Node
    def __init__(self):
        super().__init__()


    def get_min_children_count(self) -> int:
        return 2

    def get_max_children_count(self) -> int:
        return 2

    def getLeft(self):
        return self.get_children()[0]

    def getRight(self):
        return self.get_children()[1]

        
    @abstractmethod
    def build_copy(self):
        ""
        ""
       
    
    
    def cloneTree() ->Node :
        bop = build_copy()
        bopChild = []
        bopChild = bop.get_children()
        child = Node
        for child in range(this.get_children()):
            newChild = child.clone_tree()
            newChild.set_parent(bop)
            bopChild += (newChild)
        
        return bop
        
    def get_parent(self):
        return self.parent

    def set_parent(self,parent):
        self.parent =parent
        
    


            
        
