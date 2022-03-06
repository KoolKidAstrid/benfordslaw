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
    num2 = num*random.randint(0, limit)*random.randint(0, limit)*random.randint(0, limit)*random.randint(0, limit)

    while num >= 10:
        num = num // 10
    while num2 >= 10:
        num2 = num2 // 10
    output2[num2 - 1] += 1
    output[num - 1] += 1

plt.bar([0.8, 1.8, 2.8, 3.8, 4.8, 5.8, 6.8, 7.8, 8.8], output2, width=0.4, color=["lightcoral"], edgecolor=["black"], label="Four Random Numbers 1 - " + str(limit) + " Multiplied Together")
plt.bar([1.2, 2.2, 3.2, 4.2, 5.2, 6.2, 7.2, 8.2, 9.2], output, width=0.4, color=["lightskyblue"], edgecolor=["black"], label="Random Number 1 - " + str(limit))
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