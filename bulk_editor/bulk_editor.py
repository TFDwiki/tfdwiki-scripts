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

        # This is one of the pages we need to scan in-depth for changing
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

def modify_text(page_text):
    # Replace all instances of Transcendant with Transcendent, regardless of capitalization
    return page_text.replace("ranscendant", "ranscendent")

def update_page(page):
    modified_text = modify_text(page.text)
    if modified_text == page.text:
        print("No changes made to " + page.title())
        return

    print("Updating " + page.title())
    try:
        page.text = modified_text
        page.save(summary='BOT EDIT: Bulk fix of spelling mistake')
    except Exception as e:
            print(f"An error occurred with page {page.title()}: {e}")

def bulk_edit():
    search_for_pages_to_edit()
    for page in needs_modifications_list:
        update_page(page)

# Single test edit
# update_page(pywikibot.Page(site, "TestModule"))

# Perform all edits (Make sure this is tested with single test pages first!)
# bulk_edit()