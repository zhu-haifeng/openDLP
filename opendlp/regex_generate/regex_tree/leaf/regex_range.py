from opendlp.regex_generate.regex_tree.leaf.leaf import Leaf


class RegexRange(Leaf):
    def __init__(self, value: str):
        self.__value = value

    def get_min_children_count(self) -> int:
        return 0

    def get_max_children_count(self) -> int:
        return 0

    def form(self, string: str, flavour=..., context=...):
        # return string + self.__value
        return self.__value

    def clone_tree(self):
        return RegexRange(self.__value)

    def get_parent(self):
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    """
        Valido solo se sono all'interno di ListMatch o ListNotMatch
    """

    def is_valid(self):
        return False

    def __str__(self) -> str:
        return self.__value

    def is_character_class(self):
        return True

    def __hash__(self):
        h = 3
        return 79*h + hash(self.__value)

    def __eq__(self, obj) -> bool:
        if not obj:
            return False
        if not isinstance(obj, RegexRange):
            return False
        if(self.__value != obj.__value):
            return False
        return True
