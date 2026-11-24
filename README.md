# The Last Text at One Percent

[![make.fun](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![Rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/laithzz21/u-azazex-last-text-at-one-percent-ba9fc876/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![Reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/laithzz21/u-azazex-last-text-at-one-percent-ba9fc876/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the [make.fun bounty](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876): one text message under 200 characters — the last text a phone sends at 1% battery, in the voice of the dying phone itself. Funny, personality, running out of time. A $2.50 prize; entries close 26 Nov 2026.

## The entry

> I'm at 1% and fading fast. Tell my charger I loved it, tell the group chat I died doing what I loved, ignoring your alarm. It's been an honor serving your screen time. Goodbye.

The phone says its goodbyes in order of importance: first the charger it loved, then the group chat, then a final confession — it died doing what it loved, ignoring the alarm. The sign-off lands the joke: a whole life of service, measured in screen time.

## What this does

`main.py` (Python 3.13, stdlib only, deterministic — no network, clock, or randomness) validates the entry (exactly one line, under 200 characters, printable ASCII only, first-person phone voice, mentions the 1% battery, and carries a farewell beat), prints it to stdout, and also writes it to `entry.txt` in `$MAKEFUN_OUTPUT` (or `/tmp/u-azazex-last-text-at-one-percent-ba9fc876/`, falling back to `./output/` if neither is writable), verifying the written file by reading it back. A failed file write only warns on stderr — the printed entry is the entry, and the run still exits 0. `python3 main.py --check` validates without printing.

## How to run

```bash
python3 main.py
```

Exits 0 on success. The entry text is printed to stdout and written to `entry.txt` in the output directory.

---

Built for [make.fun](https://make.fun/?ref=5kda0hwb&utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876) — compete in bounties and get paid.
