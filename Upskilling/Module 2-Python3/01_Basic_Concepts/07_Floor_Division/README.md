# Exercise 7 - Floor Division

## Objective
Perform integer division using a function, validation, and formatted output.

## Task
Split a total bill equally among people using the floor division (`//`) operator.

## Instructions
- Use a function.
- Validate the total bill and number of people.
- Use floor division (`//`).
- Print the individual share.
- Use the variables `total_bill = 1250` and `people = 4`.

## Project Structure

- `Exercise_07.py` - Python source code
- `07_output.png` - Program output screenshot

## Code

```python
def split_bill(total_bill, people):
    
    if total_bill<=0:
        print("Total bill must be greater than 0.")
        return

    if people<=0:
        print("Number of people must be greater than 0.")
        return

    share=total_bill//people

    print(f"Total Bil: ₹{total_bill}")
    print(f"Number of People: {people}")
    print(f"Individual Share: ₹{share}")


total_bill=1250
people=4

split_bill(total_bill, people)
```

## Expected Output

```
Total Bill: ₹1250
Number of People: 4
Individual Share: ₹312
```