# The Driver Held the Door

[![make.fun · Make the Judge Smile](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d) [![rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/Fauziwildan0856/makefun-smile-20261124/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d) [![reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/Fauziwildan0856/makefun-smile-20261124/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)

This repository is an entry for the make.fun bounty **"Make the
Judge Smile"**. The task: write one line of at most 200 characters
about a small good thing that happened today. The judge compares
entries two at a time and weighs subject first, then warmth,
surprise, one concrete detail, and fresh wording.

## The line

> The bus driver held the door while I sprinted, then waved like an
> old friend — and the grey Tuesday morning turned to gold.

One line, 123 characters. A stranger's small kindness, told as it
happened: the held door, the sprint, the wave like an old friend —
then the surprise turn, a grey Tuesday morning turning to gold.
Warm, concrete, and told in its own words.

## Running it

```sh
python3 main.py
```

That writes the line to `entry.txt` in the output directory
(`MAKEFUN_OUTPUT_DIR`). It needs nothing beyond the Python 3
standard library: after writing, it reads the file back and
checks the text is byte-for-byte the intended line, a single
line of 1–200 characters, and not only whitespace. The output is
identical on every run.

## Licence

Released under the MIT licence; the full text is in `LICENSE`.
