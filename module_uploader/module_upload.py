import pywikibot
from tfd_family import Family
from pywikibot import login

def groupedsplit(string, splitchar='"', sep=','):
    tempstr = ''
    splitstr = []
    inquote = False
    for x in string:
        if x == splitchar:
            inquote = not inquote
            continue
        if x == sep and not inquote:
            splitstr.append(tempstr)
            tempstr = ''
            continue
        tempstr += x
    splitstr.append(tempstr)
    return splitstr

site = pywikibot.Site(code='en', fam=Family(), user='')
site.login(login.LoginManager(site=site, user=''))

characters = ["Ajax", "Blair", "Bunny", "Freyna", "Gley", "Jayber", "Kyle", "Lepic", "Sharen", "Valby", "Viessa", "Ultimate Lepic", "Ultimate Viessa"]

top = f'''{{{{PreReleaseData}}}}
{{{{Template:ModuleDefinitions|'''

middle = f'''
}}}}
{{{{Template:ModuleDetailsDefinitions'''

bottom = f'''
}}}}'''



file = open('tfd mods.csv', 'r')
mods = file.read().split('\n')

modules = {}

for mod in mods:
    x = groupedsplit(mod, sep=',')
    if x[0] == 'Name': continue
    thismodname = modules.get(x[0]) or []
    typ = ''
    for gun in ('Shotgun', 'Sniper', 'Launcher'):
        if gun in x[5]:
            x.append(gun)
            x[5] = x[5].replace(gun, '').replace(',', '').strip()
    
    thismodname.append(x)
    modules.update({x[0]: thismodname})


for modname, variants in modules.items():
    text = top
    page = pywikibot.Page(site, modname)
    dyn2 = ''
    count = 0
    for variant in variants:
        count += 1
        ex_d, ex_c, ex_wt = ['']*3
        ex = variant[5]
        if ex in characters:
            ex_d = ex
        else:
            ex_c = ex
        if len(variant) > 7:
            ex_wt = variant[7]
        # if ex_wt == '': continue
        text += f'''
{{{{Template:ModuleUnique
 | name = {{{{PAGENAME}}}}
 | variantID = {count}
 | pic = 
 | version_released = {{{{Launch}}}}
 | rarity = {variant[1]}
 | socket = {variant[2]}
 | class = {variant[3]}
 | max_enhancement_level = 
 | capacity_cost_0 = {variant[4]}
 | exclusive_descendant = {ex_d}
 | exclusive_category = {ex_c}
 | exclusive_weapon_type = {ex_wt}
 | effect_0 = {variant[6]}
 | effect_1 = 
 | effect_2 = 
 | effect_3 = 
 | effect_4 = 
 | effect_5 = 
 | effect_6 = 
 | effect_7 = 
 | effect_8 = 
 | effect_9 = 
 | effect_10 = 
}}}}'''
        dyn2 += f'''
|{{{{Template:ModuleUniqueDetails
| variantID = {count}
| module_name = {{{{PAGENAME}}}}
}}}}'''
    text += middle
    text += dyn2
    text += bottom
    if text != page.text:
        if abs(len(page.text) - len(text)) < 5:
            minor = True
        else:
            minor = False
        page.text = text
        page.save("Importing Module data", minor=minor, botflag=True)