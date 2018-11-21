from vote_utils import *
from collections import defaultdict

def borda_tally(voters):
    """
    Tallies votes according to a borda scheme.
    Specifically, the last place party gets 0 points, the second-to-last gets 1 point, etc.
    """
    parties_to_points = defaultdict(int)
    num_candidates = len(voters[0])
    for voter in voters:
        for party_idx in xrange(num_candidates):
            party = voter[party_idx]
            parties_to_points[party] += (num_candidates - 1) - party_idx
    return parties_to_points

def borda_count_vote(voters):
    """
    Runs a borda count election.
    Returns the winner and the "wasted points"
    """
    # Tally the votes
    parties_to_points = borda_tally(voters)

    # Find the ordering
    ordering = order_parties(parties_to_points)

    # Calculate wasted wasted_points
    wasted_points = classic_wasted_vote(parties_to_points)

    return ordering, wasted_points
