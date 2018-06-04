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
def reddit(sub):
	reddit = praw.Reddit('bot1')
	subreddit = reddit.subreddit(sub)
	for submission in subreddit.top(limit=10):
		posts_replied_to.append(submission.title+"\t"+str(submission.score))
			# if re.search("i love python", submission.title, re.IGNORECASE):
			# 	submission.reply("Botty bot says: Me too!!")
			# 	print("Bot replying to : ", submission.title)
	with open("topposts.txt", "w") as f:
		for post_id in posts_replied_to:
			f.write(post_id + "\n")
def main():
  reddit(sys.argv[1])
if __name__ == '__main__':
  main()
