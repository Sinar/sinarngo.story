from five import grok
from plone.directives import dexterity, form
from sinarngo.story.content.story import IStory

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IStory)
    grok.require('zope2.View')
    grok.template('story_view')
    grok.name('view')

