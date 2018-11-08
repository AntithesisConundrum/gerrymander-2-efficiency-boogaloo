from random import random
from constants import *

def generate_voters(num_voters, order_probs):
    """
    Randomly generate the preferences of num_voters voters.
    Specifically, returns a list of tuples, where each inner tuples is an
    ordering of the parties (represented as integers).
    Order_probs should be a mapping from tuples to its probability (represented
    as floats, where the total sum of values is 1).
    """
    return [weighted_random_choice(order_probs) for _ in xrange(num_voters)]

if __name__ == "__main__":
    print [order_to_labels(o) for o in generate_voters(100, BASIC_ORDER_PROBS)]