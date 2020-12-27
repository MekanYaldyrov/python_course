
import statistics as stat
import math
main = []

# Input
inp = int(input())
while inp != "End":
    main.append(int(inp))
    inp = input()

# Main program
mx = max(main)
mn = min(main)
avg = stat.mean(main) # функция mean из библиотеки stat
stdev = stat.pstdev(main)

print("Max: ", mx, "\n", "Min: ", mn, "\n", "Avg: ", avg, "\n", "StDev: ", stdev)

import statistics as stat
import math
main = []

# Input
inp = int(input())
while inp != "End":
    main.append(int(inp))
    inp = input()

# Main program
mx = max(main)
mn = min(main)
avg = stat.mean(main) # функция mean из библиотеки stat
stdev = stat.pstdev(main)

print("Max: ", mx, "\n", "Min: ", mn, "\n", "Avg: ", avg, "\n", "StDev: ", stdev)
