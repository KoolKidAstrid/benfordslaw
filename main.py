import random
import matplotlib.pyplot as plt

limit = 1000000
sample = 1000000
output = [0, 0, 0, 0, 0, 0, 0, 0, 0]
output2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
count = 0
while count < sample:
    count += 1
    num = random.randint(0,limit)
    num2 = random.randint(0, limit) * random.randint(0, limit) * random.randint(0, limit) * random.randint(0, limit)
    while num >= 10:
        num = num // 10
    while num2 >= 10:
        num2 = num2 // 10

    output[num - 1] += 1
    output2[num2 - 1] += 1

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
pos1 = []
pos2 = []
for p in positions:
    pos1.append(p + 0.2)
    pos2.append(p - 0.2)

plt.bar(
    pos1,
    output,
    width=0.4,
    color=["lightskyblue"],
    edgecolor=["black"],
    label="Random Number 1 - " + str(limit)
)

plt.bar(
    pos2,
    output2,
    width=0.4,
    color=["lightcoral"],
    edgecolor=["black"],
    label="Four Random Numbers 1 - " + str(limit) + " Multiplied Together"
)


plt.ylim(0, sample/2)
plt.grid(axis="y")
count = 0
grid = []
plt.title("Comparing " + str(sample) + " Random Numbers and an Equal Number of Numbers Derived from Random Numbers")
while count < 10:
    count += 1
    grid.append(count*sample/20)
plt.legend()
plt.yticks(grid)
plt.gca().set_yticklabels(['{:.0f}%'.format(x/(sample/100)) for x in plt.gca().get_yticks()])
plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9])
plt.show()