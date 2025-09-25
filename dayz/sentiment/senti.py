import sys
from transformers import pipeline
def analyze_sentiment(text_to_analyze):
    try:
        print("Loading model...")
        sentiment_pipeline = pipeline(
            "sentiment-analysis", 
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        print("Model loaded successfully. Analyzing text...")
        results = sentiment_pipeline(text_to_analyze)
        result = results[0]
        label = result['label']
        score = result['score']

        print("\n--- Analysis Complete ---")
        print(f"Input Text: \"{text_to_analyze}\"")
        print(f"Sentiment:  {label}")
        print(f"Confidence: {score:.4f}")
        print("-----------------------")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please ensure you have an active internet connection for the first run.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: No input text provided.")
        print("Usage: python sentiment_analyzer.py \"Your text goes here\"")
        sys.exit(1)
    input_text = " ".join(sys.argv[1:])
    analyze_sentiment(input_text)