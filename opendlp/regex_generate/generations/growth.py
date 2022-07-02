from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.leaf.leaf import Leaf
from typing import List
from random import randint
from opendlp.regex_generate.node_factory import NodeFactory

class Growth:
    def __init__(self, max_depth, node_factory:NodeFactory):
        self.max_depth = max_depth
        self.node_factory = node_factory

    def generate(self, population_size: int) -> List[Node]:
        """
        generate regex trees with fixed depth.
        @param population_size: tree nums to be generate
        @return:
        """
        population = []

        i = 0
        while i < population_size:
            candidate = self.grow(1)
            if(candidate.is_valid()):
                population.append(candidate)
            i += 1
        return population

    def grow(self, depth: int) -> Node:
        tree: Node = self.randomFunction()
        if(depth >= self.max_depth-1):
            # for i in range(tree.get_max_children_count()-tree.get_min_children_count(), tree.get_max_children_count()):
            # TODO：
            for i in range(tree.get_max_children_count()):
                leaf: Leaf = self.randomLeaf()
                leaf.set_parent(tree)
                tree.get_children().append(leaf)
        else:
            for i in range(tree.get_max_children_count()):
                if(randint(0, 1)):
                    leaf: Leaf = self.randomLeaf()
                    leaf.set_parent(tree)
                    tree.get_children().append(leaf)
                else:
                    node: Node = self.grow(depth+1)
                    node.set_parent(tree)
                    tree.get_children().append(node)
        return tree

    def randomFunction(self):
        return self.node_factory.function_set[randint(0, len(self.node_factory.function_set)-1)]

    def randomLeaf(self) -> Leaf:
        return self.node_factory.terminal_set[randint(0, len(self.node_factory.terminal_set)-1)]
