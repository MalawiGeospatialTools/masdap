from django.conf import settings

from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible
from django.utils import six

from wagtail.wagtailcore.models import Page, PageBase
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailsearch import index
from taggit.models import TaggedItemBase, Tag as TaggitTag
from modelcluster.fields import ParentalKey

from puput.abstracts import EntryAbstract
from puput.utils import import_model, get_image_model_path
from puput.routes import BlogRoutes
from puput.managers import TagManager, CategoryManager, BlogManager

from puput.models import EntryPage, BlogPage
from geonode.maps.models import Map

register_snippet(Map)

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
