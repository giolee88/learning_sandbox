# Import and Initialize Sentiment Analyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Sample Strings
happy_string = "Your humble instructor is smart, beautiful, and funny!"
angry_string = "Ugh. I am feeling so distraught! I hate everything. " \
     "I just want to do mean things to everyone."
happy_emoticon_string = ":-) :) :-D  ;-) :-P"
angry_emoticon_string = ":-( :( D-< :'("
funny_slang_string = "lol rofl haha"
angry_slang_string = "Sux meh grr"


sample_strings = {
	'happy': happy_string,
	'angry': angry_string,
	'happy emoticon': happy_emoticon_string,
	'angry emoticon': angry_emoticon_string,
	'funny slang': funny_slang_string,
	'angry slang': angry_slang_string
}

# Target String Setting
print("String choices: ")
for emotion, sample_string in sample_strings.items():
	print(f"{emotion}\n\t{sample_string}\n")
string_choice = input("Which string do you want?  ")

target_string = sample_strings[string_choice]

# Run analysis
compound = analyzer.polarity_scores(target_string)["compound"]
pos = analyzer.polarity_scores(target_string)["pos"]
neu = analyzer.polarity_scores(target_string)["neu"]
neg = analyzer.polarity_scores(target_string)["neg"]

# Print Analysis
print(target_string)
print("Compound Score: %s" % compound)
print("Positive Score: %s" % pos)
print("Neutral Score: %s" % neu)
print("Negative Score: %s" % neg)
