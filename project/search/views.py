from django.shortcuts import render

from wagtail.models import Page
from wagtail.contrib.search_promotions.models import Query


def search_view(request):
    # Search
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
