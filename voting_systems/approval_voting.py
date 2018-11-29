from vote_utils import *
from collections import defaultdict

def approval_tally(voters, approve_proportion):
    """
    Tallies votes in an approval voting scheme.
    Voters approve approve_proportion of the parties.
    """
    parties_to_votes = defaultdict(int)
    num_approved_parties = int(len(voters[0]) * approve_proportion) # Truncates
    ballots = []
    for voter in voters:
        # Add a vote for the first num_approved_parties parties.
        ballot = [None] * 2
        for i in xrange(num_approved_parties):
            parties_to_votes[voter[i]] += 1
            ballot[i] = voter[i]
        ballots.append(ballot)
    return parties_to_votes, ballots

def approval_voting(voters, approve_proportion=0.5):
    """
    Runs an approval vote.
    Wasted vote is calculated as in the canonical EG:
        Winner WV is number of votes past 50%+1
        Loser WV is number of votes
    """
    # Tally the votes
    parties_to_votes, ballots = approval_tally(voters, approve_proportion)

    # Find the ordering
    ordering = order_parties(parties_to_votes)

    # Calculate wasted vote
    wasted_vote = classic_wasted_vote(parties_to_votes)

    return ordering, wasted_vote
