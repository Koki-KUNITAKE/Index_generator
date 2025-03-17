import random

def generate_random_sequence(length):
    return ''.join(random.choice('ACGT') for _ in range(length))

def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return gc / len(seq) * 100

def has_homotrimer(seq):
    return any(seq[i] == seq[i+1] == seq[i+2] for i in range(len(seq) - 2))

def hamming_distance(seq1, seq2):
    return sum(c1 != c2 for c1, c2 in zip(seq1, seq2))

def generate_dna_sequences(n, m, min_hamming=4, max_gc = 70, max_trials=100000):
    sequences = []
    trials = 0

    while len(sequences) < n and trials < max_trials:
        candidate = generate_random_sequence(m)
        if any([has_homotrimer(candidate), gc_content(candidate) > max_gc, candidate[:2] == 'GG']):
            trials += 1
            continue
        if all(hamming_distance(candidate, existing) >= min_hamming for existing in sequences):
            sequences.append(candidate)
        trials += 1

    if len(sequences) < n:
        print(f"⚠ Could only generate {len(sequences)} sequences after {trials} trials.")

    # check if each position [0 – m-1] has at least one C or T across all sequences
    ct_coverage = []
    for pos in range(m):
        ct_isin = any(l in [i[pos] for i in sequences] for l in ['C', 'T'])
        ct_coverage.append(ct_isin)
    while not all(ct_coverage):
        generate_dna_sequences(n, m, min_hamming=4, max_trials=100000)
        
    return sequences

# Example usage
n = 20  # number of sequences
m = 8   # length of each sequence
min_hamming = 4
max_gc = 70

sequences = generate_dna_sequences(n, m, min_hamming = min_hamming, max_gc = max_gc)

for i, seq in enumerate(sequences):
    print(f"Seq{i+1}: {seq}")
