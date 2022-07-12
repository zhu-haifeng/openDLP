from asyncio.windows_events import NULL
from curses.ascii import NUL
from hashlib import new
from xmlrpc.client import boolean

from regex import B
from opendlp.regex_generate.generations.random_generate import RandomGenerator
from opendlp.regex_generate.config.evolve_param import EvolveParam
from opendlp.regex_generate.config import conf
from opendlp.regex_generate.fitness.fitness import Fitness
from random import randint
from typing import List, Tuple
from opendlp.regex_generate.regex_tree.node import Node


def random_idx(len: int) -> int:
    s = set()
    cnt = 0
    while cnt < 7:
        r = randint(0, len-1)
        if r not in s:
            s.add(r)
            cnt += 1
    return min(s)


def random_node(tree: Node):
    ""
    ""


def mutate_one(tree: Node) -> Node:
    return tree



def check_Maxdepth(root:Node , depth:int ):

    return True

    


def crossover_one_pair(tree_a: Node, tree_b: Node) -> Tuple[Node, Node]:
    isvalid = False
    tries = 0
    for tries in range(20):
        new_IndividualA = tree_a.clone_tree()
        new_IndividualB = tree_b.clone_tree()

        parent_A, index_A, node_A = random_node(new_IndividualA)
        parent_B, index_B, node_B = random_node(new_IndividualB)

        if (node_A != NULL and node_B != NULL):
            # aParent = randomNodeA.get_parent()
            a_childs = parent_A.get_children()
            b_childs = parent_B.get_children()

            a_childs.set(index_A, node_B) # set??????
            b_childs.set(index_B, node_A)

            new_IndividualA.set_parent(parent_B)
            new_IndividualB.set_parent(parent_A)

            if(#check_Maxdepth(new_IndividualA, 1)
                    # and check_Maxdepth(new_IndividualB, 1)
                    new_IndividualA.is_valid()
                    and new_IndividualB.is_valid()):

                isvalid = True
                break

    if(isvalid):
        return [new_IndividualA, new_IndividualB]
    else:
        return NULL


def evolve(evolve_param: EvolveParam, population, fitness_sorted: List[Fitness], rand_generator: RandomGenerator):
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
