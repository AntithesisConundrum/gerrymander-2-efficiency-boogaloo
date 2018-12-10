import csv
from constants import *
from voter_generator import generate_voters
from voting_systems.vote_utils import *
from voting_systems.approval_voting import approval_voting
from voting_systems.borda_count import borda_count_vote
from voting_systems.classic_stv import classic_single_transferrable_vote
from voting_systems.complete_stv import complete_single_transferrable_vote
from voting_systems.honest_fptp import honest_fptp
from voting_systems.strategic_fptp import strategic_fptp


def calculate_top_two_ratio(ordering, wasted_votes):
    """
    Calculate the ratio between the winner and the second place
    finisher's wasted votes.
    """
    winner = ordering[0]
    runner_up = ordering[1]
    return float(wasted_votes[winner]) / float(wasted_votes[runner_up])

def calculate_total_ratio(ordering, wasted_votes):
    """
    Calculate the ratio between the winner and the second place
    finisher's wasted votes.
    """
    winner = ordering[0]
    loser_total = 0.0
    for loser in ordering[1:]:
        loser_total += wasted_votes[loser]
    return float(wasted_votes[winner]) / loser_total

def run_experiment(out_name, distribution):
    out_file = open(out_name, 'wb')
    out_writer = csv.writer(out_file)

    out_writer.writerow(["Honest_FPTP_Winner",
        "Honest_FPTP_Top_Two_Ratio",
        "Honest_FPTP_Total_Ratio",
        "Strategic_FPTP_Winner",
        "Strategic_FPTP_Top_Two_Ratio",
        "Strategic_FPTP_Total_Ratio",
        "Approval_Winner",
        "Approval_Top_Two_Ratio",
        "Approval_Total_Ratio",
        "Borda_Winner",
        "Borda_Top_Two_Ratio",
        "Borda_Total_Ratio",
        "Classic_STV_Winner",
        "Classic_STV_Top_Two_Ratio",
        "Classic_STV_Total_Ratio",
        "Complete_STV_Winner",
        "Complete_STV_Top_Two_Ratio",
        "Complete_STV_Total_Ratio",
        ])

    num_trials = 100
    num_voters = 100000
    for _ in xrange(num_trials):
        electorate = generate_voters(num_voters, distribution)

        # Honest FPTP
        ordering, wasted_votes = honest_fptp(electorate)
        honest_fptp_winner = PARTY_LABELS[ordering[0]]
        honest_fptp_top_two_ratio = calculate_top_two_ratio(ordering, wasted_votes)
        honest_fptp_total_ratio = calculate_total_ratio(ordering, wasted_votes)

        # Strategic FPTP
        ordering, wasted_votes = strategic_fptp(electorate)
        strategic_fptp_winner = PARTY_LABELS[ordering[0]]
        strategic_fptp_top_two_ratio = calculate_top_two_ratio(ordering, wasted_votes)
        strategic_fptp_total_ratio = calculate_total_ratio(ordering, wasted_votes)

        # Approval Voting
        ordering, wasted_votes = approval_voting(electorate)
        approval_winner = PARTY_LABELS[ordering[0]]
        approval_top_two_ratio = calculate_top_two_ratio(ordering, wasted_votes)
        approval_total_ratio = calculate_total_ratio(ordering, wasted_votes)

        # Borda count
        ordering, wasted_votes = borda_count_vote(electorate)
        borda_winner = PARTY_LABELS[ordering[0]]
        borda_top_two_ratio = calculate_top_two_ratio(ordering, wasted_votes)
        borda_total_ratio = calculate_total_ratio(ordering, wasted_votes)

        # Classic STV
        ordering, wasted_votes = classic_single_transferrable_vote(electorate)
        classic_stv_winner = PARTY_LABELS[ordering[0]]
        classic_stv_top_two_ratio = calculate_top_two_ratio(ordering, wasted_votes)
        classic_stv_total_ratio = calculate_total_ratio(ordering, wasted_votes)

        # Complete STV
        ordering, wasted_votes = complete_single_transferrable_vote(electorate)
        complete_stv_winner = PARTY_LABELS[ordering[0]]
        complete_stv_top_two_ratio = calculate_top_two_ratio(ordering, wasted_votes)
        complete_stv_total_ratio = calculate_total_ratio(ordering, wasted_votes)

        out_writer.writerow([honest_fptp_winner,
            honest_fptp_top_two_ratio,
            honest_fptp_total_ratio,
            strategic_fptp_winner,
            strategic_fptp_top_two_ratio,
            strategic_fptp_total_ratio,
            approval_winner,
            approval_top_two_ratio,
            approval_total_ratio,
            borda_winner,
            borda_top_two_ratio,
            borda_total_ratio,
            classic_stv_winner,
            classic_stv_top_two_ratio,
            classic_stv_total_ratio,
            complete_stv_winner,
            complete_stv_top_two_ratio,
            complete_stv_total_ratio])

if __name__ == "__main__":
    run_experiment("basic_results.csv", BASIC_ORDER_PROBS)
    run_experiment("maine_results.csv", MAINE_PROBS)


