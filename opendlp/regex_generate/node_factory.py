from ast import Constant
from opendlp.regex_generate.regex_tree.leaf.constant import Constant
from opendlp.regex_generate.regex_tree.leaf.regex_range import RegexRange
from opendlp.regex_generate.regex_tree.AbstractNode.Concatenator import Concatenator
from opendlp.regex_generate.regex_tree.AbstractNode.Group import Group
from opendlp.regex_generate.regex_tree.AbstractNode.ListMatch import ListMatch
from opendlp.regex_generate.regex_tree.AbstractNode.ListNotMatch import ListNotMatch
from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMax import MatchMinMax
from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMaxGreedy import MatchMinMaxGreedy
from opendlp.regex_generate.regex_tree.AbstractNode.MatchOneOrMore import MatchOneOrMore
from opendlp.regex_generate.regex_tree.AbstractNode.MatchOneOrMoreGreedy import MatchOneOrMoreGreedy
from opendlp.regex_generate.regex_tree.AbstractNode.MatchZeroOrOne import MatchZeroOrOne
from opendlp.regex_generate.regex_tree.AbstractNode.MatchZeroOrOneGreedy import MatchZeroOrOneGreedy
from opendlp.regex_generate.regex_tree.AbstractNode.MatchZeroOrMore import MatchZeroOrMore
from opendlp.regex_generate.regex_tree.AbstractNode.MatchZeroOrOneGreedy import MatchZeroOrOneGreedy
from opendlp.regex_generate.regex_tree.AbstractNode.MatchZeroOrMore import MatchZeroOrMore
from opendlp.regex_generate.regex_tree.AbstractNode.MatchZeroOrMoreGreedy import MatchZeroOrMoreGreedy
from opendlp.regex_generate.regex_tree.AbstractNode.NegativeLookahead import NegativeLookahead
from opendlp.regex_generate.regex_tree.AbstractNode.NegativeLookbehind import NegativeLookbehind
from opendlp.regex_generate.regex_tree.AbstractNode.NonCapturingGroup import NonCapturingGroup
from opendlp.regex_generate.regex_tree.AbstractNode.Or import Or
from opendlp.regex_generate.regex_tree.AbstractNode.PositiveLookahead import PositiveLookahead
from opendlp.regex_generate.regex_tree.AbstractNode.PositiveLookbehind import PositiveLookbehind
from opendlp.regex_generate.regex_tree.AbstractNode.PositiveLookahead import PositiveLookahead
from opendlp.regex_generate.regex_tree.AbstractNode.PositiveLookbehind import PositiveLookbehind


class NodeFactory:
    def __init__(self):
        self.terminal_set = []
        self.function_set = []

    def build_terminal_set(self, bpe_tokens):
        """
        load default terminal set
        @return:
        """
        constants = [
            "\\d",
            "\\w",
            "\\.", ":", ",", ";",
            "_", "=", "\"", "'",
            "\\\\",
            "/",
            "\\?", "\\!",
            "\\}", "\\{", "\\(", "\\)", "\\[", "\\]", "<", ">",
            "@", "#", " ", " "
        ]
        ranges = []
        constants += list(bpe_tokens)
        for c in constants:
            self.terminal_set.append(Constant(c))
        for s in ranges:
            self.terminal_set.append(RegexRange(s))

    def build_function_set(self):
        """
        load default terminal set
        @return:
        """
        self.function_set = [
            Concatenator(),         Or(),
            MatchMinMax(),          MatchMinMaxGreedy(),
            PositiveLookahead(),    NegativeLookahead(),
            PositiveLookbehind(),   NegativeLookbehind(),
            MatchOneOrMore(),       MatchOneOrMoreGreedy(),
            MatchZeroOrMore(),      MatchZeroOrMoreGreedy(),
            MatchZeroOrOne(),       MatchZeroOrOneGreedy(),
            Group(),                NonCapturingGroup(),
            ListMatch(),            ListNotMatch()
        ]

        self.function_set = [
            Concatenator(),         Or(),
            MatchMinMax(),
            MatchOneOrMore(),
            MatchZeroOrMore(),
            MatchZeroOrOne(),
            Group(),                NonCapturingGroup(),
            ListMatch(),            ListNotMatch()
        ]


    def build(self, bpe_tokens=None):
        self.build_terminal_set(bpe_tokens)
        self.build_function_set()