from bs4 import BeautifulSoup
import requests

NEWS_URL = "https://news.ycombinator.com/"

response = requests.get(NEWS_URL)
# print(response.text)
web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')
# titles = soup.select(".titlelink")
articles = soup.find_all(name = "a", class_ = "titlelink") # ★
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_ = "score")]

print(len(article_texts))
print(len(article_links))
# print(sorted(article_upvotes))

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])


# for rank, upvoke in enumerate(article_upvokes):
##### sorted() makes these articles sorted in the highest upvotes.




# from bs4 import BeautifulSoup
# with open("./bs4_website/website.html", encoding='utf-8') as file:
#     contents = file.read()
#     # print(contents) 
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p) # the first
# # all_anchor_tags = soup.find_all(name = "a")
# # print(all_anchor_tags)
# # for tag in all_anchor_tags:
# #     print(tag.get("href"))
# # heading = soup.find(name="h1", id = "name")
# # print(heading)
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading.get("class"))
# company_url = soup.select_one(selector="p a")
# print(company_url)
# name = soup.select_one(selector="#name")
# print(name)
# headings = soup.select(".heading")
# print(headings)