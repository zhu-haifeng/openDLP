from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator

class ListNotMatch (UnaryOperator) :
    def build_copy(self):
        return ListNotMatch()

    def form(self, string, flavour, context):
        child = self.get_children()[0]
        string = ""
        string += ("[^")
        string += child.form(string, flavour, context)
        string += ("]")
        return string

    def is_valid(self):
        return self.check_valid(self.get_children()[0])

    def check_valid(root,self):
        
        from opendlp.regex_generate.regex_tree.leaf.constant import Constant
        from opendlp.regex_generate.regex_tree.leaf.regex_range import RegexRange
        from opendlp.regex_generate.regex_tree.AbstractNode.Concatenator import Concatenator
        if(not(isinstance(root,Constant) or isinstance(root,RegexRange) or isinstance(root,Concatenator))):
            return False

        for child in range(root.get_children()):
            if(not(self.check_valid(child))):
                return False

        return True

    def is_Character_class(self):
        return True
        
        
        
        
        