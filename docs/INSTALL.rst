edirap.service Installation
---------------------------

To install edirap.service using zc.buildout and the plone.recipe.zope2instance
recipe to manage your project, you can do this:

* Add ``edirap.service`` to the list of eggs to install, e.g.:

    [buildout]
    ...
    eggs =
        ...
        edirap.service

* Re-run buildout, e.g. with:

    $ ./bin/buildout

