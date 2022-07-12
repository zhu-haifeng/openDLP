from random import randint,random
from typing import List, Tuple
from opendlp.regex_generate.generations.random_generate import RandomGenerator
from opendlp.regex_generate.generations.growth import Growth
from opendlp.regex_generate.config.evolve_param import EvolveParam
from opendlp.regex_generate.config import conf
from opendlp.regex_generate.fitness.fitness import Fitness
from random import randint
from typing import List, Tuple
from opendlp.regex_generate.regex_tree.node import Node
from opendlp.regex_generate.regex_tree.leaf.leaf import Leaf
from opendlp.regex_generate.regex_tree.AbstractNode.AbstractNode import AbstractNode


def random_idx(len: int) -> int:
    s = set()
    cnt = 0
    while cnt < 7:
        r = randint(0, len-1)
        if r not in s:
            s.add(r)
            cnt += 1
    return min(s)


def random_node(tree: Node, evolve_param: EvolveParam) -> Tuple[Node, int, Node]:
    root_arr = [(None, -1, tree)]
    child_arr: List[Tuple[AbstractNode, int, Node]] = []
    leaf_arr: List[Tuple[Leaf, int, Node]] = []
    queue: List[Node] = [tree]
    head: int = 0
    while head < len(queue):
        parent = queue[head]
        children = parent.get_children()
        for i, c in enumerate(children):
            if isinstance(c, Leaf):
                leaf_arr.append((parent, i, c))
            else:
                child_arr.append((parent, i, c))
                queue.append(c)
        head += 1
    rand = random()
    if(child_arr != [] and rand < evolve_param.node_crossover_select_proba):
        idx = randint(0,len(child_arr)-1)
        return child_arr[idx]
    rand -= evolve_param.node_crossover_select_proba
    if(leaf_arr != [] and rand < evolve_param.leaf_crossover_select_proba):
        idx = randint(0,len(leaf_arr)-1)
        return leaf_arr[idx]
        
    rand -= evolve_param.leaf_crossover_select_proba
    # if(rand < evolve_param.root_crossover_select_proba):
    return root_arr[0]

def mutate_one(tree: Node,evolve_param: EvolveParam,rand_generator: RandomGenerator) -> Node:
    new_nodes = rand_generator.generate(20)

    for new_node in new_nodes:
        mutant:Node = tree.clone_tree()
        rand_parent, rand_idx, rand_node = random_node(mutant, evolve_param)
        rand_parent.get_children()[rand_idx] = new_node
        new_node.set_parent(rand_parent)
        if(mutant.is_valid()):
            return mutant

    return None


def crossover_one_pair(tree_a: Node, tree_b: Node,evolve_param: EvolveParam) -> Tuple[Node, Node]:
    isvalid = False
    tries = 0
    for tries in range(20):
        new_IndividualA = tree_a.clone_tree()
        new_IndividualB = tree_b.clone_tree()

        parent_A, index_A, node_A = random_node(new_IndividualA, evolve_param)
        parent_B, index_B, node_B = random_node(new_IndividualB, evolve_param)

        if (node_A != None and node_B != None):
            # aParent = randomNodeA.get_parent()
            a_childs = parent_A.get_children()
            b_childs = parent_B.get_children()

            a_childs[index_A] = node_B 
            b_childs[index_B] = node_A

            node_A.set_parent(parent_B)
            node_B.set_parent(parent_A)

            if(#check_Maxdepth(new_IndividualA, 1)
                    # and check_Maxdepth(new_IndividualB, 1)
                    new_IndividualA.is_valid()
                    and new_IndividualB.is_valid()):

                isvalid = True
                break

    if(isvalid):
        return (new_IndividualA, new_IndividualB)
    else:
        return None


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
        tree = mutate_one(fitness_sorted[random_idx(ori_len)].tree, evolve_param, rand_generator)
        if tree and tree.is_valid():
            pop_out.append(tree)
            cnt += 1

    cnt = 0
    while cnt < crossover_cnt:
        tree_a, tree_b = crossover_one_pair(
            fitness_sorted[random_idx(ori_len)].tree, fitness_sorted[random_idx(ori_len)].tree,evolve_param)
        if tree_a and tree_a.is_valid() and tree_b and tree_b.is_valid():
            pop_out.append(tree_a)
            pop_out.append(tree_b)
            cnt += 2

    cnt = 0
    while cnt < keep_cnt:
        tree = fitness_sorted[random_idx(ori_len)].tree
        if tree and tree.is_valid():
            pop_out.append(tree)
            cnt += 1

    pop_out += rand_generator.generate(conf.POPULATION_SIZE *
                                       evolve_param.random_generate_percent)
    return pop_out
