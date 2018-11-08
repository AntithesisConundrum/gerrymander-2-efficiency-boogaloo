from constants import *
from generator import generate_voters
from collections import defaultdict

def tally(voters, method):
    """
    Inputs:
        voters - a list of party orders, as returned by generate_voters
        method - a function that takes an order and returns an iterable of the winner(s)
    Output:
        Returns a mapping from party to vote total
    """
    totals = defaultdict(int)
    for voter in voters:
        winners = method(voter)
        for winner in winners:
            totals[winner] += 1
    return totals

def run_election(num_voters, order_probs, method):
    """
    Inputs:
        num_voters - number of voters
        order_probs - mapping from party ordering to probability
        method - a function that takes an order and returns an iterable of the winner(s)
    Output:
        Returns a mapping from party to vote total
    """
    voters = generate_voters(num_voters, order_probs)
    results = tally(voters, method)
    # TODO: Calculate measure of gerrymandering
    return results

if __name__ == "__main__":
    results = run_election(100, BASIC_ORDER_PROBS, )
print run_election