
from django.core.paginator import EmptyPage, Paginator
from django.template.response import TemplateResponse
from primitive_wikimedia.models import PrimitiveWikimediaEntry

def main ( request, page_number='1' ):

    data = {}

    page_number = int ( page_number )

    query = PrimitiveWikimediaEntry.objects.all ()
    entry_count = len ( query )

    pages = Paginator ( query, 16 )

    try:
        returned_page = pages.page ( page_number )
    except EmptyPage:
        returned_page = pages.page ( pages.num_pages )

    data ['entries'] = returned_page.object_list

    base_link = '/primitive-wikimedia/'

    if page_number != 1:
        data ['previous_page_link'] = base_link + str ( page_number - 1 )
    if entry_count > page_number * 16:
        data ['next_page_link'] = base_link + str ( page_number + 1 )
    return TemplateResponse ( request 'primitive_wikimedia/base.html', data )
