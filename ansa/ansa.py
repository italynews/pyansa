import feedparser

from constant import LINKS, CATEGORIES
from exceptions import (InvalidCategoryException, InvalidArticleFieldException)


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
        pass
