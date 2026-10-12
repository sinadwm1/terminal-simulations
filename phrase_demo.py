"""Random phrase display inspired by an earlier crypto-themed console prototype.

This module does not derive wallet keys, mine cryptocurrency, or query balances.
"""

import argparse
import random

WORDS = (
    "amber", "atlas", "birch", "bloom", "cedar", "cinder", "coral", "dawn",
    "ember", "field", "flora", "glade", "harbor", "ivory", "juniper", "linen",
    "maple", "meadow", "moss", "ocean", "orbit", "pebble", "river", "stone",
)


def phrases(count: int, words_per_phrase: int = 12) -> list[str]:
    if count < 1 or count > 1000:
        raise ValueError("count must be between 1 and 1000")
    if words_per_phrase < 1 or words_per_phrase > len(WORDS):
        raise ValueError("invalid words_per_phrase")
    return [" ".join(random.sample(WORDS, words_per_phrase)) for _ in range(count)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Display random sample phrases")
    parser.add_argument("--count", type=int, default=5)
    args = parser.parse_args()
    print("SIMULATION ONLY - these are not wallet seeds or credentials.")
    try:
        for phrase in phrases(args.count):
            print(phrase)
    except ValueError as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    main()
