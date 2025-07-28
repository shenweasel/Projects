import random

numrolls = ""

while numrolls != int or numrolls <= 1:
    numrolls = int(input('How many players want to gamba their choice? Please enter a number from 1 to 3: '))  
    if numrolls >= 1 and numrolls < 4:
        break 
    
char = ['Wylder', 'Raider', 'Guardian', 'Duchess', 'Executor', 'Ironeye', 'Revenant', 'Recluse']

characters = random.sample(char, numrolls)
characters = " and ".join(characters)

print(f"{characters}")
import random