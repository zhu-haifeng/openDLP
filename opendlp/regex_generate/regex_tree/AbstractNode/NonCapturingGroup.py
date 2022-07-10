
from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator


class NonCapturingGroup (UnaryOperator) :
    def build_copy(self):
        return NonCapturingGroup()

    def form(self, string, flavour, context):
        string = ''
        string +=("(?:")
        string += self.get_children()[0].form(string, flavour, context)
        string +=(")")
        return string

    def is_valid(self):
        return self.get_children()[0].is_valid()
        
        
    
        

