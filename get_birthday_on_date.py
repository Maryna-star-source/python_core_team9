from collections import defaultdict

from datetime import date, datetime, timedelta

from classes import (
    Name,
    Phone,
    Email,
    Address,
    Record,
    AddressBook,
    BirthDay,
    PhoneError,
    BDayError,
    EmailError,
    NoContactError,
)

# def get_period(start_date: date, days: int) -> dict:
#     result = {}
#     for _ in range(days + 1):
#         result[start_date.day, start_date.month] = start_date.year
#         start_date += timedelta(1)
#     return result

def get_birthdays_on_date(users: AddressBook, days=None):
    Birthday_people = []

    if not days:
        days = 0

    start_date = date.today()
    new_date = start_date + timedelta(days)
    new_date_birthday = new_date.day, new_date.month

    for name, record in users.data.items():
        birthday: date = record.birthday.value
        date_birthday = birthday.day, birthday.month
        if date_birthday == new_date_birthday:
            Birthday_people.append(record)

#     return Birthday_people
    return Birthday_people

# if __name__ == "__main__":
    # users = [
    #     {"name": "Jan Koum", "birthday": datetime(1976, 2, 20).date()},
    #     {"name": "Kim", "birthday": datetime(1976, 2, 20).date()},
    # ]

    # result = get_birthdays_per_week(users)
    # print(result)
    # # Виводимо результат
    # for day_name, names in result.items():
    #     print(f"{day_name}: {names}")

    # start_date = date.today()
    # new_date = start_date + timedelta(1)

    # print(start_date)
    # print(new_date)
