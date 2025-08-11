# Python_Basics_To_Usable_Tools

A tidy collection of beginner-friendly Python utilities turned into actually useful, runnable tools. 
Each utility has a small CLI, examples, and saves outputs to `out/`. 
No course text or certification banners included.

## Tools
1. **stats-cli** — compute mean/median/mode/std/min/max for a CSV column.
2. **histogram-maker** — produce a histogram PNG from a CSV column.
3. **distribution-visualizer** — plot Normal, Binomial, or Poisson distributions given parameters.
4. **grade-manager** — summarize a grade CSV, compute curve & letter grades, and export a report.

## Quick start
```bash
pip install -r requirements.txt
python -m python_basics_tools --help
```
Then run any subcommand (see examples below).

### Examples
```bash
# 1) Stats on a CSV column
python -m python_basics_tools stats   --csv examples/sample_numbers.csv --col value --out out/stats.json

# 2) Histogram
python -m python_basics_tools hist   --csv examples/sample_numbers.csv --col value --bins 20 --out out/hist.png

# 3) Distributions: Normal (mu=0, sigma=1)
python -m python_basics_tools dist normal   --mu 0 --sigma 1 --x-min -4 --x-max 4 --out out/normal.png

# 3) Distributions: Binomial (n=20, p=0.4)
python -m python_basics_tools dist binomial   --n 20 --p 0.4 --out out/binomial.png

# 3) Distributions: Poisson (lambda=4)
python -m python_basics_tools dist poisson   --lam 4 --k-max 15 --out out/poisson.png

# 4) Grade manager
python -m python_basics_tools grades   --csv examples/sample_grades.csv --student-col student --score-col score   --curve 5 --scheme "90:A,80:B,70:C,60:D" --out out/grades_report.csv
```
