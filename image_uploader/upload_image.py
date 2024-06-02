import pywikibot
from pywikibot import pagegenerators
from pywikibot import family
from pywikibot.specialbots import UploadRobot



class Family(family.Family):
    name = 'tfdwiki'
    langs = {
        'en': 'www.tfd.wiki',
    }
    def version(self, code):
        return "1.41.1"

    def scriptpath(self, code):
        return ''

site = pywikibot.Site('en', Family())
site.login('ImageBot')
repo = site.data_repository()

image_path = r'C:\workspace\tfd\Assets\test_image2.png'
target_filename = 'test_image2.png'
description = """== Licensing ==
{{From NEXON}}
"""

# Create the UploadRobot object
bot = UploadRobot([image_path],
                  description=description,
                  use_filename=target_filename,
                  keep_filename=True,
                  verify_description=False)

# Start the upload process
bot.run()