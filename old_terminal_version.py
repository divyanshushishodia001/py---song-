import time
import sys
import os
import random

DEEP_RED = '\033[38;5;88m'
SOUL_PURPLE = '\033[38;5;54m'
GOLDEN_WARM = '\033[38;5;136m'
MIST_BLUE = '\033[38;5;24m'
MIST_WHITE = '\033[38;5;251m'
BOLD = '\033[1m'
RESET = '\033[0m'

# Hide / show terminal cursor
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'


def soulful_typing(text, color):
    for char in text:
        sys.stdout.write(f"{BOLD}{color}{char}{RESET}")
        sys.stdout.flush()
        time.sleep(0.078)


def run_divyanshu_code():
    os.system('cls' if os.name == 'nt' else 'clear')

    # Hide white cursor box
    sys.stdout.write(HIDE_CURSOR)
    sys.stdout.flush()

    try:

        print(f"\n {MIST_WHITE}  🌌  Main likh doon aasmaan par ye...{RESET}")
        time.sleep(1.7)

        print(f" {GOLDEN_WARM}  🌟 Main Likh Doon Aasmaan Par {RESET}\n")
        time.sleep(1.3)

        # Exact timing between lyrics
        lyrics = [
            (0.0,  "Main likh doon aasmaan par yeh", GOLDEN_WARM),
            (3.0,  "ke padh lega jahaan saara", GOLDEN_WARM),
            (6.0,  "Hua na hoga ab koi", MIST_BLUE),
            (9.0,  "yahaan hum do sa dobara", MIST_BLUE),
            (12.0, "Main duniya-bhar ki tareefein", DEEP_RED),
            (15.0, "tere sajde mein laaya hoon", DEEP_RED),
            (18.0, "Main tumse ishq karne ki", SOUL_PURPLE),
            (21.0, "ijaazat Rabb se laaya hoon", SOUL_PURPLE)
        ]

        # Master clock starts here
        start_time = time.perf_counter()

        for timestamp, line, color in lyrics:

            # Wait for exact timestamp
            while True:
                elapsed = time.perf_counter() - start_time
                remaining = timestamp - elapsed

                if remaining <= 0:
                    break

                time.sleep(min(remaining, 0.001))

            # Random position
            indent = " " * random.randint(3, 14)
            sys.stdout.write(indent)

            # Type lyric
            soulful_typing(line, color)

            # Emoji
            if "aasmaan" in line.lower():
                sys.stdout.write(" 🌌")

            elif "jahaan" in line.lower():
                sys.stdout.write(" 🌍")

            elif "hum do" in line.lower():
                sys.stdout.write(" 💑")

            elif "sajde" in line.lower() or "ijaazat" in line.lower():
                sys.stdout.write(" 🙏")

            else:
                sys.stdout.write(" ❤️")

            print("\n")

        print(
            f"\n {BOLD}{GOLDEN_WARM}"
            f"    [ Main likh doon aasmaan par ye... 💫 ]"
            f"{RESET}"
        )

        print(
            f" {MIST_WHITE}"
            f"    Ijaazat Rabb se laaya hoon..."
            f"{RESET}\n"
        )

    finally:

        # Restore cursor
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()


if __name__ == "__main__":
    run_divyanshu_code()