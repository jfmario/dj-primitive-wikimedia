
from django.conf.urls import url
from primitive_wikimedia.views import main

URLS = [
    url ( r'^$', main ),
    url ( r'(?P<page_number>[0-9]+)$', main )
]
