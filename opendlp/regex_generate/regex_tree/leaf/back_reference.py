from opendlp.regex_generate.regex_tree.leaf.leaf import Leaf

from opendlp.regex_generate.config.conf import RegexFlavour
from opendlp.regex_generate.regex_tree.regex_context import RegexContext


class BackReference(Leaf):
    def __init__(self,value :int):
        self.__value = value


    def get_min_children_count(self) -> int:
        return 0

    def get_max_children_count(self) -> int:
        return 0

    def form(self, string: str, flavour=..., context=...):
        # ans = string +"//"
        # if(flavour==RegexFlavour.Java):
        #     return ans + self.__value
        # else:
        #     return ans + self.__value+context.inc_expansion_groups()
        return "//" + str(self.__value)

    def clone_tree(self):
        return BackReference(self.__value)

    def get_parent(self):
        return self.__parent

    def set_parent(self,parent):
        self.__parent = parent

    def is_valid(self):
        return True

    def __str__(self) -> str:
        return self.__value

    def is_character_class(self):
        return self.__char_class

    def __hash__(self):
        h = 9
        return 17*h + hash(self.__value)

    def __eq__(self,obj)->bool:
        if not obj:
            return False
        if not isinstance(obj,BackReference):
            return False
        if(self.__value != obj.__value):
            return False
        return True


    
