from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField


class GenrePage(Page):
    parent = models.ForeignKey("GenrePage", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    content_panels = Page.content_panels + [
        FieldPanel('parent'),
    ]

    parent_page_types = ['GenresPage']


class AuthorPage(Page):
    name = models.CharField(max_length=255, blank=False, null=False)
    en_name = models.CharField(max_length=255, blank=True, null=True, verbose_name="english name")
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    short_description = models.TextField(blank=True)
    biography = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('en_name'),
        FieldPanel('image'),
        FieldPanel('short_description'),
        FieldPanel('biography', classname="full"),
    ]

    def __str__(self):
        return self.name

    parent_page_types = ['AuthorsPage']


class PublicationPage(Page):
    name = models.CharField(max_length=255, blank=False, null=False)
    logo = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('logo'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.title

    parent_page_types = ['PublicationsPage']


class BookPage(Page):
    author = ParentalKey(AuthorPage, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")
    translator = ParentalKey(AuthorPage, on_delete=models.SET_NULL, null=True, blank=True, related_name="tranlations")
    publication = ParentalKey(PublicationPage, on_delete=models.SET_NULL, null=True, blank=True, related_name="books")
    description = RichTextField(blank=True)
    cover_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True, blank=True, related_name='+'
    )
    genres = ParentalManyToManyField(GenrePage, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('translator'),
        FieldPanel('publication'),
        FieldPanel('description', classname="full"),
        FieldPanel('cover_image'),
        FieldPanel('genres')
    ]

    def __str__(self):
        return self.title


    parent_page_type = ["BooksPage"]

class GenresPage(Page):
    def __str__(self):
        return self.title

    content_panels = Page.content_panels
    max_count = 1

    parent_page_types = ['home.HomePage']
    subpage_types = ['GenrePage']


class AuthorsPage(Page):
    def __str__(self):
        return self.title

    content_panels = Page.content_panels
    max_count = 1

    parent_page_types = ['home.HomePage']
    subpage_types = ['AuthorPage']


class PublicationsPage(Page):
    def __str__(self):
        return self.title

    content_panels = Page.content_panels
    max_count = 1

    parent_page_types = ['home.HomePage']
    subpage_types = ['PublicationPage']


class BooksPage(Page):
    def __str__(self):
        return self.title

    content_panels = Page.content_panels
    max_count = 1

    parent_page_types = ['home.HomePage']
    subpage_types = ['BookPage']

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        genre_page = GenresPage.objects.get()
        genres = genre_page.get_children()
        context['genres'] = genres
        return context
