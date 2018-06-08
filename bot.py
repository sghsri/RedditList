import praw
import pdb
import re
import os
import sys

posts = []

def makelist(sub, fil, lim):
	reddit = praw.Reddit('bot1')
	subreddit = reddit.subreddit(sub)
	#use the correct filter and limit
	if fil == "top":
		list = subreddit.top(limit=lim)
	elif fil == "hot":
		list = subreddit.hot(limit=lim)
		#append the posts
	for submission in list:
		posts.append(submission.title+"-"+str(submission.score)+"\n"+str(submission.url)+"\n")
		#write to file
	with open("topposts.txt", "w") as f:
		for post in posts:
			f.write(post + "\n")
def main():	
	#let the user choose which subreddit,filter, and how many posts to make the list from
	sub = input("subreddit? ")
	fil = input("top/hot? ")
	lim = int(input("# of posts? "))
	makelist(sub,fil,lim)
if __name__ == '__main__':
  main()
