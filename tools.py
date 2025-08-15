def get_calendar_events(date):
    events = [
        {"title": "Gym", "time": "18:00"},
        {"title": "Team Meeting", "time": "10:00"}
    ]
    return {"date": date, "events": events}


def check_travel_time(origin, destination):
    return {
        "origin": origin,
        "destination": destination,
        "travel_time_minutes": 12
    }


def book_meeting(title, start_time, location):
    return {
        "status": "confirmed",
        "title": title,
        "start_time": start_time,
        "location": location
    }
