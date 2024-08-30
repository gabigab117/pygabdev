# Generated by Django 5.0.2 on 2024-02-10 11:22

import django.db.models.deletion
import modelcluster.fields
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0092_query_searchpromotion_querydailyhits"),
        ("wagtailimages", "0025_alter_image_file_alter_rendition_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogIndexPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("intro", wagtail.fields.RichTextField()),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("date", models.DateField(verbose_name="Date de publication")),
                ("intro", wagtail.fields.RichTextField()),
                (
                    "body",
                    wagtail.fields.StreamField(
                        [
                            ("paragraphe", wagtail.blocks.RichTextBlock()),
                            (
                                "code",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "language",
                                            wagtail.blocks.ChoiceBlock(
                                                choices=[
                                                    ("bash", "Bash/Shell"),
                                                    ("css", "CSS"),
                                                    ("diff", "diff"),
                                                    ("html", "HTML"),
                                                    ("javascript", "Javascript"),
                                                    ("json", "JSON"),
                                                    ("python", "Python"),
                                                    ("scss", "SCSS"),
                                                    ("yaml", "YAML"),
                                                ],
                                                help_text="Coding language",
                                                identifier="language",
                                                label="Language",
                                            ),
                                        ),
                                        (
                                            "code",
                                            wagtail.blocks.TextBlock(
                                                identifier="code", label="Code"
                                            ),
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="BlogPageGallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                ("caption", models.CharField(blank=True, max_length=250)),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailimages.image",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gallery_images",
                        to="blog.blogpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]
