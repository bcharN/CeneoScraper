from types import NoneType
import requests 
import json
from bs4 import BeautifulSoup as bs



product_num="91714422"
product_num=int(input("enter product number: "))
url = "https://www.ceneo.pl"+"/"+product_num
while(url):
    response = requests.get(url)


    page = bs(response.text,"html.parser")

    opinions = page.find_all("div",class_="js_product-review")
    all_opinions =[]
    #opinion = opinions.pop(0)
    for opinion in opinions:
        opinion_id = opinion["data-entry-id"]
        author = opinion.select_one("span.user-post__author-name").get_text().strip()
        try:
            recommendation = opinion.select_one("span.user-post__author-recomendation > em").get_text().strip()
        except AttributeError:
            recommendation = None
        stars = opinion.select_one("span.user-post__score-count").get_text().strip()
        content = opinion.select_one("div.user-post__text").get_text().strip()

        useful = opinion.select_one("button.vote-yes > span").get_text().strip()
        useless = opinion.select_one("button.vote-no > span").get_text().strip()
        publish_date = opinion.select_one("span.user-post__published > time:nth-child(1)")["datetime"]
        try:
            purchase_date = opinion.select_one("span.user-post__published > time:nth-child(2)")["datetime"]
        except TypeError:
            purchase_date = None
        pros = opinion.select("div[class$=\"positives\"] ~ div.review-feature__item")
        pros = [item.get_text().strip() for item in pros]

        cons = opinion.select("div[class$=\"negatives\"]~ div.review-feature__item")
        cons = [item.get_text().strip() for item in cons]

        single_opinion = {
            "opinion_is" : opinion_id,
            "author" : author,
            "recommendation" : recommendation,
            "stars" : stars,
            "content" : content,
            "uesful" : useful,
            "uesless" : useless,
            "publish_date" : publish_date, 
            "purchase_date" : purchase_date,
            "pros" : pros,
            "cons" : cons,

        }
        all_opinions.append(single_opinion)
    try:
        url = "https://www.ceneo.pl"+page.select_one("a.pagination__next")["href"]
    except TypeError:
        url = None

with open("opinions/"+product_num +".json","w",encoding="UTF-8") as jf:
    json.dump(all_opinions,jf,indent=4,ensure_ascii=False)


#kod produktu od użytkownika
# commit -a -m "homework BC"
