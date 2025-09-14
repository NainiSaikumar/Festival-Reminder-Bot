"""Festival Reminder Bot - keeps track of upcoming festivals."""

import datetime


# Predefined festivals (you can add/remove here)
festivals = {
    "Diwali": "2025-10-20",
    "Christmas": "2025-12-25",
    "New Year": "2026-01-01",
    "Sankranti": "2026-01-14",
}


def view_festivals():
    """Show all saved festivals."""
    print("\nFestivals:")
    if not festivals:
        print("  (No festivals saved)")
    else:
        for name, date in festivals.items():
            print(f"- {name}: {date}")


def add_festival():
    """Add a new festival with name and date."""
    name = input("Enter festival name: ").strip()
    date_str = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")  # validate format
        festivals[name] = date_str
        print(f"{name} added successfully.")
    except ValueError:
        print("Invalid date format! Use YYYY-MM-DD.")


def delete_festival():
    """Delete a festival by name."""
    name = input("Enter festival name to delete: ").strip()
    if name in festivals:
        del festivals[name]
        print(f"{name} deleted.")
    else:
        print("Festival not found.")


def check_reminders():
    """Check festivals happening today or in the next 7 days."""
    today = datetime.date.today()
    upcoming = []

    for name, date_str in festivals.items():
        fest_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        diff = (fest_date - today).days

        if diff == 0:
            print(f"Today is {name}!")
        elif 0 < diff <= 7:
            print(f"{name} is in {diff} day(s), on {fest_date}")
        upcoming.append((fest_date, name))

    if upcoming:
        upcoming.sort()
        next_date, next_name = upcoming[0]
        print(f"\nNext Festival: {next_name} on {next_date}")


def main():
    """Main menu loop."""
    while True:
        print("\n=== Festival Reminder Bot ===")
        print("1. View festivals")
        print("2. Add a festival")
        print("3. Delete a festival")
        print("4. Check reminders")
        print("5. Exit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_festivals()
        elif choice == "2":
            add_festival()
        elif choice == "3":
            delete_festival()
        elif choice == "4":
            check_reminders()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
