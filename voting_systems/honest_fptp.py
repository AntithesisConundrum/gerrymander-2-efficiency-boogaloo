from vote_utils import *
from collections import defaultdict

def honest_tally(voters):
    """
    Takes some voters, returns the first choice of those voters.
    """
    parties_to_votes = defaultdict(int)
    for voter in voters:
        preferred_party = voter[0]
        parties_to_votes[preferred_party] += 1
    return parties_to_votes

def honest_fptp(voters):
    """
    Runs an honest first-past-the-post election.
    Wasted vote is calculated as in the canonical EG:
        Winner WV is number of votes past 50%+1
        Loser WV is number of votes
    """
    # Tally the votes
    parties_to_votes = honest_tally(voters)

    # Find the ordering
    ordering = order_parties(parties_to_votes)

    # Calculate wasted vote
    wasted_vote = classic_wasted_vote(parties_to_votes)

    return ordering, wasted_vote
