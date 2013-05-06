from collective.grok import gs
from edirap.service import MessageFactory as _

@gs.importstep(
    name=u'edirap.service', 
    title=_('edirap.service import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('edirap.service.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
