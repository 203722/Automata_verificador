from automata.fa.dfa import DFA

# DFA which matches all binary strings ending in an odd number of '1's
dfa = DFA(
    allow_partial=True,
    states={'q0', 'q1', 'q2','q3'},
    input_symbols={'∅','0', '1'},
    transitions={
        'q0': {'1': 'q2', '1': 'q2'},
        'q1': {'1': 'q1'},
        'q2': {'0': 'q3'},
        'q3': {'0': 'q3'}
    },
    initial_state='q0',
    final_states={'q3'}
)
if dfa.accepts_input('11'):
    print('accepted')
else:
    print('rejected')