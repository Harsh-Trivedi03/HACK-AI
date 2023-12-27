from uagents import Agent, Context
from uagents.setup import fund_agent_if_low
import requests

class NotificationAgent(Agent):
    def __init__(self, name, seed):
        super().__init__(name=name, seed=seed)

    def send_notification(self, message):
        CALLMEBOT_API_KEY = 'YOUR_USER_NAME_OF_TELEGRAM'  # Replace with actual API key
        url = f"http://api.callmebot.com/text.php?user={CALLMEBOT_API_KEY}&text={message}"
        response = requests.get(url)
        return response.status_code

notification_agent = NotificationAgent("notification", "notification_seed")
# Example usage
response = notification_agent.send_notification("Dear Harsh, Your interview is scheduled for 11th February 2024 at 10:00 AM at Microsoft, Bangalore")
print("Notification sent, status:", response)