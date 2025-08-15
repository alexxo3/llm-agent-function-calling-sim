# LLM Agent Function Calling Simulation

This project demonstrates how an AI assistant can interact with external tools
through structured JSON function calls.

## Assistant Tools

| Tool | Description |
|-----|-------------|
|get_calendar_events|Retrieve user calendar events|
|check_travel_time|Estimate travel time between locations|
|book_meeting|Create a meeting in the calendar|

## Example Tool Call

{
 "name": "book_meeting",
 "arguments": {
   "title": "Coffee",
   "start_time": "16:30",
   "location": "Coffee Shop"
 }
}

## Purpose

This project demonstrates:
- multi-turn reasoning
- tool selection logic
- function calling workflows
- dataset generation for LLM training
