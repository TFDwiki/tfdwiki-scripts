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
                      verify_description=False,
                      ignore_warning=False)
    bot.run()

# Just a note, if you want to upload mp4 files, pywikibot doesn't seem to be pulling from the site's approved formats
# I couldn't figure out how to specify the site.file_extensions list to include other formats
# So my workaround was to just into the library and comment out the file type check
# Find your venv location:
# print(pywikibot.__file__)
# Then modify pywikibot\page\_filepage.py
# Comment out these lines:
# if not sep or extension.lower() not in self.site.file_extensions:
#    raise ValueError(
#        f'{title!r} does not have a valid extension '
#        f'({", ".join(self.site.file_extensions)}).'
#    )
# Then cry as you hack around a lack of documentation on how to do this correctly.
