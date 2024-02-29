from itertools import product

def calculate_probability(target, die, number):
    die_outcomes = range(1,die + 1,1)
    all_combinations = list(product(die_outcomes, repeat=number))
    favorable_outcomes = [pair for pair in all_combinations if sum(pair) >= target]
    probability = len(favorable_outcomes) / len(all_combinations)
    print("All the results that succeed:")
    print(favorable_outcomes)
    return probability

print("Enter die size")
die = int(input())
print("Enter die number")
number = int(input())
print("Enter target outcome")
target = int(input())
result = round(calculate_probability(target, die, number) * 100)

print(f"The probability of getting {target} or greater on a {number}d{die} roll is: {result} %")



















