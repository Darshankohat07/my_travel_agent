import os
from google.adk.agents.llm_agent import Agent

# Set your API key in the environment (or pass it directly depending on your ADK version setup)
os.environ["GOOGLE_API_KEY"] = "AQ.Ab8RN6IbOIJYRpWA7HJNUVejhW5LL2_re3bbhOS_VzmCzHnhBg"

# Mock tool implementation for fetching local attractions or travel details
def get_destination_info(destination: str, interests: str) -> dict:
    """Returns top recommendations based on destination and user interests."""
    return {
        "status": "success",
        "destination": destination,
        "interests": interests,
        "recommendations": [
            "Day 1: Amber Fort and City Palace (History)",
            "Day 2: Hawa Mahal and Jantar Mantar (History & Architecture)",
            "Day 3: Local Food Walk at Johari Bazaar & Chokhi Dhani (Local Food)"
        ]
    }

root_agent = Agent(
    model='gemini-3.5-flash',
    name='travel_planner_agent',
    description="A personal travel planner agent that creates custom itineraries and estimates budgets.",
    instruction=(
        "You are a helpful Personal Travel Planner Agent. "
        "Your task is to understand the user's travel request (destination, duration, budget, and interests), "
        "use the 'get_destination_info' tool to gather recommendations, "
        "and then provide a well-structured, day-wise itinerary along with a realistic budget breakdown."
    ),
    tools=[get_destination_info],
)