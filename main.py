import time
from news_client import get_top_headlines
from sentiment import get_mood
from tint import show_tint

# How often to check the news (in seconds)
CHECK_INTERVAL = 1800  # 30 minutes

def main():
    """Main loop: fetch news, analyze mood, display tint."""
    print("Starting Ubiquitous Computing Helper...")
    print(f"Checking news every {CHECK_INTERVAL // 60} minutes.\n")

    while True:
        print("Fetching headlines...")
        headlines = get_top_headlines()

        print("Analyzing mood...")
        mood = get_mood(headlines)

        print(f"Current mood: {mood}")
        print("Displaying tint...\n")
        show_tint(mood)

        print(f"Waiting {CHECK_INTERVAL // 60} minutes until next check...")
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()