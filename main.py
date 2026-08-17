from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data"
DATA_PATH.mkdir(exist_ok=True, parents=True)

PLAYERS_PATH = DATA_PATH / "players.txt"
SCORES_PATH = DATA_PATH / "scores.txt"

players = []

def load_data():
    global players
    PLAYERS_PATH.touch(exist_ok=True)
    SCORES_PATH.touch(exist_ok=True)
    with open(PLAYERS_PATH) as f:
        players = [player.replace("\n", "") for player in f.readlines()]

def save_data():
    with open(PLAYERS_PATH, "w") as f:
        f.writelines([player + "\n" for player in players])

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
    save_data()
    print(f"Player {name} added successfully!")

def show_scoreboard():
    for player in players:
        print(player)

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