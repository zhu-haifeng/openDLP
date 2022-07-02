
import imp
from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator
# from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMax import MatchMinMax
# from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMaxGreedy import MatchMinMaxGreedy
from opendlp.regex_generate.regex_tree.leaf.anchor import Anchor
# from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround


class Quantifiers(UnaryOperator):
    def is_valid(self):
        child = Node
        print(self.get_children())
        child = self.get_children()[0]
        return child.is_valid() and not(isinstance(child,Quantifiers) or isinstance(child,MatchMinMax) or isinstance(child,MatchMinMaxGreedy) or isinstance(child,Anchor) or isinstance(child,Lookaround))
        