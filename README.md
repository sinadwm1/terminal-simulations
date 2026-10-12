# Terminal Simulations

[راهنمای فارسی](README_FA.md)

Two console demonstrations adapted from early Python experiments. `terminal_demo.py` plays an interactive, timed fictional security sequence. `phrase_demo.py` prints random phrases from a small original sample list. Both are simulations.

```bash
python terminal_demo.py
python phrase_demo.py --count 5
```

The terminal animation does **not** scan networks, find vulnerabilities, access systems, or extract files. Its addresses use the documentation-only `203.0.113.0/24` range. The phrase program does **not** mine cryptocurrency, generate valid wallet seeds, or check balances. The original bulk word lists and `pass.txt` are not included. Python 3 is sufficient. MIT licensed.
