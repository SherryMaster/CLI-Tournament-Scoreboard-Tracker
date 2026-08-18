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
    print("5) Show Statistics")
    print("6) exit")
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

def show_leaderboard():
    order = sorted(
        range(len(scores)),
        key=lambda i: scores[i],
        reverse=True
    )

    sorted_scores = [scores[i] for i in order]
    sorted_players = [players[i] for i in order]

    print("Rank\tName\t\tScore")
    print("=======================================")
    for i, player in enumerate(sorted_players):
        print(f"{i+1}\t{player}\t\t{sorted_scores[i]}")
    print("\n")

def record_points():
    print("Record points for a player!")
    show_scoreboard()
    while True:
        try:
            index = int(input("Enter the index of the player: ")) - 1
            if not 0 <= index < len(players):
                print("Invalid player index!")
                continue
            print(f"player {players[index]} selected!")
            points = int(input("Enter the points to add: "))
            break
        except ValueError:
            print("Invalid input, try again!")
    
    scores[index] += points
    save_data()
    print(f"Added {points} points to {players[index]}!")

def show_statistics():
    print("Statistics:")
    print(f"Total Players: {len(players)}")
    print(f"Total Points: {sum(scores)}")
    print(f"Average Points per Player: {sum(scores)/len(players) if players else 0}")
    print(f"Highest Score: {max(scores) if scores else 0}")
    print(f"Lowest Score: {min(scores) if scores else 0}")
    print("\n")

program_running = True

if __name__ == "__main__":
    load_data()
    print("Welcome to Tournament Scoreboard Tracker")


    while program_running:
        display_main_menu()
        while True:
            try:
                choice = int(input("Enter a choice: "))
                break
            except:
                print("Invalid Input, try again!")

        if choice == 1:
            add_player()
        elif choice == 2:
            record_points()
        elif choice == 3:
            show_scoreboard()
        elif choice == 4:
            show_leaderboard()
        elif choice == 5:
            show_statistics()
        elif choice == 6:
            program_running = False


    save_data()
    print("Program Ended, All data is saved!")