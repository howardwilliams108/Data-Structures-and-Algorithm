from bridges.bridges import Bridges
from bridges.data_src_dependent.data_source import DataSource


bridges = Bridges(0, "YOUR_USERNAME", "YOUR_API_KEY")


ds = DataSource()

# Retrieve Shakespeare works
works = ds.get_shakespeare_data()

# Select one work
play = works[0]

print("Title:", play.title)
print()

# Get the text
text = play.text

# Remove punctuation
text = text.lower()

for ch in ",.;:!?()[]{}\"'-":
    text = text.replace(ch, " ")

# Split into words
words = text.split()

# Dictionary
frequency = {}

# Recursive function
def count_words(words, index, freq):

    # Base Case
    if index == len(words):
        return

    word = words[index]

    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1

    # Recursive Call
    count_words(words, index + 1, freq)

# Start recursion
count_words(words, 0, frequency)

# Sort by frequency
sorted_words = sorted(
    frequency.items(),
    key=lambda item: item[1],
    reverse=True
)

print("Top 20 Words")
print("--------------------")

for word, count in sorted_words[:20]:
    print(word, ":", count)

from bridges.bridges import Bridges
from bridges.data_src_dependent.data_source import reddit_data
from datetime import datetime
import matplotlib.pyplot as plt




bridges = Bridges(4, "howardwilliams108", "1628069107419")



posts = reddit_data("askscience")



if len(posts) == 0:
    print("No Reddit posts were retrieved from the site.")
    raise SystemExit


print("Number of posts retrieved include:", len(posts))




def print_post(post):
   

    readable_time = datetime.fromtimestamp(post.post_time)
    #Displaying information for a Reddit post
    print("Title of post:", post.title)
    print("Author of the post:", post.author)
    print("Score of the post:", post.score)
    print("Vote ratio of the post:", post.vote_ratio)
    print("Comment count of post:", post.comment_count)
    print("Post time of post:", readable_time)
    print("-" * 70)




total_score = 0
total_comments = 0

# this ensures that the the first post is assumed to be the highest and lowest in order for program to work properly
highest_score_post = posts[0]
lowest_score_post = posts[0]

most_comments_post = posts[0]
fewest_comments_post = posts[0]



for post in posts:

    
    total_score += post.score
    total_comments += post.comment_count

    
    if post.score > highest_score_post.score:
        highest_score_post = post

   
    if post.score < lowest_score_post.score:
        lowest_score_post = post

    
    if post.comment_count > most_comments_post.comment_count:
        most_comments_post = post

    
    if post.comment_count < fewest_comments_post.comment_count:
        fewest_comments_post = post


average_score = total_score / len(posts)
average_comments = total_comments / len(posts)



print("The Data Aggression from Reddit")
print("$" * 20)

print(f"The Average score is: {average_score:.2f}")
print(f"Average comment count: {average_comments:.2f}")


print("\nPost with the hightest score")
print_post(highest_score_post)


print("\nPost with the lowest score")
print_post(lowest_score_post)


print("Post with the most comments")
print_post(most_comments_post)


print("Post with the fewest comments")
print_post(fewest_comments_post)




high_vote_posts = []
medium_vote_posts = []
low_vote_posts = []


for post in posts:

    
    if post.vote_ratio > 0.8:
        high_vote_posts.append(post)

    
    elif post.vote_ratio >= 0.5:
        medium_vote_posts.append(post)

    
    else:
        low_vote_posts.append(post)



print("VOTE-RATIO CATEGORIES")
print("$" * 20)

print("High vote-ratio posts:", len(high_vote_posts))
print("Medium vote-ratio posts:", len(medium_vote_posts))
print("Low vote-ratio posts:", len(low_vote_posts))



posts_with_ten_comments = []


for post in posts:

   # keeping posts with at least 10 comments only
    if post.comment_count >= 10:
        posts_with_ten_comments.append(post)


print(" $" * 20)
print("Posts with 10 or more comments")
print("=" * 20)

print("Number of qualifying posts:", len(posts_with_ten_comments))


for post in posts_with_ten_comments:
    print("\nTitle:", post.title)
    print("Score:", post.score)
    print("Comments:", post.comment_count)




author_name = input( "\nEnter the Reddit author whose posts you want to find: ").strip()

author_posts = []


for post in posts:

    # lower() allows the capitalization of the name  to be ignored.
    if post.author.lower() == author_name.lower():
        author_posts.append(post)


print("\n" + "=" * 70)
print("Posts from the author:", author_name)
print("=" * 70)


if len(author_posts) == 0:
    print("No posts from that author were found in this dataset.")

else:
    for post in author_posts:
        print("\nTitle:", post.title)
        print("Score:", post.score)
        print("Comments:", post.comment_count)




earliest_post = posts[0]
latest_post = posts[0]


for post in posts:

    #  smaller timestamp would represent an earlier time.
    if post.post_time < earliest_post.post_time:
        earliest_post = post

    #  larger timestamp would represent a later time.
    if post.post_time > latest_post.post_time:
        latest_post = post



print("Post Time Analysis")



print("\nEARLIEST POST")
print_post(earliest_post)


print("\nLATEST POST")
print_post(latest_post)


# this would return the posts that were ordered by comment count.
sorted_posts = sorted(posts,key=lambda post: post.comment_count,
    reverse=True # this would place largest comment count first
)



top_ten_posts = sorted_posts[:10]


titles = []
comment_counts = []


for post in top_ten_posts:

   # this would ensure that chart is readable enough when the program runs, it would shorten the title enough
    if len(post.title) > 40:
        short_title = post.title[:40] + "..."
    else:
        short_title = post.title

    titles.append(short_title)
    comment_counts.append(post.comment_count)


plt.figure(figsize=(12, 7))

#Thus produces a horizontal bar chart
plt.barh(titles, comment_counts)

plt.xlabel("Number of Comments in the Reddit Chat")
plt.ylabel("Reddit Post Title")
plt.title("Top 10 AskScience Posts with the Most Comments")


plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()