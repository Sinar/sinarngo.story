from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from sinarngo.story import MessageFactory as _


# Interface class; used to define content-type schema.

class IStory(form.Schema, IImageScaleTraversable):
    """
    Story Content
    """
    dexteritytextindexer.searchable('title')
    title = schema.TextLine(title=u'Title',
                            description=u'Title of Story.')

    dexteritytextindexer.searchable('description')
    description = schema.Text(title=u'Description',
                              description=u'Brief description '
                              'or summary of story.')

    dexteritytextindexer.searchable('Story details')
    body = RichText(title=u'Details of Story or Update')

    #Type (News, Update, Story)
    
    #Featured

    #Video Caption
    #Video URL
    #Video Embed
    #Relation to Gallery Folder

alsoProvides(IStory, IFormFieldProvider)
