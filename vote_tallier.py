from constants import *
from voter_generator import generate_voters
from collections import defaultdict
from voting_systems.classic_stv import *
import random

def run_election(num_voters, order_probs, method):
    """
    Inputs:
        num_voters - number of voters
        order_probs - mapping from party ordering to probability
        method - a function that takes an order and returns the winnning party
                 and a mapping from party to WV
    Output:
        Returns a mapping from party to vote total
    """
    voters = generate_voters(num_voters, order_probs)
    print voters
    winner, wasted_vote = method(voters)
    return winner, wasted_vote

# They all return winner_set, wasted_vote
# Wasted vote is a mapping from party to # (eg FPTP)