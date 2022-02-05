# pip install requests
# pip install bs4
# The two commands listed above installs the dependencies needed for this program to run. 
import requests
from bs4 import BeautifulSoup
def main():
    url = "https://www.hardenwindows10forsecurity.com/"
    response = requests.get(url)

    print(f"currently scraping: {url}")


    soup = BeautifulSoup(response.content, "html.parser")
    H2 = soup.find_all('h2')

    print("Here are all of the <h2> headings.")

    for headings in H2:
        page_headings = print(headings)





if __name__ == "__main__":
    main()
