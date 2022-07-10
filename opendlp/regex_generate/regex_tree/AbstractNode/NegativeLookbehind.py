

from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class NegativeLookbehind (Lookaround) :
    def build_copy(self):
        return NegativeLookbehind()

    def is_valid(self):
        valid = super.is_valid()
        if(valid == 0):
            return valid

        return self.is_look_behind_vaild()

    def form(self, string, flavour, context):
        string = ''
        string +=("(?<!")
        string += self.get_children()[0].form(string, flavour, context)
        string +=(")")
        return string
            
        

        
        