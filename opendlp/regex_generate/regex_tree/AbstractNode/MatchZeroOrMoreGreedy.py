from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers

class MatchZeroOrMoreGreedy (Quantifiers):
    def build_copy(self):
        return MatchZeroOrMoreGreedy()

    def form(self, string, flavour, context):
        string = ''
        string += self.get_children()[0].form(string, flavour, context)
        string +=("*")
        return string