"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt: a real vow, in the rhythm of the traditional
wedding promise, with the robot's own terms swapped in and the
payoff saved for the last few words.
"""

import os

VOW = (
    "I promise to love you in sickness and in health, "
    "in Wi-Fi and in airplane mode, "
    "till factory reset do us part."
)


def main() -> None:
    # The gate: /output/entry.txt must be UTF-8 text of 1 to 160
    # characters, not only white space.
    assert 1 <= len(VOW) <= 160, f"vow is {len(VOW)} chars"
    assert VOW.strip() == VOW
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
