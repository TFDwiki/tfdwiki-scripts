import os

import pywikibot
from pywikibot.specialbots import UploadRobot

from family import Family


site = pywikibot.Site('en', Family())
site.login('BulkEdit')

