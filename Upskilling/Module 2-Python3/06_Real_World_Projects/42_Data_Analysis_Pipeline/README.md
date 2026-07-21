# Exercise 42 - Data Analysis Pipeline

## Objective

Use modules, functions, lists, file handling, and error handling together.

## Task

Process sales data from a file and calculate statistics.

## Instructions

- Import the `statistics` module.
- Read numeric data from `sales.txt`.
- Handle file and data errors using `try-except`.
- Calculate the mean and median.
- Print a statistics summary.

## Project Structure

- `Exercise_42.py` - Python source code
- `sales.txt` - Input sales data
- `42_output.png` - Program output screenshot

## Code

```python
import statistics


def analyze_sales(filename):
    try:
        with open(filename, "r") as file:
            sales = []

            for line in file:
                line = line.strip()

                if line:
                    sales.append(float(line))

        if not sales:
            print("Error: No sales data found.")
            return

        mean_sales = statistics.mean(sales)
        median_sales = statistics.median(sales)

        print("Sales Statistics Summary")
        print(f"Sales Data: {sales}")
        print(f"Mean Sales: {mean_sales:.2f}")
        print(f"Median Sales: {median_sales:.2f}")

    except FileNotFoundError:
        print("Error: sales.txt not found.")
    except ValueError:
        print("Error: Invalid numeric data in sales.txt.")


analyze_sales("sales.txt")
```

## Expected Output

```
Sales Statistics Summary
Sales Data: [1500.0, 2300.0, 1750.0, 2000.0, 2800.0]
Mean Sales: 2070.00
Median Sales: 2000.00
```