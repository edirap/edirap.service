from five import grok
from plone.directives import dexterity, form
from edirap.service.content.service import IService

grok.templatedir('templates')

class Index(dexterity.DisplayForm):
    grok.context(IService)
    grok.require('zope2.View')
    grok.template('service_view')
    grok.name('view')

