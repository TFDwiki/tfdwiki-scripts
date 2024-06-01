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

# TODO: I'm not sure if manual uploads or the UploadRobot is the better approach here
#def upload_file(filename, description):
#    file_page = pywikibot.FilePage(site, filename)
#    file_page.text = description
#    file_page.upload(filename, ignore_warnings=False)



image_path = r'C:\workspace\tfd\Assets\test_image.png'
target_filename = 'TestImage.png'
description = 'Ignore Me'

# Create the UploadRobot object
bot = UploadRobot([image_path],
                  description=description,
                  useFilename=target_filename,
                  keepFilename=True,
                  verifyDescription=False,
                  targetSite=site)

# Start the upload process
bot.run()