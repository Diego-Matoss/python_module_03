#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    argc = len(sys.argv)
    scores = []

    if argc > 1:
        for score in sys.argv[1:]:
            try:
                new_score = int(score)
            except ValueError:
                print(f"Invalid parameter: '{score}'")
            else:
                scores.append(new_score)

    if len(scores) == 0:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} <score1> ...")
    else:
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average score: {(sum(scores) / len(scores)):.1f}")
        print(f"High score: {max(scores)}")
        print(f"Low score: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
