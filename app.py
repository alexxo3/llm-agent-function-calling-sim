import json
from tools import get_calendar_events, check_travel_time, book_meeting


def simulate_conversation():

    print("User: Find a time for coffee that doesn't overlap with my gym session.")

    calendar = get_calendar_events("2026-02-10")

    gym_time = None
    for event in calendar["events"]:
        if event["title"] == "Gym":
            gym_time = event["time"]

    print("Assistant: Checking travel time to the coffee shop.")

    travel = check_travel_time("Office", "Coffee Shop")

    meeting = book_meeting(
        title="Coffee with friend",
        start_time="16:30",
        location="Coffee Shop"
    )

    print("Assistant: Meeting booked.")
    print(meeting)


if __name__ == "__main__":
    simulate_conversation()
