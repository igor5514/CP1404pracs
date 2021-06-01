"""
by Kenzin Igor
"""

import wikipedia

while True:
    page_title = input("Please enter the page title: ")
    if page_title.strip() !="":
        print(wikipedia.search(page_title))
        print(wikipedia.suggest(page_title))
        print(wikipedia.summary(page_title))
    else:
        break
