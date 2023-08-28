"""
Author: Robert Rallison
Created: 2023-08-28

WHY: Trying to find the number of cards in the huntress pledge which includes the red box (and black box but I already sleaved it). I did
some searching but as soon as I came accross the component list, I stopped looking and just decided to scrape it for what I needed. Honestly,
I was having no luck finding any posts even on BGG to get this number and I wanted to make sure I purchased enough sleaves.

HOW: For this I am using some html response scraping with BeautifulSoup. The path to the cards sections is not super clear at first when
inspecting the pages. I decided to find all rows of a specific class and then filter out anything that doesn't have the word 'Cards'
in the text. This almost worked perfectly. I had one row that was actually just a part of the main components list that mentions
cards. So that is the only static skip. This script, as is, works out of the box on three of their component list pages.

TIPS: To test another page, use the get_card_lists function by itself to print the row names. That was helpful for me to figure
out what I needed to do differently in my logic between the pages.
"""
import requests
from bs4 import BeautifulSoup

def main():
    """
    Going to try using the class name 'elementor-row' to pull out all the list items related to cards.
    """
    huntress_url = "https://support.elzra.com/docs/component-list-catacombs-castles-huntress/"
    redbox_url = "https://support.elzra.com/docs/component-list-catacombs-red-box/"
    blackbox_url = "https://support.elzra.com/docs/component-list-catacombs-black-box/"

    # Get the rows for the huntress box
    rows_huntress = get_rows(huntress_url)

    # get the rows for the red box which I think is KS extras
    rows_redbox = get_rows(redbox_url)

    # get the rows for the red box which I think is KS extras
    rows_blackbox = get_rows(blackbox_url)

    # I could combine them but I think I like the idea of printing a card count for each separately
    huntress_cards = get_cards(rows_huntress)
    redbox_cards = get_cards(rows_redbox)
    blackbox_cards = get_cards(rows_blackbox)
    all_cards = huntress_cards + redbox_cards  # intentionally not including Black Box here

    # Just for fun: uncomment the below line if you want to print the card names
    print_card_names(all_cards, "Huntress and Red Box Card Names")

    print(f"Number of cards in huntress box: {len(huntress_cards)}")
    print(f"Number of cards in red box: {len(redbox_cards)}")
    print(f"Total cards to sleave: {len(all_cards)}")

    # This one I counted manually and it was correct so I think it's safe to assume the others are too.
    print(f"BONUS Number of cards in black box: {len(blackbox_cards)}")

def get_rows(url):
    """
    Since this was repeating code, I figured I may as well make it a function.

    Args:
        url (str): webpage to scrape
    Returns:
        Soup search results : all of the tags found when making the initial Soup request
    """
    response = requests.get(url, timeout=30)
    rows = BeautifulSoup(response.content, "lxml").find_all(True, {"class": "elementor-row"})
    return rows

def get_cards(rows):
    """
    Make sense of the list dictionary we get from get_card_lists and build a list of card names to return.

    Args:
        rows (tags): all of the tags found when making the initial Soup request
    Returns:
        List: all of the card names with white space stripped away
    """
    card_lists = get_card_lists(rows)

    # card_count = 0
    card_names = []
    for card_list_data in card_lists.values():
        # card_count += card_list_data["num"]
        for card in card_list_data["items"]:
            card_names.append(card.text.strip())
    return card_names

def get_card_lists(rows):
    """
    Loop through, filtering out rows that do not contain cards and then scrape
    out the list items to itterate for a count.

    Args:
        rows (tags): all of the tags found when making the initial Soup request
    Returns:
        Dictionary: filtered down rows and the found list items in them
    """
    all_list_items = {}
    count = 1
    for row in rows:
        if  'Cards' in row.text and 'Keystones & Keeps' not in row.text:
            list_items = row.find_all("li")
            if len(list_items) > 0:
                all_list_items[count] = {"num": len(list_items), "items": list_items, 'text': row.text}
        # Why do this instead of simply creating a list of dictionaries? I want to remember which row it was for each one. It came in handy
        # to get here and it may come in handy again if the page structure ever changes. It also makes for a nice unique key.
        count += 1
    return all_list_items

def get_longest_name(cards):
    """
    Nice a quick way to grab the longest card in the list for printing a formatted table.

    Args:
        cards (list): list of card names
    Returns:
        int: the length of the longest card in the list
    """
    longest = 0
    for card in cards:
        if len(card) > longest:
            longest = len(card)
    return longest

def print_card_names(cards, title="Pretty printing the cards."):
    """
    For a sort of pretty print of all the cards? This will make it look like there are duplicates, but that's just because
    I did not care to save the categories. Some cards are actually for crossovers to other games in the Catacombs universe.

    Args:
        cards (list): list of card names
        title (str): a title at the top of the table
    """
    MAX_COLS = 3
    justify = get_longest_name(cards)

    # This is just for looks and based on the length of the longest name
    break_line = "-" * (justify + MAX_COLS) * MAX_COLS

    # 1: Loop through the cards to build a list of rows with the right number of names per row
    cols = 0
    current_row = []
    rows = []
    for card in cards:
        current_row.append(card)
        cols += 1
        if cols == MAX_COLS:
            rows.append(current_row)
            current_row = []
            cols = 0
    
    # 2: Loop through those rows, join them into a nice printable string, and print them
    print(break_line)
    print(title.center(len(break_line)))
    for row in rows:
        print(break_line)
        # build a nice row of names
        row_text = ''.join(f"| {card.ljust(justify)} " for card in row)
        print(row_text)
    print(break_line)

if __name__ == "__main__":
    main()
