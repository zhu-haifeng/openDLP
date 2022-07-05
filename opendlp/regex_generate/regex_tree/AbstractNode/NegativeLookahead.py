from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class NegativeLookahead (Lookaround) :
    def buildcopy(self):
        return NegativeLookahead()

    def form(self, string, flavour, context):
        string +=("(?!")
        self.get_children()[0].form(string, flavour, context)
        string +=(")")
        return string
        
        