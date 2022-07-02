from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers

class MatchZeroOrMoreGreedy (Quantifiers):
    def buildcopy(self):
        return MatchZeroOrMoreGreedy()

    def form(self, string, flavour, context):
        self.get_children()[0].form(self, string, flavour, context)
        string +=("*")
        return string