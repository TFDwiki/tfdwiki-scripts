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

def modify_text(page_text):
    completed_text = []
    lines = page_text.split('\n')
    last_line = ""
    line_above = "capacity_cost_0"
    for line in lines:
        # Go through lines until you hit a capacity line, then insert if needed
        if line_above not in last_line:
            last_line = line
            completed_text.append(line)
            continue
        
        # Only insert the descendant lines if they're not already here
        if "exclusive_base_descendant" not in line:
            completed_text.append(" | exclusive_base_descendant = ")
            completed_text.append(" | exclusive_to_ultimate_version = ")

        last_line = line
        completed_text.append(line)
    
    multiline_version = "\n".join(completed_text)
    return multiline_version

def update_page(page):
    modified_text = modify_text(page.text)
    if modified_text == page.text:
        print("No changes made to " + page.title())
        return

    print("Updating " + page.title())
    try:
        page.text = modified_text
        page.save(summary='BOT EDIT: Bulk inserting exclusive_base_descendant into module pages missing this template property.')
    except Exception as e:
            print(f"An error occurred with page {page.title()}: {e}")

def bulk_edit():
    search_for_pages_to_edit()
    for page in needs_modifications_list:
        update_page(page)

# Single test edit
#update_page(pywikibot.Page(site, "TestModuleMulti"))

# Perform all edits (Make sure this is tested with single test pages first!)
# bulk_edit()
