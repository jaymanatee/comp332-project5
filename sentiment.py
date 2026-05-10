from textblob import TextBlob

def get_mood(headlines):
    """Analyze sentiment of headlines and return overall mood."""
    # Get polarity score for each headline (-1 negative, 0 neutral, 1 positive)
    scores = [TextBlob(headline).sentiment.polarity for headline in headlines]
    avg_score = sum(scores) / len(scores)

    if avg_score > 0.1:
        return "positive"
    elif avg_score < -0.1:
        return "negative"
    else:
        return "neutral"

if __name__ == "__main__":
    from news_client import get_top_headlines
    headlines = get_top_headlines()
    print(f"Mood: {get_mood(headlines)}")