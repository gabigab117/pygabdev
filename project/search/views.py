from django.shortcuts import render

from wagtail.models import Page
from wagtail.contrib.search_promotions.models import Query


def search_view(request):
    """
        Processes the search requests submitted through the GET method by looking up the 'query' parameter.
        It performs a search across live pages in the Wagtail CMS and logs the search query for promoting results
        in future searches.

        If a search query is provided, it searches through the live pages using Wagtail's built-in search functionality,
        logs the query for future reference, and collects the search results. If no query is provided, it returns an
        empty queryset.

        Args:
            request (HttpRequest): The HTTP request object containing the search query.

        Returns:
            HttpResponse: The HTTP response object that renders the 'search/search.html' template, passing the search
            query and the search results.
        """
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)

        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    return render(request, 'search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
