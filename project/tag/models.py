from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from django.db import models
from wagtail.models import Page


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey("blog.BlogPage", on_delete=models.CASCADE, related_name="tagged_items")


class BlogTagIndexPage(Page):
    def get_context(self, request, *args, **kwargs):
        from blog.models import BlogPage
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)
        context = super().get_context(request, *args, **kwargs)
        context["blogpages"] = blogpages
        return context
