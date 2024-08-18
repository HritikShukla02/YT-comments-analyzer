from YouTube import *
import pandas
from sentiment_analyser import *


def comment_cat(sentiment):
    if sentiment <= -0.5:
        cat = "very Negative"
    elif sentiment <= -0.2:
        cat = "Negative"
    elif sentiment <= 0.2:
        cat = "Moderate"
    elif sentiment <= 0.5:
        cat = "Positive"
    else:
        cat = "Very Positive"
    return cat


def run_choice():
    while True:
        ch = input("Would you like to run again?(y/n): ")
        if ch == "y":
            return True
        elif ch == "n":
            print("Thank you!!")
            return False
        else:
            print("Wrong Input⚠️⚠️⚠️")
run = True
while run:
    link = input("Paste the link to YouTube Video: ")

    video_id = get_video_id(link=link)

    print("Getting comments from the video⌚⌚⌚")
    comments = get_comments(vid_id=video_id)
    # print(comments.head())
    # print(comments.index)

    print("Analysing Comment's Sentiments🚀🚀🚀")
    for ind in comments.index:
        comment = comments.loc[ind, "comment"]
        analysis = sentiment_analyzer(comment)
        comments.loc[ind, "comment_polarity"] = float(analysis[0])
        comments.loc[ind, 'comment_subjectivity'] = float(analysis[1])


    comments.sort_values(by='likes', ascending=False,inplace=True, ignore_index=True)


    print("Categorising Comment's Sentiments🚀🚀🚀")
    for ind in comments.index:
        comments.loc[ind, 'sentiment_cat'] = comment_cat(comments.loc[ind, "comment_polarity"])

    print("Generating Output CSV file🗃️🗃️🗃️")
    comments.to_csv("comments.csv")

    print("\n\n")
    print("Presenting Final Summary👉👉👉")

    print("\n\nGroup Analysis by Sentiment Category for comment Polarity: ")
    print(comments[['sentiment_cat', "comment_polarity"]].groupby(by='sentiment_cat').describe())

    print("\n\nGroup Analysis by Sentiment Category for comment Subjectivity: ")
    print(comments[['sentiment_cat', "comment_subjectivity"]].groupby(by='sentiment_cat').describe())


    print("\n\nOverall Analysis:")
    comment_summary = comments[['sentiment_cat', "comment_polarity", "comment_subjectivity"]]
    print(comment_summary.describe())

    run = run_choice()



