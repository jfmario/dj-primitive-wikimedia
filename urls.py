
from django.conf.urls import url
from primitive_wikimedia.views import main_view

URLS = [
    url ( r'^$', main_view ),
    url ( r'(?P<page_number>[0-9]+)$', main_view )
]
