# 🐍 + 🗞 = PyAnsa
[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/italynews/pyansa/blob/master/LICENSE)
[![Open Source Love png3](https://badges.frapsoft.com/os/v3/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

Our API ansa

## Install requirements
```sh
pip install -r requirements.txt
```
## How to
### Start
```py
from ansa import Ansa

ansa = Ansa()
```

### Retrieve all categories
```py
ansa.get_categories_list()
>>> ['homepage', 'cronaca', 'politica', 'mondo', 'economia', 'calcio', 'sport', 'cinema', 'cultura', 'tecnologia', 'ultimaora', 'englishnews', 'foto', 'video', 'abruzzo', 'basilicata', 'calabria', 'campania', 'emilia-Romagna', 'friuli-venezia-giulia', 'lazio', 'liguria', 'lombardia', 'marche', 'molise', 'piemonte', 'puglia', 'sardegna', 'sicilia', 'toscana', 'trentino-alto-adige', 'umbria', 'valle-aosta', 'veneto']
```


### Article manipulation
```py
ansa.get_articles_by_category('homepage')
>>> [article_list]
ansa.get_article_by_title('mytitle', 'homepage')
>>> [article]

ansa.read_article('article_url')
>>> { "title" : "value",
      "text" : "value",
      "image" : "value",  # <-  retrieved by ansa site
      ... other article fields...
    }
```

### Retrieve article by field
```py
ansa.get_article('myfield', 'myvalue', 'mycategory')
>>> [article]
```
With this method, you can filter articles by any field

## Develop on this
```sh
pip install -r requirements-dev.txt
pytest -s --cov
```
