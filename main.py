"""Funniest Time Machine Warning Label — make.fun entry.

Writes a single warning label (1-120 chars) to /output/entry.txt
with no trailing newline.
"""

import os

ENTRY = "WARNING: Do not meet yourself. Four minutes later you will agree. Eleven hours later you will fight about it."

# Deadpan warning, one specific rule, escalated twice: first you agree
# with your past self, then you end up fighting about it — and the
# concrete numbers (four minutes, eleven hours) sell the time-travel
# absurdity better than any vague "do not" could.
assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
