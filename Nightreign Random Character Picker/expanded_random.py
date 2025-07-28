import random

numrolls = input("How many players do you want? (1 or more): ")
if not numrolls.isdigit() or int(numrolls) < 1:
    raise ValueError("Please enter a valid number of players (1 to 3).")
if int(numrolls) > 1:
    allow_dupes = input("Allow duplicates? (yes or no): ").strip().lower()
    raise ValueError("Please enter 'yes' or 'no'.") if allow_dupes not in ["yes", "no"] else None
else:
    allow_dupes = "no"

def main(numrolls, allow_dupes):
    numrolls = int(numrolls)

    char = ['Wylder', 'Raider', 'Guardian', 'Duchess', 'Executor', 'Ironeye', 'Revenant', 'Recluse']
    if numrolls > 1:  
        if allow_dupes == "yes":
            characters = random.choices(char, k=numrolls)
            characters = " and ".join(characters)
        
        elif allow_dupes == "no":
            characters = random.sample(char, numrolls)
            characters = " and ".join(characters)

        if allow_dupes == "yes":
            allow_dupes = "duplicates allowed"
        else:
            allow_dupes = "no duplicates allowed"
        print(f"For {numrolls} players with {allow_dupes} you have been given {characters} to play for this expedition. GL, HF!")
        return characters

    else:
        characters = random.choice(char)
        characters = f"{characters}"
        print(f"For {numrolls} player you have been given {characters} to play for this expedition. GL, HF!")
        
    return characters

if __name__ == "__main__":
    main(numrolls, allow_dupes)