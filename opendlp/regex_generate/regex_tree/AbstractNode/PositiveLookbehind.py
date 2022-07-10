
from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class PositiveLookbehind (Lookaround):
    def build_copy(self):
        return PositiveLookbehind()

    def is_valid(self):
        valid = super.is_valid()
        if(valid == 0):
            return valid
        
        return self.is_look_behind_valid()

    def form(self, string, flavour, context):
        string = ''
        string +=("(?<=")
        self.get_children()[0].form(string, flavour, context)
        string +=(")")
        return string
        
        
        
