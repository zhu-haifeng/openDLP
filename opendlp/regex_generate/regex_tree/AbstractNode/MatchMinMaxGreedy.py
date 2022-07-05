
from opendlp.regex_generate.regex_tree.AbstractNode.TernaryOperator import TernaryOperator




class MatchMinMaxGreedy (TernaryOperator):
    MAX_N_GENERATION = 20

    def buildcopy(self):
        return MatchMinMaxGreedy()
    
    def form(self, string, flavour, context):
        self.get_first().form(string, flavour, context)
        string +=("{")
        string +=(int(str(self.get_second())))
        string +=(",")
        string +=(int(str(self.get_third())))
        string +=("}")
        return string

    def is_valid(self):
        from opendlp.regex_generate.regex_tree.AbstractNode.MatchMinMax import MatchMinMax
        from opendlp.regex_generate.regex_tree.leaf.constant import Constant
        from opendlp.regex_generate.regex_tree.AbstractNode.Concatenator import Concatenator
        from opendlp.regex_generate.regex_tree.AbstractNode.Lookaround import Lookaround
        from opendlp.regex_generate.regex_tree.AbstractNode.Quantifier import Quantifiers
        first = self.get_first()
        "检查是否之前的是否输错"
        validFirst = first.is_valid() and not(
            isinstance(first, Concatenator)
            or isinstance(first, Quantifiers)
            or isinstance(first, MatchMinMax)
            or isinstance(first, MatchMinMaxGreedy)
            or isinstance(first, Lookaround))
        second = self.get_second()
        third = self.get_third()

        if(isinstance(third,Constant) and isinstance(second,Constant)):
            try :
                leftValue = int(str(second))
                rightValue = int(str(third))
            except ValueError as ex:
                return False

            if(leftValue < 0 or rightValue < 0):
                return False

            if(leftValue >=rightValue):
                return False
            return validFirst

        return False



        
        
        