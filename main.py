import requests
from bs4 import BeautifulSoup

base_url = "https://version3.guestworkervisas.com/"
page = requests.get(base_url+"schoolh1bjunkies.php")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')


table = soup.find_all(id="example")
table_rows = table[0].select("tbody tr a")
state_links = [link["href"] for link in table_rows]

city_links=[]
for link in state_links:
    city_page = requests.get(base_url+link)
    city_soup = BeautifulSoup(page.content, 'html.parser')
    city_table = soup.find_all(id="example")
    city_rows = table[0].select("tbody tr a")
    print(page)
    city_link = [link["href"] for link in city_rows]
    print(city_link)
    city_links.append(city_link)

print(city_links)
print(len(city_links))