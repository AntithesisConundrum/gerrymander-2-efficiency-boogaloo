from vote_utils import *
from collections import defaultdict

def stv_complete_tally(voters):
    """
    Tallies votes in a single transferrable vote scheme.
    Continues running rounds of elections until there is only one party left.

    Returns a mapping from each party to their votes when eliminated (or in the last contested
    round for the winner)
    """
    complete = False
    output_mapping = {}
    eliminated_parties = set()
    num_elminiated_parties = 1
    num_candidates = len(voters[0])
    while not complete:
        # Tally the results for this round
        parties_to_votes = defaultdict(int)
        for voter in voters:
            # Find the first party that hasn't been eliminated.
            for party in voter:
                if party not in eliminated_parties:
                    parties_to_votes[party] += 1
                    break

        # Find the loser
        loser = find_loser(parties_to_votes)

        # Eliminate the loser and note their vote total
        eliminated_parties.add(loser)
        output_mapping[loser] = parties_to_votes[loser]

        if num_elminiated_parties == num_candidates - 1:
            complete = True
            for party in voters[0]:
                if party not in eliminated_parties:
                    output_mapping[party] = parties_to_votes[party]
        num_elminiated_parties += 1
    return output_mapping

def complete_single_transferrable_vote(voters):
    """
    Runs an STV election.
        Variation: Continues running rounds until there is only one 
    """
    # Tally the votes
    parties_to_votes = stv_complete_tally(voters)

    # Find the ordering
    ordering = order_parties(parties_to_votes)

    # Calculate wasted vote
    wasted_vote = classic_wasted_vote(parties_to_votes)

    return ordering, wasted_vote
