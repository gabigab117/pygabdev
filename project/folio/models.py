from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page, Orderable
from wagtail import blocks
from wagtail.search import index
from wagtailcodeblock.blocks import CodeBlock


class ProjectIndexPage(Page):
    intro = RichTextField()

    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        projects = ProjectPage.objects.child_of(self).live().order_by("-date")
        context['projects'] = projects
        return context


class ProjectPage(Page):
    date = models.DateField(verbose_name="Date de publication")
    intro = RichTextField()
    body = StreamField([
        ("paragraphe", blocks.RichTextBlock()),
        ("code", CodeBlock()),
    ], use_json_field=True)

    @property
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [index.SearchField("intro"), index.SearchField("body")]

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Gallerie d'images")
        ]


class ProjectPageGallery(Orderable):
    page = ParentalKey(ProjectPage, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE)
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldPanel('image'),
        FieldPanel('caption')
    ]
