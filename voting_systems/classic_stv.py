from vote_utils import *
from collections import defaultdict

def stv_classic_tally(voters):
    """
    Tallies votes in a single transferrable vote scheme.
    Continues running rounds of elections until a party reaches 50% of the vote.

    Returns a mapping from each party to their votes when eliminated (or in the last contested
    round for the winner)
    """
    threshold = len(voters)/2
    complete = False
    output_mapping = {}
    eliminated_parties = set()
    num_elminiated_parties = 1
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

        # Check if the threshold had been crossed
        if max(parties_to_votes.values()) >= threshold:
            complete = True
            for party in voters[0]:
                if party not in eliminated_parties:
                    output_mapping[party] = parties_to_votes[party]
        num_elminiated_parties += 1
    return output_mapping

def classic_single_transferrable_vote(voters):
    """
    Runs an STV election.
    """
    # Tally the votes
    parties_to_votes = stv_classic_tally(voters)

    # Find the ordering
    ordering = order_parties(parties_to_votes)

    # Calculate wasted vote
    wasted_vote = classic_wasted_vote(parties_to_votes)

    return ordering, wasted_vote
