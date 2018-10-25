import pytest

from ansa.exceptions import InvalidCategoryException, InvalidArticleFieldException
from ansa import Ansa
from requests.exceptions import ConnectionError

def test_exceptions_raises_InvalidCategoryException():
    ansa = Ansa()
    with pytest.raises(InvalidCategoryException) as excinfo:
        ansa.get_articles_by_category(category='owanesh')
    assert "Category not allowed, did you mean one of ['homepage', 'cronaca', 'politica', 'mondo', 'economia', 'calcio', 'sport', 'cinema', 'cultura', 'tecnologia', 'ultimaora', 'englishnews', 'foto', 'video', 'abruzzo', 'basilicata', 'calabria', 'campania', 'emilia-romagna', 'friuli-venezia-giulia', 'lazio', 'liguria', 'lombardia', 'marche', 'molise', 'piemonte', 'puglia', 'sardegna', 'sicilia', 'toscana', 'trentino-alto-adige', 'umbria', 'valle-aosta', 'veneto']" in str(
        excinfo.value)
