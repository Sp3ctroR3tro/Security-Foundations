import requests
from bs4 import BeautifulSoup
def main():
    url = "https://www.hardenwindows10forsecurity.com/"
    response = requests.get(url)

    print(f"currently scraping: {url}")
    soup = BeautifulSoup(response.content, "html.parser")
    H2 = soup.find_all('h2')

    print("Here is the text of all <h2> headings tags :")

    for headings in H2:

        page_headings = print(headings.get_text())

if __name__ == "__main__":
    main()
