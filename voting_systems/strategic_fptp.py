from vote_utils import *
from honest_fptp import honest_tally
import random
from collections import defaultdict

def strategic_tally(voters, honesty):
    """
    Tallies votes in a strategic manner.
    This means that people will vote for one of the two most popular parties under honest preference;
        the exception is the honesty proportion. (e.g. if honesty = 0.05 then 5% vote honestly)
    """
    # Determine the winner and runner up in the district
    winner, runner_up = find_winner_and_runner_up(honest_tally(voters))

    # Tally votes in a strategic manner.
    parties_to_votes = defaultdict(int)
    for voter in voters:
        r = random.random()

        if r < honesty: # This is the "honest" case
            preferred_party = voter[0]
        else: # This is the "strategic" case
            # Find if the voter prefers winner or runner_up
            for party in voter:
                if party == winner or party == runner_up:
                    preferred_party = party
                    break
        parties_to_votes[preferred_party] += 1 
    return parties_to_votes


def strategic_fptp(voters, honesty=0.05):
    """
    Runs an strategic first-past-the-post election.
    This means that people will vote for one of the two most popular parties under honest preference;
        the exception is the honesty proportion. (e.g. if honesty = 0.05 then 5% vote honestly)

    Wasted vote is calculated as in the canonical EG:
        Winner WV is number of votes past 50%+1
        Loser WV is number of votes
    """
    # Tally votes
    parties_to_votes = strategic_tally(voters, honesty)

    # Find the ordering
    ordering = order_parties(parties_to_votes)

    # Calculate wasted vote
    wasted_vote = classic_wasted_vote(parties_to_votes)

    return ordering, wasted_vote