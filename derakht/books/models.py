from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, PageChooserPanel
from wagtail.models import Page
from wagtail.fields import RichTextField


class Genre(Page):
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        PageChooserPanel('parent', self),
    ]

    parent_page_types = ['Genre']
    subpage_types = ['Genre']

    def __str__(self):
        return self.title


class Book(Page):
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    description = RichTextField(blank=True)
    cover_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('publication_date'),
        FieldPanel('description', classname="full"),
        FieldPanel('cover_image'),
    ]

    parent_page_types = ['Genre']
    subpage_types = []

    def __str__(self):
        return self.title


class BookPage(Page):
    book_of_page = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True, blank=True, related_name='+')
    summary = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('slug'),
            FieldPanel('book_of_page'),
            FieldPanel('summary', classname="full"),
        ], heading="Book Information"),
    ]

    parent_page_types = ['Genre']
    subpage_types = []

    def __str__(self):
        return self.title
