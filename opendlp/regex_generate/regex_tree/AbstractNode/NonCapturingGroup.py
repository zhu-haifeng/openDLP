
from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator


class NonCapturingGroup (UnaryOperator) :
    def buildcopy(self):
        return NonCapturingGroup()

    def form(self, string, flavour, context):
        self +=("(?:")
        self.get_children()[0].form(self, string, flavour, context)
        self +=(")")
        return string

    def is_valid(self):
        return self.get_children()[0].is_valid()
        
        
    
        

