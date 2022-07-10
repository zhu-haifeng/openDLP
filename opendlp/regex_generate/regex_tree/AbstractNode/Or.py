
from opendlp.regex_generate.regex_tree.AbstractNode.BinaryOperator import BinaryOperator
from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers

class Or(BinaryOperator):
    def build_copy(self):
        return Or()

    def form(self, string, flavour, context):
        string = ''
        if (isinstance(self.get_parent(), Quantifiers)):
            string += ("(?:")

        string += self.getLeft().form(string, flavour, context)
        self  += ("|")
        string += self.getRight().form(string, flavour, context)
        if (isinstance(self.get_parent(),Quantifiers)):
            string += (")")
        return string
    
    def is_vaild(self):
        if(isinstance(self.getLeft(), Quantifiers) or isinstance(self.getRight(),Quantifiers)):
            return False
        
        return self.getLeft().is_valid() and self.getRight().is_valid()
        

        
        
        