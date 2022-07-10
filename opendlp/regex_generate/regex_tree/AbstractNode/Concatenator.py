
from opendlp.regex_generate.regex_tree.AbstractNode.BinaryOperator import BinaryOperator

class Concatenator(BinaryOperator):

    def build_copy(self):
        return Concatenator()

    
    def form(self, string, flavour, context):
        string = ''
        string += self.getLeft().form(string, flavour, context) 
        string += self.getRight().form(string, flavour, context)
        return  string
        
    def is_vaild(self):
        from opendlp.regex_generate.regex_tree.AbstractNode.Or import Or
        if (isinstance(self.getLeft(), Or) or isinstance(self.getRight, Or)):
            return False
        return self.getLeft().is_valid() and self.getRight().is_valid()

        