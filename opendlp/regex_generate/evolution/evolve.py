from opendlp.regex_generate.generations.random_generate import RandomGenerator
from opendlp.regex_generate.config.evolve_param import EvolveParam
from opendlp.regex_generate.config import conf
from opendlp.regex_generate.fitness.fitness import Fitness
from random import randint
from typing import List
from opendlp.regex_generate.regex_tree.node import Node


def random_idx(len: int) -> int:
    set = set()
    cnt = 0
    while cnt < 7:
        r = randint(0, len-1)
        if r not in set:
            set.add(r)
    return min(set)


def mutate_one(tree: Node) -> Node:
    return tree


def crossover_one_pair(tree_a: Node, tree_b: Node) -> Node:
    return (tree_a, tree_b)


def evolve(evolve_param: EvolveParam, population, fitness_sorted:List[Fitness], rand_generator: RandomGenerator):
    """
    evolve
    @param evolve_param:
    @param population:
    @param fitness_sorted:
    @return: new_population
    """
    pop_out = []
    ori_len = len(fitness_sorted)
    evolve_total = conf.POPULATION_SIZE * evolve_param.evolve_percent
    mutation_cnt = evolve_total * evolve_param.mutation_proba
    crossover_cnt = evolve_total * evolve_param.crossover_proba
    keep_cnt = evolve_total * evolve_param.keep_proba
    cnt = 0
    while cnt < mutation_cnt:
        tree = mutate_one(fitness_sorted[random_idx(ori_len)].tree)
        if tree.is_valid():
            pop_out.append(tree)
            cnt += 1

    cnt = 0
    while cnt < crossover_cnt:
        tree_a, tree_b = crossover_one_pair(
            fitness_sorted[random_idx(ori_len)].tree, fitness_sorted[random_idx(ori_len)].tree)
        if tree_a.is_valid() and tree_b.is_valid():
            pop_out.append(tree_a)
            pop_out.append(tree_b)
            cnt += 2

    cnt = 0
    while cnt < keep_cnt:
        tree = fitness_sorted[random_idx(ori_len)].tree
        if tree.is_valid():
            pop_out.append(tree)
            cnt += 1

    pop_out += rand_generator.generate(conf.POPULATION_SIZE *
                                       evolve_param.random_generate_percent)
    return pop_out
