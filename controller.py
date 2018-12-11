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
from random import shuffle
from collections import defaultdict

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

def calculate_efficiency_gap(wasted_votes, num_voters):
    """
    Calculate EG given wasted votes.
    Assumes DEMOCRAT won.
    """
    winner = wasted_votes[DEMOCRAT]
    loser = wasted_votes[REPUBLICAN] + wasted_votes[LIBERTARIAN] + wasted_votes[GREEN]
    return (winner-loser)/float(num_voters)

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

def run_full_experiment(out_name, distribution):
    out_file = open(out_name, 'wb')
    out_writer = csv.writer(out_file)

    out_writer.writerow([
        "Strategic_FPTP_Efficiency_Gap",
        "Honest_FPTP_Efficiency_Gap",
        "Approval_Efficiency_Gap",
        "Borda_Efficiency_Gap",
        "Classic_STV_Efficiency_Gap",
        "Complete_STV_Efficiency_Gap",
        "Wasted_Ballot_Efficiency_Gap",
        ])

    num_trials = 1000
    num_districts = 10
    voters_per_district = 1000
    num_voters = num_districts * voters_per_district

    # Get num_trials electorates
    for _ in xrange(num_trials):
        electorate = generate_voters(num_voters, distribution)

        # Map each voting system to a mapping from party to WV
        sys_party_wv = defaultdict(lambda: defaultdict(int))

        # Keep track of number of districts won by winning_party
        districts_won = 0

        # For each district, calculate wasted vote
        for district_no in xrange(num_districts):
            # Find district electorate
            district_electorate = electorate[district_no*voters_per_district:(district_no+1)*voters_per_district]

            systems = [
                (strategic_fptp, "Strategic_FPTP"),
                (honest_fptp, "Honest_FPTP"),
                (approval_voting, "Approval"),
                (borda_count_vote, "Borda"),
                (classic_single_transferrable_vote, "Classic_STV"),
                (complete_single_transferrable_vote, "Complete_STV")
            ]

            for method, name in systems:
                ordering, wasted_votes = method(district_electorate)
                for party in ordering:
                    sys_party_wv[name][party] += wasted_votes[party]

        # For each district plan, calculate efficiency gap
        out_writer.writerow([calculate_efficiency_gap(sys_party_wv["Honest_FPTP"], num_voters),
            calculate_efficiency_gap(sys_party_wv["Strategic_FPTP"], num_voters),
            calculate_efficiency_gap(sys_party_wv["Approval"], num_voters*2),
            calculate_efficiency_gap(sys_party_wv["Borda"], num_voters*(3+2+1)),
            calculate_efficiency_gap(sys_party_wv["Classic_STV"], num_voters),
            calculate_efficiency_gap(sys_party_wv["Complete_STV"], num_voters),
            calculate_wasted_ballot_efficiency_gap(DEMOCRAT, electorate),
        ])

if __name__ == "__main__":
    #run_experiment("basic_results.csv", BASIC_ORDER_PROBS)
    #run_experiment("maine_results.csv", MAINE_PROBS)
    run_full_experiment("maine_full_results.csv", MAINE_PROBS)

