import random
import time
from datetime import datetime, timedelta
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

quotes = ["Set your goals high and do not stop till you get there.",
          "To shine like the sun, you need to burn like one.",
          "If your dreams don't scare you, they are not big enough.",
          "To success in life. You need two things. Ignorance and Confidence.",
          "Work until you don't, have to introduce yourself.",
          "Whatever brings you down, will eventually make you stronger!",
          "You must do the things, you think you cannot do.",
          "Don't quit. You're already in pain. You're already hurt. Get a reward from it.",
          "When you focus on problem. You will have more problem. When you focus on possibilities. You will have more opportunities.",
          "You become who you spend your time with."]


def print_quote_in_slack():
    try:
        slack_token = "xoxb-4372378497634-5634271777729-jz8UYsEKsSQkkVKSKjmKqP49"
        client = WebClient(token=slack_token)
        channel_name = "general"  # Replace "general" with your desired channel name
        response = client.chat_postMessage(
            channel="#" + channel_name,
            text=random.choice(quotes) + " Good evening"
        )
        print("Message sent successfully!")
    except SlackApiError as e:
        print(f"Error sending message: {e}")


def print_hello_world():
    return random.choice(quotes) + " Good evening"
    # print("Hello, World!")


def wait_until_morning():
    now = datetime.now()
    tomorrow_morning = now.replace(
        hour=10, minute=0, second=0, microsecond=0) + timedelta(days=1)
    time_to_wait = (tomorrow_morning - now).total_seconds()
    print(time_to_wait)
    time.sleep(time_to_wait)


if __name__ == "__main__":
    while True:
        wait_until_morning()
        print_quote_in_slack()
        print_hello_world()

# In this code, we define two functions: print_hello_world() to print the "Hello, World!" message and wait_until_morning() to calculate the time remaining until the next morning (7:00 AM) and sleep the program until then using the time.sleep() function.

# The wait_until_morning() function calculates the time remaining until tomorrow morning (7:00 AM) by obtaining the current date and time using datetime.now() and then setting the time for tomorrow morning using replace(). We add 1 day to ensure it's the next morning. The total_seconds() method calculates the total time remaining in seconds, which is then passed to time.sleep() to make the program sleep until the next morning.

# The main loop in the if __name__ == "__main__": block ensures that the program continuously waits until the next morning and then prints "Hello, World!" at 7:00 AM every day.

# Keep in mind that this code assumes you want to print the message at 7:00 AM local time. You can adjust the hour and minute in the tomorrow_morning variable to match your desired morning time.
