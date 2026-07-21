def check_conditions(condition1, condition2):
    if condition1:
        if condition2:
            print("Nested")

    print("Indentation applied successfully.")

condition1 = True
condition2 = True

check_conditions(condition1, condition2)