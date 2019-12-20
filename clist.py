from requests import get
from bs4 import BeautifulSoup
from post import Post

def read_posts(url_filename):

    posts_file = open(url_filename, "r")
    post_urls = posts_file.readlines()
    posts = []

    for post_url in post_urls:
        # remove new line from URL
        post_url = post_url.rstrip('\n')
        response = get(post_url) # HTTP GET for c.l. post

        # extract HTML from page
        html_soup = BeautifulSoup(response.text, 'html.parser')
        
        # get post title
        post_title = html_soup.h2.span.find("span", {"id":"titletextonly"}).text
        
        # get post price
        post_price = html_soup.h2.span.find("span", {"class": "price"}).text

        # get post date and time
        post_datetime = html_soup\
            .find("p", {"class": "postinginfo reveal"})\
            .find("time", {"class": "date timeago"})\
            .text

        # separate date and time
        datetime_list = post_datetime.split(' ') # split string on spaces
        datetime_list.remove('\n') # remove all lone newline chars
        # remove all empty strings from the list  
        while '' in datetime_list:
            datetime_list.remove('')
        # remove all newline characters that may succede the date or time
        for i in range(len(datetime_list)):
            datetime_list[i] = datetime_list[i].rstrip() 
        # get date
        post_date = datetime_list[0]
        # get time
        post_time = datetime_list[1]

        # instantiate post object and append it to the list
        posts.append(Post(post_title, post_price, post_date, post_time))

    return posts

def display_posts(posts_list):
    print("-"*80)
    for post in posts_list:
        # display the post
        post.display()
        print("-"*80)
        


if __name__ == "__main__":
   posts_objs = read_posts('posts.txt')
   display_posts(posts_objs)
