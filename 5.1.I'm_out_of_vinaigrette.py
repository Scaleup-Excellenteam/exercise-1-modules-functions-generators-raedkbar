from datetime import datetime, timedelta
import random
from typing import List


DATE_FORMAT = '%Y-%m-%d'


def get_date_range() -> List[datetime]:
    """
    Prompts the user to enter a valid date range and returns a list containing the first and second dates.

    Returns:
        List[datetime]: A list containing the first and second dates as datetime objects.
    """
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


def generate_random_date(date_range: List[datetime]) -> datetime:
    """
    Generates a random date within the given date range.

    Params:
        date_range (List[datetime]): A list containing the first and second dates as datetime objects.

    Returns:
        datetime: A randomly generated date within the given range.
    """
    first_date, second_date = date_range
    random_days = random.randint(0, (second_date - first_date).days)
    return second_date + timedelta(days=random_days)


def main() -> None:
    """
    The main function of the program.
    Generates a random date within the user-defined date range and checks if it is a Monday.
    If it is Monday, it prints "I'm out of vinaigrette!".
    """
    random_date = generate_random_date(get_date_range())
    if random_date.weekday() == 0:
        print("I'm out of vinaigrette!")


if __name__ == '__main__':
    main()
