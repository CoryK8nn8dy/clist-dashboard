from requests import get
from json import loads
from bs4 import BeautifulSoup

posts_file = open("posts.txt", "r")
post_urls = posts_file.readlines()

for post_url in post_urls:
    # remove new line
    post_url = post_url.rstrip('\n')
    response = get(post_url) # HTTP GET for c.l. post
    # extract HTML from page
    # start with post title
    html_soup = BeautifulSoup(response.text, 'html.parser')
    post_body = html_soup.body.article.section.find(
            "div", {"class": "posting"}
            ) # find body of c.l. post
    post_title = post_body.h2.span.find("span", {"id": "titletextonly"}).text
    print(post_title)

    # get post price
    print(post_body.h2.span.find("span", {"class": "price"}).text)

    # get post date
    print(type(post_body.find(
        "p", {"class": "postinginfo reveal"}
        ).find(
        "time", {"class": "date timeago"}.string
        ))
    )
