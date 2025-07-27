import random

numrolls = int(input('how many gambas do you want?'))

char = ['Wylder', 'Raider', 'Guardian', 'Duchess', 'Executor', 'Ironeye', 'Revenant', 'Recluse']

chars = random.sample(char, numrolls)

print(f"{chars}")
