from bs4 import BeautifulSoup
import requests

NEWS_URL = "https://news.ycombinator.com/"

response = requests.get(NEWS_URL)
# print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select(".athing .titlelink")
print(titles)




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