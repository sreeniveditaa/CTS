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