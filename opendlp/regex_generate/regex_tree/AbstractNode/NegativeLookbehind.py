

from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class NegativeLookbehind (Lookaround) :
    def buildcopy(self):
        return NegativeLookbehind()

    def is_valid(self):
        valid = super.is_valid()
        if(valid == 0):
            return valid

        return self.is_look_behind_vaild()

    def form(self, string, flavour, context):
        self +=("(?<!")
        self.get_children()[0].form(self, string, flavour, context)
        self +=(")")
        return string
            
        

        
        