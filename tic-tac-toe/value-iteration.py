# set of States
S = {"Olympus", "Delphi", "Dodoni", "Delos"}
# set of Actions
A = {"Fly", "Walk", "Horse"}
# (s_next, s, a): probability
P = {
    # Olympus
    ("Olympus", "Olympus", "Fly"): 0.1,
    ("Delphi", "Olympus", "Fly"): 0.9,
    ("Delphi", "Olympus", "Walk"): 0.2,
    ("Dodoni", "Olympus", "Walk"): 0.8,

    ("Delphi", "Olympus", "Horse"): 0,
    ("Delos", "Olympus", "Horse"): 0,
    ("Dodoni", "Olympus", "Horse"): 0,
    ('Delos', 'Olympus', 'Fly'): 0,
    ('Olympus', 'Olympus', 'Horse'): 0,
    ('Dodoni', 'Olympus', 'Fly'): 0,
    ('Olympus', 'Olympus', 'Walk'): 0,
    ('Delos', 'Olympus', 'Walk'): 0,

    # Delphi
    ("Delphi", "Delphi", "Fly"): 0.3,
    ("Delos", "Delphi", "Fly"): 0.7,
    ("Olympus", "Delphi", "Horse"): 0.8,
    ("Dodoni", "Delphi", "Horse"): 0.2,

    ("Dodoni", "Delphi", "Fly"): 0,
    ('Olympus', 'Delphi', 'Fly'): 0,
    ('Delphi', 'Delphi', 'Walk'): 0,
    ('Delphi', 'Delphi', 'Horse'): 0,
    ('Dodoni', 'Delphi', 'Walk'): 0,
    ('Olympus', 'Delphi', 'Walk'): 0,
    ('Delos', 'Delphi', 'Horse'): 0,
    ('Delos', 'Delphi', 'Walk'): 0,

    # Dodoni
    ("Dodoni", "Dodoni", "Fly"): 0.3,
    ("Olympus", "Dodoni", "Fly"): 0.7,
    ("Delphi", "Dodoni", "Horse"): 0.3,
    ("Olympus", "Dodoni", "Horse"): 0.7,

    ("Delphi", "Dodoni", "Fly"): 0,
    ("Delos", "Dodoni", "Fly"): 0,
    ("Dodoni", "Dodoni", "Horse"): 0,
    ("Delos", "Dodoni", "Horse"): 0,
    ("Dodoni", "Dodoni", "Walk"): 0,
    ('Delphi', 'Dodoni', 'Walk'): 0,
    ('Olympus', 'Dodoni', 'Walk'): 0,
    ('Delos', 'Dodoni', 'Walk'): 0,

    # Delos
    ("Delos", "Delos", "Fly"): 0.2,
    ("Delphi", "Delos", "Fly"): 0.4,
    ("Dodoni", "Delos", "Fly"): 0.4,

    ('Olympus', 'Delos', 'Fly'): 0,
    ('Delos', 'Delos', 'Walk'): 0,
    ('Olympus', 'Delos', 'Horse'): 0,
    ('Dodoni', 'Delos', 'Horse'): 0,
    ('Delphi', 'Delos', 'Walk'): 0,
    ('Delos', 'Delos', 'Horse'): 0,
    ('Olympus', 'Delos', 'Walk'): 0,
    ('Delphi', 'Delos', 'Horse'): 0,
    ('Dodoni', 'Delos', 'Walk'): 0
}  # transition function
# (s, a): reward
R = {
    # Olympus
    ("Olympus", "Fly"): 1.7,
    ("Olympus", "Walk"): 1.2,
    ("Olympus", "Horse"): 0,

    # Delphi
    ("Delphi", "Fly"): 3.2,
    ("Delphi", "Horse"): 1,
    ("Delphi", "Walk"): 0,

    # Dodoni
    ("Dodoni", "Fly"): 1.1,
    ("Dodoni", "Horse"): 0.3,
    ("Dodoni", "Walk"): 0,

    # Delos
    ("Delos", "Fly"): -1,
    ("Delos", "Walk"): 0,
    ("Delos", "Horse"): 0,
}  # reward function

gamma = 0.9  # discount factor
delta = 0.0  # Error tolerance
V = {s: 0 for s in S}  # Initialize values

for i in range(100000):
    max_diff = 0  # Initialize max difference
    V_new = V.copy()  # Initialize values
    for s in S:
        max_v = 0
        for a in A:
            v = R[(s, a)]
            for s_next in S:
                v += P[(s_next, s, a)] * (
                    gamma * V[s_next]
                )
            max_v = max(max_v, v)
        V_new[s] = max_v

        max_diff = max(max_diff, abs(V[s] - V_new[s]))
    V = V_new

    if max_diff < delta:
        break
# this outputs: {'Olympus': 14.038285510096328, 'Delos': 10.763537261134609, 'Delphi': 13.67264174591069, 'Dodoni': 13.622082015562583}
print(V)
