from bs4 import BeautifulSoup
import requests
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
body = response.text

soup = BeautifulSoup(body, "html.parser")
print(soup.prettify())

### method 1
# title_texts = soup.select(selector="h3.title")
# for idx in range(len(title_texts)-1, -1, -1):
#     print(title_texts[idx])
### method 2
# title_texts = soup.find_all('h3', class_ = "title")
# with open("./bs4_website/bs4_movies/Output.txt", "w", encoding="utf-8") as text_file:
#     for idx in range(len(title_texts)-1, -1, -1):
#         text = title_texts[idx].get_text()
#         text_file.write(f"{text}\n")
### method 3
title_texts = soup.find_all('h3', class_ = "title")
with open("./bs4_website/bs4_movies/Output3.txt", "w", encoding="utf-8") as text_file:
    text = [title.getText() for title in title_texts]
    text_file.write(f"{text[::-1]}\n")