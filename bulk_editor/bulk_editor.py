import pywikibot
from family import Family


site = pywikibot.Site('en', Family())
site.login('BulkEdit')

category = pywikibot.Category(site, 'Category:Modules')

investigate_list = []
error_list = []

pages = category.articles()
for page in pages:
    page_title = page.title()
    print("Currently looking at: " + page_title)

    # Verify the page is using the correct template (some test files might be under this category but malformed)
    templated_proof_text = "{{Template:ModuleUnique"
    try:
        page_text = page.text
    except pywikibot.exceptions.IsRedirectPage:
        print(page_title + " is a redirect page, these shouldn't be listed as part of the category.")
        error_list.append(page_title)
        continue
    except pywikibot.exceptions.NoPage:
        print(page_title + " does not exist... HOW?!")
        error_list.append(page_title)
        continue
    
    if templated_proof_text not in page_text:
        print("This page isn't using the template format we expect, skipping (but adding to investigate list).")
        investigate_list.append(page_title)
        continue


print("\n\n*******************************Pages needing investiation:*******************************")
for page in investigate_list:
    print(page)

print("\n\n*******************************Pages with errors:*******************************")
for page in error_list:
    print(page)