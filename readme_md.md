# Personal Travel Planner Agent 🌍✈️

A Python-based Personal Travel Planner Agent built using the Google ADK and powered by Google's Gemini models. This agent helps users design custom day-wise itineraries and budget estimations based on their destinations, duration, budget, and personal interests (such as history, local food, or adventure).

---

## Features
- **Requirement Analysis:** Understands user inputs regarding destination, duration, budget, and interests.
- **Custom Itinerary Generation:** Generates structured, day-wise travel plans.
- **Tool Integration:** Uses custom mock or real tools (`get_destination_info`) to fetch tailored destination recommendations.
- **Budget Estimation:** Provides a rough expense overview aligned with user constraints.

---

## Prerequisites
- Python 3.8 or higher installed on your system.
- Google ADK package installed.
- A valid Google Gemini API Key.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/travel-planner-agent.git
   cd travel-planner-agent
   ```

2. **Install dependencies (if applicable):**
   ```bash
   pip install google-adk
   ```

3. **Configure your API Key:**
   Make sure to set your API key securely as an environment variable in your script or terminal before running:
   ```bash
   set GOOGLE_API_KEY="your-api-key-here"
   ```

---

## Usage

Run your agent script using Python:
```bash
python travel_agent.py
```

### Example Input/Use Case:
* **User Request:** *"I want to visit Jaipur for 3 days with a budget of ₹15,000. I like history and local food."*
* **Agent Output:** A 3-day itinerary highlighting key attractions like Amber Fort, City Palace, Hawa Mahal, and local food spots, combined with budget projections.

---

## Security Warning ⚠️
Never commit your raw API keys directly to public GitHub repositories. Always load credentials using environment variables or a `.env` file (and make sure to add `.env` to your `.gitignore`).

---

## License
This project is open-source and available under the [MIT License](LICENSE).