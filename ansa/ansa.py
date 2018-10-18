from .constant import LINKS, CATEGORIES
import feedparser


class Ansa():

    def get_articles(self, categoria):
        if categoria in CATEGORIES:
            category = LINKS[categoria]
        else:
            print("Io non esisto!")
            return
        parse_rss = feedparser.parse(category)
        return parse_rss.entries

    def get_item(self, title, category):
        article_list = self.get_articles(category)
        for n in article_list:
            if n.title == title:
                return n

    def get_categories_list(self, list):
        return CATEGORIES

    