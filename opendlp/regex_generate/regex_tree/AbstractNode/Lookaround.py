from opendlp.regex_generate.regex_tree.AbstractNode.UnaryOperator import UnaryOperator

class Lookaround (UnaryOperator):

    def __init__(self):
        self.numberQuantifiers = 0
        self.hasOnlyMinMax = True

    def is_valid(self):
        from opendlp.regex_generate.regex_tree.leaf.regex_range import RegexRange
        from opendlp.regex_generate.regex_tree.leaf.anchor import Anchor
        from opendlp.regex_generate.regex_tree.leaf.back_reference import BackReference
        child = self.get_children()[0]
        return child.is_valid() and not(
            isinstance(child, RegexRange)
            or isinstance(child, Anchor)
            or isinstance(child, BackReference)
        )

    def checkQuantifiers(self, root):

        from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers
        from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMax import MatchMinMax
        from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMaxGreedy import MatchMinMaxGreedy
        numberQuantifier = 0
        self.hasOnlyMinMax = True
        if(isinstance(root, Quantifiers)):
            self.hasOnlyMinMax = False
            numberQuantifier += 1
        if(isinstance(root, MatchMinMax) or isinstance(root, MatchMinMaxGreedy)):
            numberQuantifier += 1

        for child in range(root.get_children()):
            self.checkQuantifiers(child)

    def is_look_behind_vaild(self):
        self.checkQuantifiers(self)
        return self.hasOnlyMinMax or (self.numberQuantifiers < 1)
