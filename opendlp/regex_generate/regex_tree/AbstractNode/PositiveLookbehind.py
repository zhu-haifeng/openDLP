
from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class PositiveLookbehind (Lookaround):
    def buildcopy(self):
        return PositiveLookbehind()

    def is_valid(self):
        valid = super.is_valid()
        if(valid == 0):
            return valid
        
        return is_look_behind_valid()

    def form(self, string, flavour, context):
        self +=("(?<=")
        self.get_children()[0].form(self, string, flavour, context)
        self +=(")")
        return string
        
        
        
