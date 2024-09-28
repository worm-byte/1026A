"""

This file has multiple functions that make a keyword dictionary,
cleans the tweets, calculates the sentiment and classifies it,
reads the tweets and turns each into a dictionary, makes a report
on the tweets and writes the output to a file.
"""

#takes words and sentiment value from a file and returns a dictionary
def read_keywords(keyword_file_name):
    keywords = {}
    try:
        infile = open(keyword_file_name, 'r')
        line = infile.readline()
        while line != "":
            line = line.strip()
            line = line.rsplit("\t",2)
            keywords[line[0]] = int(line[1])
            line = infile.readline()
        infile.close()
    except IOError:
        print(f"Could not open file {keyword_file_name}!")
    return keywords

#clean up the tweet from string input removing everything but alphabet letters and spaces and return modified string
def clean_tweet_text(tweet_text):
    tweet = ""
    for letter in tweet_text:
        if letter.isalpha():
            tweet += letter
        elif letter == " ":
            tweet += " "
    tweet = tweet.lower()
    return tweet

#using modified tweet text and keyword dictionary, calculate the sentiment value of a tweet and return integer
def calc_sentiment(tweet_text, keyword_dict):
    tweet_text = tweet_text.split()
    value = 0
    for word in tweet_text:
        if word in keyword_dict:
            value += keyword_dict[word]
    return value

#using sentiment value, classify tweet as positive, neutral, or negative, return string
def classify(score):
    value = ""
    if score > 0:
        value = "positive"
    elif score == 0:
        value = "neutral"
    elif score < 0:
        value = "negative"
    else:
        print("Could not classify sentiment value.")
    return value

#input tweets from a file and turn each into a dictionary, return a list of dictionaries
def read_tweets(tweet_file_name):
    tweets_list = []
    try:
        infile = open(tweet_file_name, 'r')
        line = infile.readline()
        tweet_dict = {}
        while line != "":
            line = line.strip()
            line = line.rsplit(",", 9)
            tweet_text = line[0].split(",", 2)
            tweet_dict["city"] = line[7]
            tweet_dict["country"] = line[5]
            tweet_dict["date"] = tweet_text[0]
            tweet_dict["favorite"] = int(line[3])
            tweet_dict["lang"] = line[4]
            if line[8] == "NULL":
                tweet_dict["lat"] = "NULL"
            else:
                tweet_dict["lat"] = float(line[8])

            if line[9] == "NULL":
                tweet_dict["lon"] = "NULL"
            else:
                tweet_dict["lon"] = float(line[9])

            tweet_dict["retweet"] = int(line[2])
            tweet_dict["state"] = line[6]
            tweet_dict["text"] = clean_tweet_text(tweet_text[1])
            tweet_dict["user"] = line[1]
            tweets_list.append(tweet_dict)
            tweet_dict = {}
            line = infile.readline()
        infile.close()
    except IOError:
        print(f"Could not open file {tweet_file_name}!")
    return tweets_list

#using list of tweets and keyword dictionary, do analysis of tweets and return a dictionary
def make_report(tweet_list, keyword_dict):
    report_dict = {}
    fav_sentiment_total = 0
    retweet_sentiment_total = 0
    sentiment_total = 0
    fav_counter = 0
    negative_counter = 0
    neutral_counter = 0
    positive_counter = 0
    retweet_counter = 0
    tweets_counter = 0
    country_dict = {}
    country_tweets = {}
    avg_country_dict = {}

    for tweet in tweet_list: #just a bunch of counters and sums mostly
        sentiment = calc_sentiment(tweet["text"],keyword_dict)
        sentiment_total += sentiment
        tweets_counter += 1

        if tweet["favorite"] > 0:
            fav_sentiment_total += sentiment
            fav_counter += 1

        if tweet["retweet"] > 0:
            retweet_sentiment_total += sentiment
            retweet_counter += 1

        sentiment_score = classify(sentiment)
        if sentiment_score == "positive":
            positive_counter += 1
        elif sentiment_score == "negative":
            negative_counter += 1
        else:
            neutral_counter += 1

        if tweet["country"] in country_dict:
            country_dict[tweet["country"]] += sentiment
            country_tweets[tweet["country"]] += 1
        else:
            country_dict[tweet["country"]] = sentiment
            country_tweets[tweet["country"]] = 1


    if fav_counter > 0: #start adding values to dictionary based on counters and sums
        report_dict["avg_favorite"] = round(fav_sentiment_total/fav_counter,2)
    else:
        report_dict["avg_favorite"] = "NAN"

    if retweet_counter > 0:
        report_dict["avg_retweet"] = round(retweet_sentiment_total / retweet_counter,2)
    else:
        report_dict["avg_retweet"] = "NAN"

    if tweets_counter > 0:
        report_dict["avg_sentiment"] = round(sentiment_total / tweets_counter,2)
    else:
        report_dict["avg_sentiment"] = "NAN"

    report_dict["num_favorite"] = fav_counter
    report_dict["num_negative"] = negative_counter
    report_dict["num_neutral"] = neutral_counter
    report_dict["num_positive"] = positive_counter
    report_dict["num_retweet"] = retweet_counter
    report_dict["num_tweets"] = tweets_counter

    if "NULL" in country_dict:
        country_dict.pop("NULL")

    if country_dict == {}:
        report_dict["top_five"] = "NAN"
    else: #sort the top 5 countries by avg sentiment
        for key in country_dict:
            if key in country_tweets:
                avg_country_dict[key] = country_dict[key]/country_tweets[key]

        swap = sorted(avg_country_dict.items(),key = lambda x:x[1], reverse = True)

        top_5 = dict(swap[0:5])

        countries = list(top_5.keys())

        report_dict["top_five"] = ", ".join(countries)
    return report_dict

#write a report from the report dictionary to an output file
def write_report(report, output_file):
    try:
        infile = open(output_file, 'w')
        infile.write(f"Average sentiment of all tweets: {report['avg_sentiment']}\n")
        infile.write(f"Total number of tweets: {report['num_tweets']}\n")
        infile.write(f"Number of positive tweets: {report['num_positive']}\n")
        infile.write(f"Number of negative tweets: {report['num_negative']}\n")
        infile.write(f"Number of neutral tweets: {report['num_neutral']}\n")
        infile.write(f"Number of favorited tweets: {report['num_favorite']}\n")
        infile.write(f"Average sentiment of favorited tweets: {report['avg_favorite']}\n")
        infile.write(f"Number of retweeted tweets: {report['num_retweet']}\n")
        infile.write(f"Average sentiment of retweeted tweets: {report['avg_retweet']}\n")
        infile.write(f"Top five countries by average sentiment: {report['top_five']}\n")
        infile.close()
        print("Wrote report to",output_file)
    except IOError:
        print(f"Could not open file {output_file}!")
