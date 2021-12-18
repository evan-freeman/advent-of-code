file = "2021/day6/input.txt"
with open(file) as f:
    input = f.read()
# input = "3,4,3,1,2"
input = [int(x) for x in input.split(",")]


("3,4,3,1,2", 18, 26)


current_fish = [input.count(x) for x in range(9)]
print(current_fish)
num_days = 256
for i in range(num_days):
    new_fish = current_fish[0]
    next_fish = current_fish[1:] + current_fish[:1]
    next_fish[6] += new_fish
    current_fish = next_fish

print(current_fish)
print(sum(current_fish))
