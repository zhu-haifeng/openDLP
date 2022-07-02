
from opendlp.regex_generate.regex_tree.AbstractNode.BinaryOperator import BinaryOperator
from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers

class Or(BinaryOperator):
    def buildCopy(self):
        return self

    def form(self, string, flavour, context):
        if (isinstance(self.get_parent(), Quantifiers)):
            self += ("(?:")

        self.getLeft().form(self, string, flavour, context)
        self  += ("|")
        self.getRight().form(self, string, flavour, context)
        if (isinstance(self.get_parent(),Quantifiers)):
            self += (")")
        return string
    
    def is_vaild(self):
        if(isinstance(self.getLeft(), Quantifiers) or isinstance(self.getRight(),Quantifiers)):
            return False
        
        return self.getLeft().is_valid() and self.getRight().is_valid()
        

        
        
        