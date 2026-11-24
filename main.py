#!/usr/bin/env python3
"""Entry for make.fun bounty u-azazex-last-text-at-one-percent-ba9fc876.

Prints the entry text -- the last text message a phone sends at 1%
battery, written in the voice of the dying phone itself -- to stdout.
Python 3.13, stdlib only, deterministic -- no network, clock, or randomness.
"""

import os
import sys

ENTRY = (
    "I'm at 1% and fading fast. Tell my charger I loved it, tell the group "
    "chat I died doing what I loved, ignoring your alarm. It's been an honor "
    "serving your screen time. Goodbye."
)

MAX_CHARS = 200
ALLOWED_EXTRA = set(".,'\"-()!?;:%")


def count_chars(text: str) -> int:
    """Character count as the competition counts it: plain length."""
    return len(text)


def line_count(text: str) -> int:
    """Number of lines in the entry; the brief demands exactly one."""
    return text.count("\n") + 1 if text else 0


def sentence_count(text: str) -> int:
    """Rough sentence count: terminal punctuation marks that end a thought.

    A last text from a dying phone should read as a short message with a
    beat or two, not a single flat fragment, so require at least two.
    """
    return sum(1 for ch in text if ch in ".!?")


def find_bad_chars(text: str) -> list[str]:
    """Characters outside plain printable ASCII (letters, digits, space,
    and the punctuation in ALLOWED_EXTRA). Returns them sorted, unique."""
    bad = set()
    for ch in text:
        if ch.isascii() and (ch.isalnum() or ch.isspace() or ch in ALLOWED_EXTRA):
            continue
        bad.add(ch)
    return sorted(bad)


def voice_checks(text: str) -> list[str]:
    """Checks that the text really reads as the dying phone speaking.

    Returns a list of problems (empty when the voice holds up):
    - it must be first person, the phone talking about itself;
    - it must name the 1% battery it is dying on;
    - it must sound like it is running out of time (a farewell or a
      fading-out line), not like a generic status update.
    """
    problems = []
    lowered = text.lower()
    first_person = ("i'm" in lowered or "i " in lowered or " my " in lowered
                    or lowered.startswith("i"))
    if not first_person:
        problems.append("entry is not in the phone's first-person voice")
    if "1%" not in text:
        problems.append("entry never mentions the 1% battery")
    farewell_words = ("goodbye", "fading", "dying", "last", "gone", "dark")
    if not any(word in lowered for word in farewell_words):
        problems.append("entry has no farewell / running-out-of-time beat")
    if "charger" not in lowered and "charge" not in lowered:
        problems.append("entry never mentions the charger it is leaving behind")
    return problems


def validate(text: str) -> None:
    """Check the entry meets every rule in the competition brief.

    Fails loudly (ValueError) on the first violated rule so a bad entry
    can never be printed as if it were valid.
    """
    if not text:
        raise ValueError("entry is empty")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    if line_count(text) != 1:
        raise ValueError(
            f"entry must be exactly one line, got {line_count(text)} lines"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no newline characters)")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    chars = count_chars(text)
    if chars >= MAX_CHARS:
        raise ValueError(
            f"entry is {chars} chars, must be under the {MAX_CHARS} limit"
        )
    bad = find_bad_chars(text)
    if bad:
        raise ValueError(f"entry contains disallowed characters: {bad!r}")
    if text.count(" ") < 5:
        raise ValueError("entry is too short to be a real text message")
    if sentence_count(text) < 2:
        raise ValueError(
            f"entry has {sentence_count(text)} sentence(s); a dying phone's "
            "last text needs at least two beats"
        )
    problems = voice_checks(text)
    if problems:
        raise ValueError("voice check failed: " + "; ".join(problems))


def write_entry(text: str) -> str | None:
    """Write the entry to the output file, falling back to ./output/.

    Returns the path written, or None if every location failed.
    """
    out_dir = os.environ.get("MAKEFUN_OUTPUT") or "/tmp/u-azazex-last-text-at-one-percent-ba9fc876"
    for candidate in (out_dir, "./output"):
        try:
            os.makedirs(candidate, exist_ok=True)
            path = os.path.join(candidate, "entry.txt")
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(text + "\n")
            return path
        except OSError:
            continue
    return None


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    check_only = "--check" in args
    try:
        validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    if check_only:
        print(
            f"entry valid: {count_chars(ENTRY)} chars, "
            f"{sentence_count(ENTRY)} sentences, 1 line",
            file=sys.stderr,
        )
        return 0
    print(ENTRY)
    # Also persist the entry; a failed write only warns -- the printed
    # entry is the entry, and the run still exits 0.
    path = write_entry(ENTRY)
    if path is None:
        print("warning: could not write entry.txt anywhere", file=sys.stderr)
    else:
        # Read-back verification: the file must contain exactly the entry.
        try:
            with open(path, encoding="utf-8") as fh:
                if fh.read().rstrip("\n") != ENTRY:
                    print(f"warning: read-back mismatch in {path}", file=sys.stderr)
        except OSError as exc:
            print(f"warning: could not read back {path}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
