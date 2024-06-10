# tfdwiki-scripts
 A collection of scripts used for managing stuff on the TFD wiki.

 Note that these scripts are not "ready-to-deploy". In all cases, the scripts in this repository are intended to be manually modified to suit a specific purpose, and then executed manually once. As such, you will find that the code may point to folders or resources not included in the various scripts.

## Getting Started
Automation scripts can be a very powerful tool, but you can also do a lot of damage to a lot of pages in a short amount of time. Please make sure you follow these instructions to get started.

### Join the Discord
Write access to the MediaWiki API is disabled for regular users. In order to gain write access, please [join our Discord](https://discord.gg/8TuKeeDp4h) so we can get you set up and provide you with any help you may need.

### Create both a regular and bot wiki accounts
Please create two accounts on the wiki: Your main account, and a second account with the word "Bot" at the end.

As a layer of safety, we compartmentalize API edits from regular user edits. It's easier to wipe a bot account's edits and not risk removing any content edits you as a person have made. This also protects your main account, should your bot account's password get committed to any repositories by accident.

## Pywikibot

These scripts all use [Pywikibot](https://www.mediawiki.org/wiki/Manual:Pywikibot?useskin=vector), a Python library designed for Wikipedia, but usable by all MediaWiki sites. It can be a bit confusing to get set up and running, especially since much of the documentation is oriented around Wikipedia, instead of being site-agnostic.

It is STRONGLY recommended you use the [user-config.py](https://www.mediawiki.org/wiki/Manual:Pywikibot/user-config.py?useskin=vector) method of storing credentials, instead of embedding your username and password directly into your script. This will safeguard your password from being committed by accident.

See [Install Pywikibot](https://www.mediawiki.org/w/index.php?title=Manual:Pywikibot/Installation&useskin=vector#Configure_Pywikibot) for instructions on getting set up. Refer to [this file](https://github.com/TFDwiki/tfdwiki-scripts/blob/master/image_uploader/families/tfdwiki_family.py) for how to compose the Family class for our wiki.

## Scripts in this repository
See the README.md file in each folder for details about that particular script's functions and use.
