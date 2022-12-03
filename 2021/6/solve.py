raw = [int(line) for line in open("resources/input.txt").readline().split(',')]

days = 256

# 0 days, 1 days, 2 days
fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for f in raw:
  fish[f] = fish[f] + 1  
  
def simulate(days):
  for d in range(days):
    births = fish[0]
    for i in range(1, len(fish)):
      fish[i - 1] = fish[i]
    fish[6] = fish[6] + births
    fish[8] = births



print(f"In {d+1} days there will be {sum(fish)} fish")
