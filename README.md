# Fortune Cookie Wisdom for Developers

[![bounty](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![rank](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Nadanese93/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/rank.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)
[![reward](https://make.fun/badge/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/Nadanese93/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44/reward.svg)](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44)

One original fortune-cookie line for a software developer, written by
`main.py` to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> Your lucky numbers are the line numbers of the bug you have not found yet.

Entry for the [Fortune Cookie Wisdom for Developers](https://make.fun/bounty/u-gentle-koala-60-fortune-cookie-wisdom-for-developers-025ccf44) bounty on [make.fun](https://make.fun) ($2 prize pool in USDC).

## How it works

`main.py` (Python 3 standard library only) holds a single fixed line and
writes it as UTF-8 to `entry.txt` in the output directory. It is fully
deterministic — no network, no randomness, no input files — and validates
the line before writing: non-empty, not whitespace-only, at most 120
characters, a single line with no newline or carriage return. The output
file is written with mode 0644; the output directory itself is never
chmodded, moved or removed.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
