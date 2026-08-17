import os
from pathlib import Path

DATA_PATH = Path("data")
DATA_PATH.mkdir(exist_ok=True, parents=True)

PLAYERS_PATH = DATA_PATH / "players.txt"
SCORES_PATH = DATA_PATH / "scores.txt"

players = []

def load_data():
    pass

def save_data():
    pass

def display_main_menu():
    print("1) Add Player")
    print("2) Record Points")
    print("3) Show Scoreboard")
    print("4) Show Leaderboard")
    print("5) exit")
    print()

program_running = True

if __name__ == "__main__":
    load_data()
    print("Welcome to Tournament Scoreboard Tracker")


    while program_running:
        display_main_menu()

        choice = int(input("Enter a choice: "))

        if choice == 5:
            program_running = False


    save_data()
    print("Program Ended, All data is saved!")