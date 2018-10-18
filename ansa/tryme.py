from ansa import Ansa

ansa_obj = Ansa()

print(ansa_obj.get_articles_by_category(ansa_obj.get_categories_list()[0]))
