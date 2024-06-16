import pywikibot
from family import Family


site = pywikibot.Site('en', Family())
site.login('BulkEdit')

category = pywikibot.Category(site, 'Category:Modules')

investigate_list = []
error_list = []
already_modified_list = []
needs_modifications_list = []

def search_for_pages_to_edit():
    pages = category.articles()
    for page in pages:
        page_title = page.title()
        print("Currently looking at: " + page_title)

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
        
        # Verify the page is using the correct template (some test files might be under this category but malformed)
        templated_proof_text = "{{Template:ModuleUnique"
        if templated_proof_text not in page_text:
            print("This page isn't using the template format we expect, skipping (but adding to investigate list).")
            investigate_list.append(page_title)
            continue

        # If the page already contains the modification, there's no need to edit it
        finished_text = "| exclusive_to_ultimate_descendant"
        if finished_text in page_text:
            print("This page has already been updated, skipping.")
            already_modified_list.append(page_title)
            continue

        # One extra safety check to make sure the page has the text we want to modify
        to_modify_text = "| exclusive_descendant"
        if to_modify_text not in page_text:
            print("This page is using the expected template, but doesn't have the expected line to replace. Investigate.")
            investigate_list.append(page_title)
            continue

        # This is one of the pages we need to modify
        needs_modifications_list.append(page)


    print("\n\n*******************************Pages needing investiation:*******************************")
    for page in investigate_list:
        print(page)

    print("\n\n*******************************Pages with errors:*******************************")
    for page in error_list:
        print(page)

    print("\n\n*******************************Already completed before running:*******************************")
    print(len(already_modified_list))

    print("\n\n*******************************Pages to modify:*******************************")
    for page in needs_modifications_list:
        print(page)

search_for_pages_to_edit()