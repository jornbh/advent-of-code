# Manual solution to day 3 of advent of code

This task coud be completed almost entirely using some normal regex, grep, Vim and some Python to do the additions and multiplications. As a result, this day was kind of silly

## 1

```bash
cat input.txt grep -oG \(mul([0-9]*,[0-9]*)\) | tee muls.txt
```

- Then, to process this:
- replace , with *. Replace mul with print. Pipe into Python
- colapse all lines into one. Replace " " with "+". Pipe into python

## 2

```bash
cat input.txt grep -oG \(mul([0-9]*,[0-9]*)\|do()\|don't()\) | tee conditional_muls.txt
```

Same a  step 1, but first:

`:g/do()/norm! O`
`:g/don't()/norm! O`
`:g/don't()/norm! dip`
`:g/do()/norm! dd`

Then, repeat step 1.

## Notes

- I solved this a bit faster due to
  - Better mappings in vim for some of the longer commands
  - A script for properly handling input piped into Python, so that it is easier to integrate with Vim

