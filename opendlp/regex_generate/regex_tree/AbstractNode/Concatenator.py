
from opendlp.regex_generate.regex_tree.AbstractNode.BinaryOperator import BinaryOperator
# from opendlp.regex_generate.regex_tree.AbstractNode.Or import Or


class Concatenator(BinaryOperator):

    def buildcopy(self):
        return Concatenator()

    
    def form(self, string, flavour, context):
        string += self.getLeft().form(string, flavour, context) + self.getRight().form(string, flavour, context)
        return  string
        
    def is_vaild(self):
        if (isinstance(self.getLeft(), Or) or isinstance(self.getRight, Or)):
            return False
        return self.getLeft().is_valid() and self.getRight().is_valid()

        