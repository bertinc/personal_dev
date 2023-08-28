"""
Trying to pull the number of cards in the huntress pledge
"""
import requests
from bs4 import BeautifulSoup

def main():
    """
    Going to try using the class name 'elementor-row' to pull out all the list items related to cards.
    """
    huntress_url = "https://support.elzra.com/docs/component-list-catacombs-castles-huntress/"
    redbox_url = "https://support.elzra.com/docs/component-list-catacombs-red-box/"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response_huntress = requests.get(huntress_url, headers=header, timeout=30)
    soup = BeautifulSoup(response_huntress.content, "lxml")
    rows_huntress = soup.find_all(True, {"class": "elementor-row"})

    response_redbox = requests.get(redbox_url, headers=header, timeout=30)
    soup = BeautifulSoup(response_redbox.content, "lxml")
    rows_redbox = soup.find_all(True, {"class": "elementor-row"})

    huntress_cards = get_total_cards(rows_huntress)
    redbox_cards = get_total_cards(rows_redbox)

    print(f"Number of cards in huntress pledge: {huntress_cards}")
    print(f"Number of cards in huntress pledge: {redbox_cards}")
    print(f"Total cards: {huntress_cards + redbox_cards}")

def get_total_cards(rows):
    """
    Loop through, filtering out rows that do not contain cards and then scrape
    out the list items to itterate for a count.
    """
    all_list_items = {}
    count = 0
    for row in rows:
        if  'Cards' in row.text and 'Keystones & Keeps' not in row.text:
            list_items = row.find_all("li")
            all_list_items[count] = {"num": len(list_items), "items": list_items}
        count += 1
    total_cards = 0
    for list_item in all_list_items.values():
        total_cards += list_item["num"]
    return total_cards

if __name__ == "__main__":
    main()
