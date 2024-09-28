"""

This file runs the program, asking for input, with imported functions from sentiment_analysis.
It does some exception handling to ensure there is proper input.
It will output a file.
"""

# Import the sentiment_analysis module

from sentiment_analysis import read_keywords, clean_tweet_text, read_tweets , calc_sentiment , classify, make_report, write_report


def main():
    try:
        # ask user for keyword file name
        keywords = input("Input keyword filename (.tsv file): ")

        if not keywords.endswith(".tsv"):
            raise Exception("Must have tsv file extension!")

    except Exception as exceptobj:
        import traceback
        traceback.print_exc()

    try: # get the keywords from file and turn into dictionary
        words = read_keywords(keywords)

        if words == {}:
            raise Exception("Tweet list or keyword dictionary is empty!")

    except Exception as e:
        import traceback
        traceback.print_exc()

    try: #input file name to read tweets from
        tweets = input("Input tweet filename (.csv file): ")

        if not tweets.endswith(".csv"):
            raise Exception("Must have csv file extension!")
    except Exception as exp:
        import traceback
        traceback.print_exc()

    try: # turn each tweet into a dictionary
        tweets_list = read_tweets(tweets)

        if tweets_list == []:
            raise Exception("Tweet list or keyword dictionary is empty!")

    except Exception as exc:
        import traceback
        traceback.print_exc()

    try: #input file name to write report to
        report_name = input("Input filename to output report in (.txt file): ")

        if not report_name.endswith(".txt"):
            raise Exception("Must have txt file extension!")

        # write a report dictionary based on sentiments for tweets
        report_tweets = (make_report(tweets_list, words))
        write_report(report_tweets, report_name)
    except Exception as ex:
        import traceback
        traceback.print_exc()

main()
