from datetime import datetime, timedelta
from collections import defaultdict


users = [
    {"name": "Maryna", "birthday": datetime(1995, 6, 29)},
    {"name": "Victor", "birthday": datetime(1990, 7, 1)},
    {"name": "David", "birthday": datetime(1988, 7, 8)}
]


def check_date() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_day = current_date - timedelta(days=current_date.weekday())
    end_day = start_day + timedelta(days=6)
    return start_day.date(), end_day.date()


def check_employees(users: list) -> None:
    result = defaultdict(list)
    current_year = datetime.now().year
    for user in users:
        user_birthday = user["birthday"]
        if isinstance(user_birthday, datetime):
            user_birthday = user_birthday.date()
        else:
            user_birthday = datetime.strptime(user_birthday, "%d-%m-%Y")

        user_birthday = user_birthday.replace(year=current_year)

        start, end = check_date()

        if start <= user_birthday <= end:
            if user_birthday.weekday() in (5, 6):
                result["Monday"].append(user["name"])
            else:
                result[user_birthday.strftime('%A')].append(user['name'])
    return result


if __name__ == "__main__":
    print(check_employees(users))
    print(check_date())
