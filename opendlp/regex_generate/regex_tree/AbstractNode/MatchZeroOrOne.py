from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.regex_context import RegexContext
from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers


class MatchZeroOrOne (Quantifiers) :
    def buildcopy(self):
        return MatchZeroOrOne()

    def form(self, string, flavour, context: RegexContext):
        from opendlp.regex_generate.regex_tree.AbstractNode.Group import Group
        from opendlp.regex_generate.regex_tree.AbstractNode.NonCapturingGroup import NonCapturingGroup
        tmp = []
        child = Node
        child = self.get_children()[0]
        index = context.inc_groups()
        child.form(tmp, flavour, context)
        l = tmp.len()-1 if child.is_escaped() else tmp.length()
        group = l > 1 and not(child.is_character_class()) and  not(isinstance(child, Group)) and not(isinstance(child,NonCapturingGroup))
        if(group):
            string +=("(?:")
            string.add(tmp)
            string +=(")")
        else:
            string.add(tmp)
        
        string +=("?+")
        return string
        
        