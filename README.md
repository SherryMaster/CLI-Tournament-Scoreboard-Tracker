# Tournament Scoreboard Tracker

Simple tracker for tournament players and scores.

## Overview

This small project reads player and score data and displays a tournament scoreboard.

## Features

- Read players and scores from plain text files
- Produce a ranked scoreboard (highest score first)
- Easy to run locally with Python

## Requirements

- Python 3.8+

## Run

From the project root, run:

```
python main.py
```

## Usage

- Place player names in `data/players.txt`, one name per line.
- Place scores in `data/scores.txt`. Use a simple per-line format pairing names and scores (example formats below).

Example `players.txt`:

```
Alice
Bob
Charlie
```

Example `scores.txt` (option A, name and score separated by comma):

```
Alice, 12
Bob, 9
Charlie, 15
```

Or (option B, tab or space separated):

```
Alice 12
Bob 9
Charlie 15
```

Adjust the files to match the parser used by `main.py`.

## Case-sensitivity decision

This project treats player names as case-insensitive for matching and deduplication. Input should be treated as human-friendly (e.g., `alice`, `Alice`, and `ALICE` are the same player).

Implementation note: the program should normalize names (for example, to lowercase) when reading and comparing.

## Manual Verification

Normal cases

- Add the example files above and run `python main.py`.
- Expected: a ranked list showing `Charlie` first (15), then `Alice` (12), then `Bob` (9).

Invalid-input cases to try

- Malformed score line (e.g., `Alice: twelve`): verify the program either logs a clear error or skips the line with a warning.
- Missing files: remove `data/players.txt` or `data/scores.txt` and verify the program prints a helpful message rather than crashing.
- Duplicate names with different casing (e.g., `alice` and `Alice`): verify they are treated as the same player and scores are aggregated or handled per program design.

If you'd like, I can also update `main.py` to include explicit parsing rules and graceful error handling to match these expectations.
