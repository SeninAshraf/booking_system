from datetime import datetime, date

while True:
    show_date = input("Enter Show Date (YYYY-MM-DD): ")

    try:
        show_date = datetime.strptime(
            show_date,
            "%Y-%m-%d"
        ).date()

        if show_date < date.today():
            print("Show date cannot be in the past.")
            continue

        break

    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD.")