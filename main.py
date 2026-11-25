"""Angry Judge: The Short Rant Contest.

A program that writes one short, funny rant about an everyday
annoyance to /output/entry.txt: 47 minutes on hold with a company
that keeps insisting your call is important to it.

Python 3.13, standard library only. No network, no dependencies,
no randomness, no timestamps: every run writes the same bytes.
"""

from pathlib import Path

TEXT = (
    '"Your call is important to us." 47 minutes of saxophone later, '
    "I can hum the hold music at my own funeral. A human finally "
    'answers, says "let me transfer you," and \u2014 click \u2014 the '
    "same saxophone starts again. I have been important to this "
    "company for a full hour, and the only thing that has spoken to "
    "me is a robot that lies."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    code_points = len(TEXT)
    assert 1 <= code_points <= 400, f"text is {code_points} code points"
    assert TEXT.strip(), "text must not be only white space"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
