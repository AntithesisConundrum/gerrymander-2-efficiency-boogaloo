"""
Standardizes Maine voting records into something we can use.
Takes each vote that orders the four official candidates,
    * coding Hoar as a Libertarian
    * coding Bond as a Green 
and prints a standardized probability map.

Data taken from the FINAL files posted here:
https://www.maine.gov/sos/cec/elec/results/results18.html#Nov6
"""

from collections import defaultdict
from csv import reader
from constants import *

results = defaultdict(int)
# Hoar and Bond were coded semi-arbitrarily.
candidates_to_parties = {
    "Poliquin, Bruce": REPUBLICAN,
    "Golden, Jared": DEMOCRAT,
    "Hoar, William": LIBERTARIAN,
    "Bond, Tiffany": GREEN
}
candidates = candidates_to_parties.keys()


for file_no in xrange(1,9):
    votes = open(str(file_no)+".csv", "r")
    votes.readline()
    voters = reader(votes)

    for voter in voters:
        standardized_voter = []
        matched_parties = set() # Only accept a complete ranking of the four main candidates
        for choice in xrange(4):
            index = 1+choice
            chosen_candidate = voter[index]
            matching_candidates = 0
            matching_party = None
            for candidate in candidates:
                if candidate in chosen_candidate:
                    matching_candidates += 1
                    matching_party = candidates_to_parties[candidate]

            if matching_candidates == 1:
                standardized_voter.append(matching_party)
                matched_parties.add(matching_party)
        if len(matched_parties) == 4:
            results[tuple(standardized_voter)] += 1


d = freq_to_prob(results)
print "{"
for key in sorted(d.keys(), key=lambda x: 1000*x[0]+100*x[1]+10*x[2]+x[3]):
    ord_str = ""

    print "\t("+", ".join(order_to_cap_names(key))+"): "+str(d[key])+","
print "}"