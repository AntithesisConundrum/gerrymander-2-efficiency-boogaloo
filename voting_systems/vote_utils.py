def order_parties(parties_to_votes):
    """
    Takes a mapping from parties to votes
    Returns the parties ordered by vote total
    The party at index ZERO is the winner.
    """
    return sorted(parties_to_votes.keys(), key=lambda p: -1*parties_to_votes[p])

def find_winner_and_runner_up(parties_to_votes):
    """
    Takes a mapping from parties to votes
    Returns the winner and the runner up
    """
    ordering = order_parties(parties_to_votes)
    return ordering[0], ordering[1]

def find_loser(parties_to_votes):
    """
    Takes a mapping from parties to votes
    Returns the loser
    """
    ordering = order_parties(parties_to_votes)
    return ordering[-1]

def classic_wasted_vote(parties_to_votes):
    """
    Calculates the "classic" wasted vote:
        The wasted vote of the winner is the number of votes past 50%+1
        The wasted vote of the loser is the number of votes

    Returns mapping from party to number of votes
    """
    # Find the winner and the runner up
    winner, runner_up = find_winner_and_runner_up(parties_to_votes)
    # Calculate wasted vote
    wasted_vote = dict(parties_to_votes)
    wasted_vote[winner] = parties_to_votes[winner] - (parties_to_votes[runner_up] + 1)
    return wasted_vote


def calculate_wasted_ballot_efficiency_gap(winner, voters):
    """
    Calculates the wasted ballot-based efficiency gap.
    """
    ballots_for_winner = 0
    ballots_against_winner = 0

    # We divide based on whether the winner was in the top half.
    for voter in voters:
        winner_found = False
        for i in xrange(len(voter)/2):
            if voter[i] == winner:
                winner_found = True
                break
        if winner_found:
            ballots_for_winner += 1
        else:
            ballots_against_winner += 1
    wasted_ballots_for_winner = ballots_for_winner - (ballots_against_winner-1)
    wasted_ballots_against_winner = ballots_against_winner
    return (wasted_ballots_for_winner-wasted_ballots_against_winner)/float(len(voters))
