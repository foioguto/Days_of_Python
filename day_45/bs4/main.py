from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find(name="a", class_="storylink")


article_texts = []
article_links = []
for article in articles:
    text = articles.getText()
    article_texts.append(text)
    link = articles.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)




# import lxml


# with open("day_45/bs4/website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title.string)

# x = soup.find_all(name="a")
# # print(x)

# for tag in x:
#     print(tag.getText())

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
