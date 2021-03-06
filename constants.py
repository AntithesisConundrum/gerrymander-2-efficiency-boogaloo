from random import choice, random
DEMOCRAT = 0
REPUBLICAN = 1
LIBERTARIAN = 2
GREEN = 3
NUM_PARTIES = 4

PARTY_CAP_NAMES = ["DEMOCRAT", "REPUBLICAN", "LIBERTARIAN", "GREEN"]
PARTY_NAMES = ["Democrat", "Republican", "Libertarian", "Green"]
PARTY_LABELS = ["D", "R", "L", "G"]

ALL_PERMUTATIONS = [
    (DEMOCRAT, REPUBLICAN, LIBERTARIAN, GREEN),
    (DEMOCRAT, REPUBLICAN, GREEN, LIBERTARIAN),
    (DEMOCRAT, LIBERTARIAN, REPUBLICAN, GREEN),
    (DEMOCRAT, LIBERTARIAN, GREEN, REPUBLICAN),
    (DEMOCRAT, GREEN, REPUBLICAN, LIBERTARIAN),
    (DEMOCRAT, GREEN, LIBERTARIAN, REPUBLICAN),
    (REPUBLICAN, DEMOCRAT, LIBERTARIAN, GREEN),
    (REPUBLICAN, DEMOCRAT, GREEN, LIBERTARIAN),
    (REPUBLICAN, LIBERTARIAN, DEMOCRAT, GREEN),
    (REPUBLICAN, LIBERTARIAN, GREEN, DEMOCRAT),
    (REPUBLICAN, GREEN, DEMOCRAT, LIBERTARIAN),
    (REPUBLICAN, GREEN, LIBERTARIAN, DEMOCRAT),
    (LIBERTARIAN, DEMOCRAT, REPUBLICAN, GREEN),
    (LIBERTARIAN, DEMOCRAT, GREEN, REPUBLICAN),
    (LIBERTARIAN, REPUBLICAN, DEMOCRAT, GREEN),
    (LIBERTARIAN, REPUBLICAN, GREEN, DEMOCRAT),
    (LIBERTARIAN, GREEN, DEMOCRAT, REPUBLICAN),
    (LIBERTARIAN, GREEN, REPUBLICAN, DEMOCRAT),
    (GREEN, DEMOCRAT, REPUBLICAN, LIBERTARIAN),
    (GREEN, DEMOCRAT, LIBERTARIAN, REPUBLICAN),
    (GREEN, REPUBLICAN, DEMOCRAT, LIBERTARIAN),
    (GREEN, REPUBLICAN, LIBERTARIAN, DEMOCRAT),
    (GREEN, LIBERTARIAN, DEMOCRAT, REPUBLICAN),
    (GREEN, LIBERTARIAN, REPUBLICAN, DEMOCRAT),
]

# This tries to create a reasonable distribution:
# 50/50 split between people who choose D before R and vice versa; 
# 40/40/10/10 between D/R/L/G first choices;
BASIC_ORDER_FREQS = {
    (DEMOCRAT, REPUBLICAN, LIBERTARIAN, GREEN): 0,
    (DEMOCRAT, REPUBLICAN, GREEN, LIBERTARIAN): 100,
    (DEMOCRAT, LIBERTARIAN, REPUBLICAN, GREEN): 0,
    (DEMOCRAT, LIBERTARIAN, GREEN, REPUBLICAN): 0,
    (DEMOCRAT, GREEN, REPUBLICAN, LIBERTARIAN): 100,
    (DEMOCRAT, GREEN, LIBERTARIAN, REPUBLICAN): 200,
    (REPUBLICAN, DEMOCRAT, LIBERTARIAN, GREEN): 100,
    (REPUBLICAN, DEMOCRAT, GREEN, LIBERTARIAN): 0,
    (REPUBLICAN, LIBERTARIAN, DEMOCRAT, GREEN): 100,
    (REPUBLICAN, LIBERTARIAN, GREEN, DEMOCRAT): 200,
    (REPUBLICAN, GREEN, DEMOCRAT, LIBERTARIAN): 0,
    (REPUBLICAN, GREEN, LIBERTARIAN, DEMOCRAT): 0,
    (LIBERTARIAN, DEMOCRAT, REPUBLICAN, GREEN): 0,
    (LIBERTARIAN, DEMOCRAT, GREEN, REPUBLICAN): 0,
    (LIBERTARIAN, REPUBLICAN, DEMOCRAT, GREEN): 30,
    (LIBERTARIAN, REPUBLICAN, GREEN, DEMOCRAT): 30,
    (LIBERTARIAN, GREEN, DEMOCRAT, REPUBLICAN): 0,
    (LIBERTARIAN, GREEN, REPUBLICAN, DEMOCRAT): 40,
    (GREEN, DEMOCRAT, REPUBLICAN, LIBERTARIAN): 30,
    (GREEN, DEMOCRAT, LIBERTARIAN, REPUBLICAN): 30,
    (GREEN, REPUBLICAN, DEMOCRAT, LIBERTARIAN): 0,
    (GREEN, REPUBLICAN, LIBERTARIAN, DEMOCRAT): 0,
    (GREEN, LIBERTARIAN, DEMOCRAT, REPUBLICAN): 40,
    (GREEN, LIBERTARIAN, REPUBLICAN, DEMOCRAT): 0,
}

BASIC_ORDER_PROBS = {
    (DEMOCRAT, REPUBLICAN, GREEN, LIBERTARIAN): 0.1,
    (DEMOCRAT, LIBERTARIAN, REPUBLICAN, GREEN): 0.0,
    (DEMOCRAT, LIBERTARIAN, GREEN, REPUBLICAN): 0.0,
    (DEMOCRAT, GREEN, REPUBLICAN, LIBERTARIAN): 0.1,
    (DEMOCRAT, GREEN, LIBERTARIAN, REPUBLICAN): 0.2,
    (DEMOCRAT, REPUBLICAN, LIBERTARIAN, GREEN): 0.0,
    (REPUBLICAN, DEMOCRAT, GREEN, LIBERTARIAN): 0.0,
    (REPUBLICAN, DEMOCRAT, LIBERTARIAN, GREEN): 0.1,
    (REPUBLICAN, GREEN, LIBERTARIAN, DEMOCRAT): 0.0,
    (REPUBLICAN, LIBERTARIAN, GREEN, DEMOCRAT): 0.2,
    (REPUBLICAN, GREEN, DEMOCRAT, LIBERTARIAN): 0.0,
    (REPUBLICAN, LIBERTARIAN, DEMOCRAT, GREEN): 0.1,
    (LIBERTARIAN, DEMOCRAT, REPUBLICAN, GREEN): 0.0,
    (LIBERTARIAN, GREEN, DEMOCRAT, REPUBLICAN): 0.0,
    (LIBERTARIAN, REPUBLICAN, DEMOCRAT, GREEN): 0.03,
    (LIBERTARIAN, GREEN, REPUBLICAN, DEMOCRAT): 0.04,
    (LIBERTARIAN, DEMOCRAT, GREEN, REPUBLICAN): 0.0,
    (LIBERTARIAN, REPUBLICAN, GREEN, DEMOCRAT): 0.03,
    (GREEN, DEMOCRAT, REPUBLICAN, LIBERTARIAN): 0.03,
    (GREEN, LIBERTARIAN, REPUBLICAN, DEMOCRAT): 0.0,
    (GREEN, DEMOCRAT, LIBERTARIAN, REPUBLICAN): 0.03,
    (GREEN, REPUBLICAN, LIBERTARIAN, DEMOCRAT): 0.0,
    (GREEN, REPUBLICAN, DEMOCRAT, LIBERTARIAN): 0.0,
    (GREEN, LIBERTARIAN, DEMOCRAT, REPUBLICAN): 0.04,
}


MAINE_PROBS = {
    (REPUBLICAN, DEMOCRAT, GREEN, LIBERTARIAN): 0.0508711012722,
    (GREEN, DEMOCRAT, LIBERTARIAN, REPUBLICAN): 0.0283088959985,
    (GREEN, REPUBLICAN, LIBERTARIAN, DEMOCRAT): 0.00826371093691,
    (REPUBLICAN, LIBERTARIAN, GREEN, DEMOCRAT): 0.142787827326,
    (LIBERTARIAN, DEMOCRAT, REPUBLICAN, GREEN): 0.00181953268336,
    (GREEN, DEMOCRAT, REPUBLICAN, LIBERTARIAN): 0.00592864399327,
    (DEMOCRAT, REPUBLICAN, GREEN, LIBERTARIAN): 0.0407423693348,
    (DEMOCRAT, LIBERTARIAN, REPUBLICAN, GREEN): 0.00965868599415,
    (GREEN, LIBERTARIAN, REPUBLICAN, DEMOCRAT): 0.0153447256296,
    (REPUBLICAN, DEMOCRAT, LIBERTARIAN, GREEN): 0.0322663795848,
    (REPUBLICAN, GREEN, LIBERTARIAN, DEMOCRAT): 0.102955224333,
    (DEMOCRAT, GREEN, LIBERTARIAN, REPUBLICAN): 0.291473973101,
    (GREEN, REPUBLICAN, DEMOCRAT, LIBERTARIAN): 0.00501887765159,
    (DEMOCRAT, REPUBLICAN, LIBERTARIAN, GREEN): 0.0256099225182,
    (LIBERTARIAN, DEMOCRAT, GREEN, REPUBLICAN): 0.00656548043244,
    (GREEN, LIBERTARIAN, DEMOCRAT, REPUBLICAN): 0.0307955906658,
    (DEMOCRAT, LIBERTARIAN, GREEN, REPUBLICAN): 0.102894573244,
    (DEMOCRAT, GREEN, REPUBLICAN, LIBERTARIAN): 0.0185743961426,
    (REPUBLICAN, GREEN, DEMOCRAT, LIBERTARIAN): 0.0247001561766,
    (LIBERTARIAN, GREEN, DEMOCRAT, REPUBLICAN): 0.0141771921578,
    (REPUBLICAN, LIBERTARIAN, DEMOCRAT, GREEN): 0.0267168049006,
    (LIBERTARIAN, REPUBLICAN, DEMOCRAT, GREEN): 0.0028202756592,
    (LIBERTARIAN, GREEN, REPUBLICAN, DEMOCRAT): 0.00742975845704,
    (LIBERTARIAN, REPUBLICAN, GREEN, DEMOCRAT): 0.00427590180589,
}

def freq_to_prob(d):
    """Takes a dict from order to freqs, returns a dict of order to probs"""
    n = float(sum(d.values()))
    return {k: d[k]/n for k in d.keys()}

def order_to_cap_names(order):
    return tuple([PARTY_CAP_NAMES[p] for p in order])

def order_to_names(order):
    return tuple([PARTY_NAMES[p] for p in order])

def order_to_labels(order):
    return tuple([PARTY_LABELS[p] for p in order])

def weighted_random_choice(d):
    """Takes a dict from order to probs, return order under weights"""
    total = 0
    rand = random()
    for order in d:
        total += d[order]
        # Strictly <; if prob is 0, we want 0 chance.
        if rand < total:
            return order
    # Should never reach this, but just in case...
    print "weighted_random_choice fall through"
    return choice(d.keys())
