from abc import abstractmethod
import this

from pandas._libs.tslibs.timedeltas import parse_timedelta_unit

from opendlp.regex_generate.regex_tree.node import Node
<<<<<<< HEAD
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode
=======
from opendlp.regex_generate.regex_tree.AbstractNode import AbstractNode
>>>>>>> my/dev



class BinaryOperator (AbstractNode):
    parent = Node



    def __init__(self):
        # self.parent = []
        ""
        ""

    def get_min_children_count() -> int:
        return 2

    def get_max_children_count() -> int:
        return 2

    def getLeft(self):
        return self.get_children()[0]

    def getRight(self):
        return self.get_children()[1]

        
    @abstractmethod
    def buildCopy(self):
        ""
        ""
       
    
    
    def cloneTree() ->Node :
        bop = buildCopy()
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
        
    


            
        
