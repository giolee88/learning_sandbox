# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

for filepath in ["Sample1.txt", "Sample2.txt", "Sample3.txt"]:
    with open(filepath, 'r') as input_file:
        sample = input_file.read()

    compound = analyzer.polarity_scores(sample)["compound"]
    pos = analyzer.polarity_scores(sample)["pos"]
    neu = analyzer.polarity_scores(sample)["neu"]
    neg = analyzer.polarity_scores(sample)["neg"]

    # Print Samples and Analysis
    print(sample)
    print("Compound Score: %s" % compound)
    print("Positive Score: %s" % pos)
    print("Neutral Score: %s" % neu)
    print("Negative Score: %s" % neg)
    print("")
