from collections import defaultdict

from datetime import date, datetime, timedelta

# def get_period(start_date: date, days: int) -> dict:
#     result = {}
#     for _ in range(days + 1):
#         result[start_date.day, start_date.month] = start_date.year
#         start_date += timedelta(1)
#     return result

def get_birthdays_per_week(users, days=100):
    # Реалізуйте тут домашнє завдання
    Birthday_people = defaultdict(list)

    start_date = date.today()
    new_date = start_date + timedelta(days)
    new_date_birthday = new_date.day, new_date.month

    for user in users:
        birthday: date = user["birthday"]
        date_birthday = birthday.day, birthday.month
        if date_birthday == new_date_birthday:
            Birthday_people[user["name"]].append(user["birthday"])

#     return Birthday_people
    return Birthday_people

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 2, 20).date()},
        {"name": "Kim", "birthday": datetime(1976, 2, 20).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {names}")

    # start_date = date.today()
    # new_date = start_date + timedelta(100)

    # print(start_date)
    # print(new_date)
