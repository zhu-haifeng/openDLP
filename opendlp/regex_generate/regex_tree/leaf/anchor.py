from opendlp.regex_generate.regex_tree.leaf.leaf import Leaf


class Anchor(Leaf):
    def __init__(self,value :str):
        self.__value = value
        allowedClasses = set(("\\w", "\\d", ".", "\\b", "\\s"))
        # self.__escaped = value.startswith("\\")

    def get_min_children_count(self) -> int:
        return 0

    def get_max_children_count(self) -> int:
        return 0

    def form(self, string: str, flavour=..., context=...):
        return string + self.__value

    def clone_tree(self):
        return Anchor(self.__value)

    def get_parent(self):
        return self.__parent

    def set_parent(self,parent):
        self.__parent = parent

    def is_valid(self):
        return True

    def __str__(self) -> str:
        return self.__value


    def __hash__(self):
        h = 7
        return 13*h + hash(self.__value)

    def __eq__(self,obj)->bool:
        if not obj:
            return False
        if not isinstance(obj,Anchor):
            return False
        if(self.__value != obj.__value):
            return False
        return True


    
