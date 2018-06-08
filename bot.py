import praw
import pdb
import re
import os
import sys



if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
       posts_replied_to = f.read()
       posts_replied_to = posts_replied_to.split("\n")
       posts_replied_to = list(filter(None, posts_replied_to))
def reddit(sub, fil):
	reddit = praw.Reddit('bot1')
	subreddit = reddit.subreddit(sub)
	if fil == "top":
		list = subreddit.top(limit=10)
	elif fil == "hot": 
		list = subreddit.hot(limit=10)
	for submission in list:
		posts_replied_to.append(submission.title+"-"+str(submission.score)+"\n"+str(submission.url))
	with open("topposts.txt", "w") as f:
		for post in posts_replied_to:
			f.write(post + "\n")
def main():	
	sub = input("subreddit? ")
	fil = input("top/hot? ")
	reddit(sub,fil)
if __name__ == '__main__':
  main()
