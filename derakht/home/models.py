from django.db import models
from django.forms import CheckboxSelectMultiple
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import PageChooserBlock
from wagtail.fields import RichTextField

from wagtail.models import Page

from books.models import Book


class HomePage(Page):
    body = RichTextField(blank=True)
    featured_books = ParentalManyToManyField(Book, blank=True)
    genre= PageChooserBlock(required=False)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        # FieldPanel('genre', classname="full"),
        FieldPanel('featured_books', widget=CheckboxSelectMultiple),
    ]

    def __str__(self):
        return self.title