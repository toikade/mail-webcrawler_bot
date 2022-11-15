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
    city_soup = BeautifulSoup(city_page.content, 'html.parser')
    city_table = city_soup.find_all(id="example")
    city_rows = city_table[0].select("tbody tr a")
    # print(base_url+link)
    # print('+'*100)
    city_link = [link["href"] for link in city_rows]
    print(city_link)
    # print(len(city_link))
    # print('='*100)
    city_links.append(city_link)

town_links=[]
for item in city_links:
    for link in item:
        town_page = requests.get(base_url+link)
        town_soup = BeautifulSoup(town_page.content, 'html.parser')
        town_table = town_soup.find_all(id="example")
        town_rows = town_table[0].select("tbody tr a")
        #print(base_url+link)
        #print('+'*100)
        town_link = [link["href"] for link in town_rows]
        #print(town_link)
       # print(len(town_link))
        #print('='*100)
        town_links.append(town_link)
print(town_links)
print(len(town_links))
with open('town_links.txt', 'w') as f:
    f.write(town_links)

# scraped_data_array = []
# for item in town_links:
    # for link in item:
        # case_page = requests.get(base_url+link)
        # case_soup = BeautifulSoup(case_page.content, 'html.parser')
        # case_table = soup.find_all(id="example")
        # case_rows = table[0].select("tbody tr td")
        # wanted_list = [19,21,31,32,34,6,44,71,74]
        # wanted_info = [i.get_text() for index, i in enumerate(case_rows) if index in wanted_list]
        # scraped_data_array.append(wanted_info)
# print(scraped_data_array)