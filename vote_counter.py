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
    out = []
    for i in xrange(num_voters):
        total = 0
        rand = random()
        for order in order_probs:
            total += order_probs[order]
            # Strictly <; if prob is 0, we want 0 chance.
            if rand < total:
                out.append(order)
                break
                # Maybe add defensive-programming check that something is added?
    return out

print [order_to_labels(o) for o in generate_voters(100, BASIC_ORDER_PROBS)]