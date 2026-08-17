from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data"
DATA_PATH.mkdir(exist_ok=True, parents=True)

PLAYERS_PATH = DATA_PATH / "players.txt"
SCORES_PATH = DATA_PATH / "scores.txt"

players = []
scores = []

def load_data():
    global players, scores
    PLAYERS_PATH.touch(exist_ok=True)
    SCORES_PATH.touch(exist_ok=True)
    with open(PLAYERS_PATH) as f1:
        with open(SCORES_PATH) as f2:
            players = [player.replace("\n", "") for player in f1.readlines()]
            scores = [int(score.replace("\n", "")) for score in f2.readlines()]

def save_data():
    with open(PLAYERS_PATH, "w") as f:
        f.writelines([player + "\n" for player in players])
    with open(SCORES_PATH, "w") as f:
        f.writelines([str(score) + "\n" for score in scores])

def display_main_menu():
    print("1) Add Player")
    print("2) Record Points")
    print("3) Show Scoreboard")
    print("4) Show Leaderboard")
    print("5) exit")
    print()

def add_player():
    print("Add a player!")
    name = input("Enter Player name: ")
    
    players.append(name)
    scores.append(0)
    save_data()
    print(f"Player {name} added successfully!")

def show_scoreboard():
    print("Index\tName\t\tScore")
    print("=======================================")
    for i, player in enumerate(players):
        print(f"{i+1}\t{player}\t\t{scores[i]}")
    print("\n")

program_running = True

if __name__ == "__main__":
    load_data()
    print("Welcome to Tournament Scoreboard Tracker")


    while program_running:
        display_main_menu()

        choice = int(input("Enter a choice: "))

        if choice == 1:
            add_player()
        elif choice == 3:
            show_scoreboard()
        elif choice == 5:
            program_running = False


    save_data()
    print("Program Ended, All data is saved!")