import bs4
import requests
import re


def print_presenters(arr):
    for p in arr:
        print(p)


def get_presenters(arr):
    b = []
    for a in arr:
        if a.find('&amp;'):
            a = a.replace('&amp;', 'and')
        b.append(a[6:-3])
    return b;


def parse_site():
    r = requests.get("https://www.blackhat.com/html/bh-media-archives/bh-archives-2000.html")
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    temp = soup.select('b')
    temp = str(temp)
    names1 = re.findall(r'2000">.*</a', temp)
    return names1;


if __name__ == "__main__":
    html = parse_site()
    presenters = get_presenters(html)
    print_presenters(presenters)
