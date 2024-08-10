import wikipedia

MENU = """---Menu---
Choose a search option:
(P)age Title
(S)earch Phrase"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "":
        if choice == "P":
            get_page_data()
        elif choice == "S":
            get_search_phrase()
        else:
            print("Invalid option.")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you!")


def get_page_data():
    title = input("Enter page title: ")
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(f"Title: {page.title}")
        print(f"URL: {page.url}")
        print(f"Summary: {page.summary[:500]}...")
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError as e:
        print(e)
    """
    # Fixed BeautifulSoup error by replacing line 389 in wikipedia.py with:
    lis = BeautifulSoup(html, features="html.parser").find_all('li')
    """


def get_search_phrase():
    phrase = input("Enter search phrase: ")

    search_results = wikipedia.search(phrase, results=5)
    print("Search results:")
    for result in search_results:
        print(f"- {result}")

main()
