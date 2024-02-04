from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail import blocks
from wagtailcodeblock.blocks import CodeBlock


class BlogIndexPage(Page):
    intro = RichTextField()

    content_panels = Page.content_panels + [FieldPanel("intro")]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context


class BlogPage(Page):
    date = models.DateField(verbose_name="Date de publication")
    intro = RichTextField()
    body = StreamField([
        ("paragraphe", blocks.RichTextBlock()),
        ("code", CodeBlock()),
    ], use_json_field=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return {
                'image': gallery_item.image,
                'caption': gallery_item.caption
            }
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel("date"),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Gallerie d'images")
        ]


class BlogPageGallery(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name="gallery_images")
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE)
    caption = models.CharField(blank=True, max_length=250)
    panels = [
        FieldPanel('image'),
        FieldPanel('caption')
    ]
