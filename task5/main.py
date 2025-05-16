import csv
from collections import defaultdict


def misra_gries(filepath, filelen, threshold):
    k = int(filelen // threshold)
    counters = {}

    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            key = row[0]
            if key in counters:
                counters[key] += 1
            elif len(counters) < k:
                counters[key] = 1
            else:
                remove_keys = []
                for candidate in counters:
                    counters[candidate] -= 1
                    if counters[candidate] == 0:
                        remove_keys.append(candidate)
                for candidate in remove_keys:
                    del counters[candidate]
    
    return set(counters.keys())

def count_exact(filepath, candidates):
    counts = defaultdict(int)
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            key = row[0]
            if key in candidates:
                counts[key] += 1
    return counts

def find_heavy_hitters(file1, file2, filelen, threshold):
    candidates = misra_gries(file1, filelen, threshold)
    
    counts2 = count_exact(file2, candidates)
    filtered = {key for key in candidates if counts2[key] >= threshold}
    
    if not filtered:
        return []

    counts1 = count_exact(file1, filtered)
    heavy = [key for key in filtered if counts1[key] >= threshold]
    return heavy
