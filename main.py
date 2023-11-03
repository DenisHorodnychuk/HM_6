from bs4 import BeautifulSoup

with open("main.html") as file:
    soup = BeautifulSoup(file, "html.parser")

    for main_title in soup.select('h1.main-title'):
        print(main_title.text)

    for subtitle in soup.select('p.subtitle'):
        print(subtitle.text)

    for article_title in soup.select('article h2.article-title'):
        print(article_title.text)

    for article_text in soup.select('article p.article-text'):
        print(article_text.text)

    for footer_text in soup.select('footer p.footer-text'):
        print(footer_text.text)
