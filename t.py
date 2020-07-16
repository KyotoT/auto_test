# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup

# アクセスするURL
url = "https://www.nikkei.com/markets/kabu/"

# URLにアクセスする 戻り値にはアクセスした結果やHTMLなどが入ったinstanceが帰ってきます
instance = urllib2.urlopen(url)

# instanceからHTMLを取り出して、BeautifulSoupで扱えるようにパースします
soup = BeautifulSoup(instance, "html.parser")

# CSSセレクターを使って指定した場所のtextを表示します
print soup.select_one("#CONTENTS_MARROW > div:nth-child(1) > div.cmn-headline_news > div.cmn-article_title > h4 > a > span").text
