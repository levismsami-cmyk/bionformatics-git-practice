sequence = "ATGCGTACGATCGATCGCGTA"

gc_count = sequence.count("G") + sequence.count("C")
gc_percentage = (gc_count / len(sequence)) * 100

print("DNA sequence:", sequence)
print("GC percentage:", round(gc_percentage, 2), "%")
