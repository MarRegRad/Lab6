def generate_combinations(word):
    n = len(word)
    combinations = []
    for i in range(1, n+1):
        for j in range(n-i+1):
            combination = ''
            for k in range(j, j+i):
                combination += word[k]
            combinations.append(combination)
    return combinations

word = 'абракадабра'

combinations = set(generate_combinations(word))
print(sorted(combinations))