from abc import abstractmethod
from pickle import FALSE


from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.TernaryOperator import TernaryOperator
from opendlp.regex_generate.regex_tree.AbstractNode.Group import Group
# from opendlp.regex_generate.regex_tree.AbstractNode.NonCapturingGroup import NonCapturingGroup
from opendlp.regex_generate.regex_tree.leaf.constant import Constant
# from opendlp.regex_generate.regex_tree.AbstractNode.Concatenator import Concatenator
from opendlp.regex_generate.regex_tree.leaf.anchor import Anchor
# from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround
# from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers
# from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMaxGreedy import MatchMinMaxGreedy


class MatchMinMax (TernaryOperator):

    Max_N_generation = 20

    
    def buildcopy(self):
        return MatchMinMax()

    def form(self, string, flavour, context):
        tmp = []
        child = Node
        child = self.get_first()
        index = context.incGroups();
        child.form(self, tmp, flavour, context)
        l = tmp.length()-1 if child.is_escaped() else tmp.length()
        group = l > 1 and not(child.is_character_class()) and not(isinstance(child, Group)) and not(isinstance(child,NonCapturingGroup))

        if (group):
            string += ("(?:")
            string += (tmp)
            string += (")")
        else:
            string += (tmp)

        string += ("{")
        string += (int(str(self.get_second())))
        string += (",")
        string += (int(str(self.get_third())))
        string +=("}+")
        return string

    def is_valid(self):
        first = self.get_first()
        validFirst = first.is_valid() and not(isinstance(first, Concatenator) or isinstance(first,Quantifiers) or isinstance(first,MatchMinMax) or isinstance(first,MatchMinMaxGreedy) or isinstance(first, Anchor) or isinstance(first, Lookaround))

        second  = self.get_second()
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

    
        
        
        