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
import logging

def main():
    """
    Loop through a dictionary of urls to output the number of cards in each box set from the Huntress + Black Box pledge
    of Catacombs & Castles 2nd Edition Kickstarter campaign.
    """
    logging.basicConfig()
    logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger("card_count")

    # Add as many urls as you like here from the components list pages by Elzra
    urls = {
        "huntress": "https://support.elzra.com/docs/component-list-catacombs-castles-huntress/",
        "redbox": "https://support.elzra.com/docs/component-list-catacombs-red-box/",
        "blackbox": "https://support.elzra.com/docs/component-list-catacombs-black-box/"
    }

    all_cards = []
    justify = 30
    count_padding = 4
    report = []  # Building a report so we can decide later out to produce output
    for name, url in urls.items():
        # put this in there so it looks less like it's doing nothing
        logger.debug(f"Getting {name} cards")
        rows = get_rows(url)
        cards = get_cards(rows)
        all_cards += cards
        report.append(f"Cards in {name} box: {str(len(cards)).rjust(count_padding)}".rjust(justify))
    report.append(f"Total Cards: {str(len(all_cards)).rjust(count_padding)}".rjust(justify))

    # Uncomment this if you want to see the card names
    # print_card_names(all_cards)

    # from here you can decide where you want to send the report
    print('\n'.join(report))

def get_rows(url):
    """
    Using the class name 'elementor-row' to pull out all the row elements. This gives us a nice list of tags
    to later filter for only rows with card related things.

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

    card_names = []
    for card_list_data in card_lists.values():
        for card in card_list_data["items"]:
            card_names.append(card.text.strip())
    return card_names

def get_card_lists(rows):
    """
    Loop through, filtering out rows that do not contain cards and then scrape out the list items to itterate later. Lots of line comments
    in this one becuase there were a lot of places where I felt it needed more explianation.

    Args:
        rows (tags): all of the tags found when making the initial Soup request
    Returns:
        Dictionary: filtered down rows and the found list items in them
    """
    all_list_items = {}
    count = 1  # Row number
    # Add things to this list as you find them. Any text in this list will be used to filter out rows that do not have cards.
    filter_list = [
        "Keystones & Keeps"
    ]
    for row in rows:
        # The second half of this condition is using a generator to make sure we skip any rows where the text contains
        # something from the filter list. It didn't feel clear when I wrote it so I thought I should explain.
        if 'Cards' in row.text and not any(value in row.text for value in filter_list):
            list_items = row.find_all("li")  # so far, just getting the <li> tags at this point seems to work
            if len(list_items) > 0:
                # Yes, there were a few rows on initial testing that had 0 items, so lets ignore those
                all_list_items[count] = {"num": len(list_items), "items": list_items, 'text': row.text}
                # Why do this instead of simply creating a list of cards here? Well, these extra bits of information come in handy for
                # debugging when trying out a new page. If the numbers seem off, you can call this method alone and investigate what is
                # getting through. Most likely you will need to add more things to the filter list.
        count += 1
    return all_list_items

def print_card_names(cards, title="Pretty printing the cards."):
    """
    For a sort of pretty print of all the cards? This will make it look like there are duplicates, but that's just because
    I did not care to save the categories. Some cards are actually for crossovers to other games in the Catacombs universe.

    Args:
        cards (list): list of card names
        title (str): a title at the top of the table
    """
    MAX_COLS = 3
    justify = len(max(cards, key=len))

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
