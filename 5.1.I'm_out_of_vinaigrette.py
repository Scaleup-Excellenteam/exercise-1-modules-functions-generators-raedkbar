from datetime import datetime, timedelta
import random

DATE_FORMAT = '%Y-%m-%d'


def get_date_range():
    while True:
        try:
            first_date = datetime.strptime(input("Enter the first date (YYYY-MM-DD): "), DATE_FORMAT)
            second_date = datetime.strptime(input("Enter the second date (YYYY-MM-DD): "), DATE_FORMAT)
            if first_date <= second_date:
                return [first_date, second_date]
            else:
                print("The first date must be before or the same as the second date.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def generate_random_date(date_range):
    start, end = date_range
    random_days = random.randint(0, (end - start).days)
    return start + timedelta(days=random_days)


random_date = generate_random_date(get_date_range())

if random_date.weekday() == 0:
    print("I'm out of vinaigrette!")
