
from regex import R
from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class PositiveLookahead (Lookaround) :
    def build_copy(self):
        return PositiveLookahead()

    def form(self, string, flavour, context):
        string = ''
        string +=("(?=")
        string += self.get_children()[0].form(string, flavour, context)
        string +=(")")
        return string

        
        


