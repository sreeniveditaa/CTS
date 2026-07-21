def split_bill(total_bill, people):
    
    if total_bill<=0:
        print("Total bill must be greater than 0.")
        return

    if people<=0:
        print("Number of people must be greater than 0.")
        return

    share = total_bill//people

    print(f"Total Bil: ₹{total_bill}")
    print(f"Number of People: {people}")
    print(f"Individual Share: ₹{share}")


total_bill=1250
people=4

split_bill(total_bill, people)