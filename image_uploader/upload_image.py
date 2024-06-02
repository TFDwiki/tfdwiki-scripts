import os

import pywikibot
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

description = """== Licensing ==
{{From NEXON}}
"""

directory = r'C:\workspace\tfd\test'

for filename in os.listdir(directory):
    if not filename.endswith('.png'):
        continue

    file_path = os.path.join(directory, filename)
    file_size = os.path.getsize(file_path)

    # Placeholder assets are very small files. Ignore these.
    if file_size < 200:
        print("Skipping " + filename)
        continue

    print("Uploading " + filename)
    bot = UploadRobot([file_path],
                      description=description,
                      use_filename=filename,
                      keep_filename=True,
                      verify_description=False)
    bot.run()
