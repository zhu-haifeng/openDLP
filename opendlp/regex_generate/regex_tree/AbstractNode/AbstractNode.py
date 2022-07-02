from abc import abstractmethod
import re

from opendlp.regex_generate.config.conf import RegexFlavour
from opendlp.regex_generate.regex_tree.id_factory import IDFactory
from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.regex_context import RegexContext



class AbstractNode (Node):
    def __init__(self):
        # pass
        self.id=IDFactory.next_id()
        self.children = []

    # def is_character_class(self):
    #     return False
    
    # def is_escaped(self):
    #     return False

    def get_children(self,):
        print ("abstract get_children")
        return self.children

    # def get_id(self):
    #     return self.id
        
    # @abstractmethod
    # def get_min_children_count(self) -> int:
    #     """
    #     """
    
    # @abstractmethod
    # def get_max_children_count(self) -> int: 
    #     """
    #     """
    
    # @abstractmethod
    # def AbstractNode(self):
    #     self.id = IDFactory.next_id
    #     self.children = [](Node.get_max_children_count())

    # @abstractmethod
    # def form(self, string, flavour=RegexFlavour.Python, context=RegexContext()):
    #     """
    #     """
        

        
        

        


