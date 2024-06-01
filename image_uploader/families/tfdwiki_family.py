from pywikibot import family


class Family(family.Family):
    name = 'tfdwiki'
    langs = {
        'en': 'www.tfd.wiki',
    }
    def version(self, code):
        return "1.41.1"  # The MediaWiki version used.

    def scriptpath(self, code):
        return ''
    