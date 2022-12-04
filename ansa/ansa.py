import feedparser

from .constant import LINKS, CATEGORIES, BASE_URL
from .exceptions import (InvalidCategoryException, InvalidArticleFieldException)
from .utils import simple_get
from bs4 import BeautifulSoup


class Ansa():
    def get_article(self, field, value, category):
        articles = self.get_articles_by_category(category)
        article_list = []
        for article in articles:
            if field in article:
                if article[field] == value:
                    article_list.append(article)
            else:
                raise InvalidArticleFieldException(
                    'Field not allowed, did you mean one of ' +
                    str(list(article.keys())))
        return article_list

    def get_articles_by_category(self, category):
        alpha = None
        if category in CATEGORIES:
            alpha = LINKS[category]
        else:
            raise InvalidCategoryException(
                'Category not allowed, did you mean one of ' + str(CATEGORIES)
            )
        parser = feedparser.parse(alpha)
        return parser.entries

    def get_article_by_title(self, title, category):
        return get_article('title', title, category)

    def get_categories_list(self):
        return CATEGORIES

    def read_article(self, article_url):
        raw_html = simple_get(article_url)
        html = BeautifulSoup(raw_html, 'html.parser')
        article = {}
        for elem in html.find_all('div', attrs={"class": "news-txt"}):
            text = str(elem.text).replace(u'\xa0', u' ')
            if "text" in article:
                article["text"] = article["text"].append(text)
            else:
                article["text"] = text
        summary = html.find('h2', attrs={"class": "news-stit"})
        article["summary"] = summary.text
        title = html.find('h1', attrs={"class": "news-title"})
        article["title"] = title.text
        div_of_image = html.find('div', attrs={'class': 'img-photo'})
        image = div_of_image.next_element.next_element
        article["image"] = {'src': BASE_URL+image['src'], 'alt': image['alt']}
        return article
