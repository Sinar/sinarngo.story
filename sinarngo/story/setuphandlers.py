from collective.grok import gs
from sinarngo.story import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.story', 
    title=_('sinarngo.story import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.story.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
