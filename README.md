# Week 6 Assignment: Times Tables, Skip Counting & Loop Hospital

## Project Files
* `times_table.py`: Asks the user for a number and prints its multiplication table from 1 to 10 using `range(1, 11)` and f-strings.
* `skip_counter.py`: Uses `range()` step parameters to display even numbers from 0 to 20 and count down from 10 to 0.
* `loop_hospital.py`: Contains diagnostic fixes and `# FIXED:` explanations for three bugged loops (off-by-one, infinite loop, and misplaced accumulator).

## Reflection & Concepts
An **off-by-one error** occurs when a loop iterates one time too many or one time too few, typically caused by misunderstanding whether boundary values in conditions or ranges are inclusive or exclusive. 

In Python, the habit that helps avoid this is remembering that `range(start, stop)` is **exclusive of the `stop` value**. To include a specific upper limit $N$, always set the stop boundary to $N + 1$.