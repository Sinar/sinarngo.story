from five import grok
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from z3c.formwidget.query.interfaces import IQuerySource

class StoryType(grok.GlobalUtility):
    grok.name('sinarngo.story.storytype')
    grok.implements(IVocabularyFactory)

    _terms = [
        {
        'value': 'update',
        'title': 'Update',
        },
        {
        'value': 'news',
        'title': 'News',
        },
        {
        'value': 'story',
        'title': 'Story',
        },
        ]

    def __call__(self, context):
        terms = []
        for i in self._terms:
            terms.append(SimpleTerm(**i))
        return SimpleVocabulary(terms)
