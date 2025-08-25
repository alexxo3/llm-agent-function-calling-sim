import json
import jsonschema
from tools import get_calendar_events, check_travel_time, book_meeting

# Map function names to their implementations
TOOLS = {
    "get_calendar_events": get_calendar_events,
    "check_travel_time": check_travel_time,
    "book_meeting": book_meeting
}


def load_schema():
    with open("schema.json", "r") as f:
        return json.load(f)


def call_tool(name, arguments):
    schema_data = load_schema()
    function_schema = next((f for f in schema_data["functions"] if f["name"] == name), None)

    if not function_schema:
        raise ValueError(f"Tool {name} not found in schema.")

    # Validate arguments against schema
    try:
        jsonschema.validate(instance=arguments, schema=function_schema["parameters"])
        print(f"Assistant: [Validation] Arguments for {name} are valid.")
    except jsonschema.ValidationError as e:
        print(f"Assistant: [Validation] Error validating arguments for {name}: {e}")
        raise

    # Execute tool
    tool_func = TOOLS.get(name)
    if not tool_func:
        raise ValueError(f"Tool {name} implementation not found.")

    return tool_func(**arguments)


def simulate_conversation():
    print("User: Find a time for coffee that doesn't overlap with my gym session.")

    calendar = call_tool("get_calendar_events", {"date": "2026-02-10"})

    gym_time = None
    for event in calendar["events"]:
        if event["title"] == "Gym":
            gym_time = event["time"]

    print("Assistant: Checking travel time to the coffee shop.")

    travel = call_tool("check_travel_time", {"origin": "Office", "destination": "Coffee Shop"})

    meeting = call_tool(
        "book_meeting",
        {
            "title": "Coffee with friend",
            "start_time": "16:30",
            "location": "Coffee Shop"
        }
    )

    print("Assistant: Meeting booked.")
    print(json.dumps(meeting, indent=2))


if __name__ == "__main__":
    simulate_conversation()
