from requests import get
from json import loads
from bs4 import BeautifulSoup

posts_file = open("posts.txt", "r")
post_urls = posts_file.readlines()

for post_url in post_urls:
    post_url = post_url.rstrip('\n')
    response = get(post_url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    post_body = html_soup.body.article.section.find("div", {"class": "posting"})
    post_title = post_body.h2.span.find("span", {"id": "titletextonly"}).text
    print(post_title)
