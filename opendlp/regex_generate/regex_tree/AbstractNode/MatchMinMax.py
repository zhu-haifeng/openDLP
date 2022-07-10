from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.TernaryOperator import TernaryOperator


class MatchMinMax (TernaryOperator):

    Max_N_generation = 20

    
    def build_copy(self):
        return MatchMinMax()

    def form(self, string, flavour, context):
        
        from opendlp.regex_generate.regex_tree.AbstractNode.Group import Group
        from opendlp.regex_generate.regex_tree.AbstractNode.NonCapturingGroup import NonCapturingGroup
        tmp = ""
        child = self.get_first()
        index = context.inc_groupss();
        TMP=child.form(tmp, flavour, context)
        l = len(tmp)-1 if child.is_escaped() else len(tmp)
        group = l > 1 and not(child.is_character_class()) and not(
            isinstance(child, Group)) and not(isinstance(child, NonCapturingGroup))
        string = ''
        if (group):
            string += ("(?:")
            string +=(TMP)
            string += (")")
        else:
            string +=(TMP)

        string += ("{")
        string += str(self.get_second())
        string += ","
        string += str(self.get_third())
        string += ("}?")
        return string

    def is_valid(self):
        
        from opendlp.regex_generate.regex_tree.leaf.constant import Constant
        from opendlp.regex_generate.regex_tree.AbstractNode.Concatenator import Concatenator
        from opendlp.regex_generate.regex_tree.leaf.anchor import Anchor
        from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround
        from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers
        from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMaxGreedy import MatchMinMaxGreedy
        first = self.get_first()
        validFirst = first.is_valid() and not(
            isinstance(first, Concatenator)
            or isinstance(first, Quantifiers)
            or isinstance(first, MatchMinMax) or isinstance(first, MatchMinMaxGreedy)
            or isinstance(first, Anchor) or isinstance(first, Lookaround)
        )

        second = self.get_second()
        third = self.get_third()

        if(isinstance(third,Constant) and isinstance(second,Constant)) :
            try :
                leftValue = int(str(self.get_second))
                rightValue = int(str(self.get_third))
            except ValueError as ex:
                return False
            if (leftValue < 0 and rightValue > 0):
                return False
            if(leftValue >= rightValue):
                return False

            return validFirst
        return False

    
        
        
        