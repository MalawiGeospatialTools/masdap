from django.db import models
from puput.models import EntryPage, BlogPage
from geonode.maps.models import Map

from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class MapEntryPage(EntryPage):
    map = models.ForeignKey(
        'maps.Map',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    content_panels = EntryPage.content_panels + [
        SnippetChooserPanel('map'),
    ]
BlogPage.subpage_types.append(MapEntryPage)
