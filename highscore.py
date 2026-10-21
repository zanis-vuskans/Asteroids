HIGHSCORE_FILE = "highscore.txt"

def load_high_score():
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip())
    except (FileNotFoundError, ValueError):
        return 0

def save_high_score(value):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(value))