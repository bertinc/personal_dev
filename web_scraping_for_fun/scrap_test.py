import requests
import lxml
from bs4 import BeautifulSoup
import sys
import json
import csv

def main(argv):
    all_posts = {}
    start = 0
    current_posts = get_next_page(start)
    all_posts.update(current_posts)
    while(current_posts):
        start += 15
        current_posts = get_next_page(start)
        all_posts.update(current_posts)
        if start > 200:
            # gonna leave this here for now until I can determine I am
            # relatively safe from infinite loops
            break
    print(len(all_posts))

    # print to JSON
    out_filename = 'output.json'
    out_file = open(out_filename, 'w')
    json.dump(all_posts, out_file)
    out_file.close()

    # print to CSV
    out_filename = 'output.csv'
    out_file = open(out_filename, 'w', newline='')
    csv_writer = csv.writer(out_file)
    csv_writer.writerow(['id', 'name', 'date', 'msg'])
    for key, val in all_posts.items():
        csv_writer.writerow([key, val['name'], val['date'], str(val['msg'])[:10]])

def get_next_page(start):

    base_url = f"http://www.oldclassiccar.co.uk/forum/phpbb/phpBB2/viewtopic.php?t=12591&start={start}"
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }

    response = requests.get(base_url, headers=header)

    soup = BeautifulSoup(response.content, "lxml")

    post_table = soup.find(class_="forumline")
    posts = post_table.find_all(True, {'class':['row1', 'row2']})

    # test if we should break out


    posts_dict = {}
    current_id = ''

    for post in posts:
        name_and_id = post.find('span', class_='name')
        if name_and_id:
            id = name_and_id.find('a')['name']
            name = name_and_id.text
            if id:
                current_id = id
                posts_dict[current_id] = {'name': name}
        else:
            details = post.find('span', class_='postdetails')
            body = post.find('span', class_='postbody')
            if details:
                if len(details.contents) and str(details.contents[0]).startswith('Posted:'):
                    posted = str(details.contents[0])[8:]
                    if current_id and current_id in posts_dict.keys():
                        posts_dict[current_id]['date'] = posted
            if body:
                if current_id and current_id in posts_dict.keys():
                    posts_dict[current_id]['msg'] = ''.join(str(element) for element in body.contents)

    return posts_dict

if __name__ == "__main__":
    main(sys.argv[1:])