import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import csv

base_url = "https://visa.1point3acres.com/"
page = requests.get(base_url+"h1b/salary/job-science-teacher/city-santa%20clara,ca")
print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')

mainTable = soup.find('table')
tableRow = mainTable.find_all('tr', class_="ant-table-row")

#create a variable to check the first loop and set the header for the csv file
firstIter = True
counter = 1
for trItem in tableRow:
    tdTags = trItem.findAll('td')
    # Employer = tdTags[0].text
    # EmployerLink = tdTags[0].find('a')["href"]
    # JobTitle = tdTags[1].text
    # BaseSalary = tdTags[2].text
    # SchoolLocation = tdTags[3].text
    # SubmitDate = tdTags[4].text
    # StartDate = tdTags[5].text
    CaseLink = tdTags[6].find('a')["href"]
    # Certified = tdTags[6].text
    print(CaseLink)
    
    # join the base_url with the caselink and request the page
    casePage = requests.get(base_url+CaseLink)
    # pass it to bs in order to use the bs syntax to query it
    caseSoup = BeautifulSoup(casePage.content, 'html.parser')
    caseTable = caseSoup.find(id = '__NEXT_DATA__').text
    print(type(caseTable))
    # loads json text into py in order to be recognised as dict
    json_object = json.loads(caseTable)
    # format into a human readable 
    json_formatted_object = json.dumps(json_object, indent=2)

    caseYear = json_object['props']['pageProps']['year']
    caseNumber = json_object['props']['pageProps']['number']
    # dataBody is the main wanted data sorted from the json
    dataBody = json_object['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['details']
    dataFields = ["CASE_NUMBER", "CASE_STATUS", "EMPLOYER_ADDRESS", "EMPLOYER_CITY", "EMPLOYER_COUNTRY", "EMPLOYER_NAME",
                  "EMPLOYER_PHONE", "JOB_TITLE", "PREVAILING_WAGE", "WORKSITE_CITY", "WORKSITE_STATE", "EMPLOYER_POC_EMAIL",
                  "EMPLOYER_POC_FIRST_NAME", "EMPLOYER_POC_LAST_NAME", "EMPLOYER_POC_MIDDLE_NAME", "EMPLOYER_POC_PHONE",
                  "EMPLOYER_POC_JOB_TITLE"]

    dataFields.insert(0, 'caseYear')
    # dataValues is where the values to be added to the csv file are held
    dataValues = []
    for i in dataFields:
        if dataFields.index(i)>0:  #the 2 first values are added later, so have to be skipped
            try:
                if i == "EMPLOYER_ADDRESS" and i not in dataBody:
                    dataValues.append(dataBody["EMPLOYER_ADDRESS1"])
                    continue
                dataValues.append(dataBody[i])
            except KeyError:
                dataValues.append("N/A")
            
    dataValues.insert(0, caseYear)
    # if firstIter:
    #     with open('h1bdata.csv', 'w') as file: #open the csv file for writing
    #         writer = csv.writer(file)
    #         writer.writerow(dataFields)
    #         firstIter = False
    with open('h1bdata.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(dataValues)

    

    print(json.dumps(dataBody, indent=2))
    #print(dataBody['VISA_CLASS'])
    print(counter)    
    counter +=1

dataFromCsv  = pd.read_csv('h1bdata.csv')
print(dataFromCsv)
