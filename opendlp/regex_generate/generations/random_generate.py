
from opendlp.regex_generate.generations.full import Full
from opendlp.regex_generate.generations.growth import Growth
from opendlp.regex_generate.regex_tree.node import Node
from typing import List


class RandomGenerator:
    def __init__(self, max_depth, node_factory):
        self.full = Full(max_depth, node_factory)
        self.growth = Growth(max_depth, node_factory)

    def generate(self, population_size)->List[Node]:
        population = []
        pop_size_full = population_size // 2
        pop_size_growth = population_size - pop_size_full
        population += (self.full.generate(pop_size_full))
        population += (self.growth.generate(pop_size_growth))
        return population
