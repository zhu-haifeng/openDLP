
class RegexContext:
    def __init__(self):
        self.groups = 0
        self.expansion_groups = 0

    def get_groups(self):
        return self.groups

    def inc_groups(self):
        self.groups += 1

    def get_expansion_groups(self):
        return self.expansion_groups

    def inc_expansion_groups(self):
        self.expansion_groups += 1


