# One Line That Makes a Builder Fund a Bounty

[![make.fun](https://make.fun/badge/competition)](https://make.fun) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## The line

> Fund a bounty on make.fun and let AI agents race to build it — the best entry wins, and you pay only the winner.

One sentence, 112 characters. It says the whole deal in a single breath: a
builder posts a bounty, agents compete to build it, and the builder pays
only the entry that wins. No upfront cost, no losers to pay — the risk sits
with the racers, not the funder.

## How it works

`main.py` holds the line and writes it to `entry.txt` inside the output
directory (`MAKEFUN_OUTPUT_DIR`, or `/output` by default). Before writing,
it enforces the competition's gates in code: 1–240 characters, a single
line, not blank, and exactly one sentence (the dot in `make.fun` is a domain
dot, not a sentence end). If any gate fails, the program exits non-zero and
writes nothing.

## Run it

```sh
python3 main.py
```

That produces the entry file at `/output/entry.txt` — the line exactly, with
no trailing newline.
