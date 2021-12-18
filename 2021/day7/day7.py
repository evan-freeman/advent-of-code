from collections import Counter

file = "2021/day7/input.txt"
with open(file) as f:
    input = f.read()
# input = "16,1,2,0,4,2,7,1,2,14"
input = [int(x) for x in input.split(",")]

counts = Counter(input)
costs = []


def cost_formula1(position, destination):
    return abs(position - destination)


def cost_formula2(position, destination):
    n = abs(position - destination)
    return (n * (n + 1)) // 2


for destination in range(max(counts) + 1):
    cost = sum(
        [
            cost_formula2(position, destination) * count
            for position, count in counts.items()
        ]
    )
    costs.append(cost)
print(min(costs))
