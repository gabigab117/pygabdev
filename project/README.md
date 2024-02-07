# PyGabDev

## Introduction

For this project, I used Django, Wagtail, and Bootstrap. This is my personal platform. I chose to combine the power of
Django and Wagtail because I am familiar with Django and I enjoy using Wagtail for the editing/CMS part.

## Prerequisites

### requirements.txt

```
anyascii==0.3.2
asgiref==3.7.2
beautifulsoup4==4.11.2
certifi==2024.2.2
charset-normalizer==3.3.2
crispy-bootstrap5==2023.10
defusedxml==0.7.1
Django==5.0.1
django-crispy-forms==2.1
django-environ==0.11.2
django-extensions==3.2.3
django-filter==23.5
django-modelcluster==6.2.1
django-permissionedforms==0.1
django-recaptcha==4.0.0
django-taggit==4.0.0
django-treebeard==4.7.1
djangorestframework==3.14.0
draftjs-exporter==2.1.7
et-xmlfile==1.1.0
filetype==1.2.0
html5lib==1.1
idna==3.6
l18n==2021.3
laces==0.1.0
openpyxl==3.1.2
pillow==10.2.0
pillow-heif==0.14.0
pytz==2024.1
requests==2.31.0
six==1.16.0
soupsieve==2.5
sqlparse==0.4.4
telepath==0.3.1
urllib3==2.2.0
wagtail==6.0
wagtailcodeblock==1.29.0.1
webencodings==0.5.1
Willow==1.6.3
```

### settings.py

I added constants in my settings file to manage Crispy Forms, reCAPTCHA and the mail server.

But you need to add your site to Google reCAPTCHA: https://www.google.com/recaptcha/admin/create, choose reCAPTCHA v2
and add the domain 127.0.0.1 for it to work locally.

For recaptcha in dev : Test Keys

```
# Recaptcha
SILENCED_SYSTEM_CHECKS = ['django_recaptcha.recaptcha_test_key_error']
RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
```

## Landing App

This is the index of my web application. I use a Wagtail model.

## Blog App

Here are two models. The BlogIndexPage with its child BlogPage. I have also integrated an image gallery with BlogPage. I
use Wagtail models.

## Folio App

I use the same architecture as Blog. ProjectIndex, ProjectPage, image gallery. And ... more Wagtail.

# Search App

I use the Wagtail search system. To be clearer:
```
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
```

It is important not to forget the command `python manage.py update_index` ...
