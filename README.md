# Tournament Scoreboard Tracker

Simple tracker for tournament players and scores.

## Overview

This project is an interactive tournament scoreboard tracker. It lets you add players, record points, view a scoreboard or leaderboard, and inspect basic statistics from two local text files.

## Features

- Add players interactively
- Record points for an existing player
- Show a scoreboard in the current player order
- Show a leaderboard sorted by highest score first
- Show basic statistics such as total players and total points

## Requirements

- Python 3.8+

## Run

From the project root, run:

```
python main.py
```

## Usage

- Run the program from the project root with `python main.py`.
- The program creates `data/players.txt` and `data/scores.txt` automatically if they do not exist.
- Player names are stored one per line in `data/players.txt`.
- Scores are stored one integer per line in `data/scores.txt`.
- The two files are positional: the first player matches the first score, the second player matches the second score, and so on.

Example `players.txt`:

```
Alice
Bob
Charlie
```

Example `scores.txt`:

```
12
9
15
```

Notes:

- Adding a player starts them at `0` points.
- Player-name checks are case-sensitive, so `alice` and `Alice` are treated as different names.
- Recording points requires selecting a player by index from the scoreboard.
- Points must be integers between `0` and `100`.

## Manual Verification

Normal cases

- Add the example files above and run `python main.py`.
- Expected: `Show Scoreboard` lists players in file order, and `Show Leaderboard` shows `Charlie` first with `15`, then `Alice` with `12`, then `Bob` with `9`.

Input checks to try

- Enter a blank player name when adding a player: the program should reject it.
- Try adding a duplicate name with the exact same casing: the program should reject it.
- Enter a non-integer choice or point value: the program should prompt again.
- Enter points below `0` or above `100`: the program should reject the value.
- Remove both data files and run the program again: it should recreate them automatically.
