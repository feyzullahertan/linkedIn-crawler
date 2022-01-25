from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time
import api
import mysql.connector

## Taking links
realdb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="feyzullah05",
    database="mydb"
    )
"""
names=[]

arr=[]
my_cursor=realdb.cursor()
my_cursor.execute("SELECT person_id,person_name FROM person")
names=my_cursor.fetchall()
sql_insert='UPDATE mydb.person SET person_link= "%s" WHERE person_name= "%s" '

def get_salt_links():
    for i in list(names):
        searchName=str(i[1]) + " linkedin"
        results = api.google_search(searchName, my_cse_id, num=1)
        for result in results:
            arr.append([result.get('link') , i[1]])
            print(i[1])
            print(result.get('link'))
    my_cursor.executemany(sql_insert,arr[0])
    realdb.commit()
"""




#chrome driver path. Chrome version 73
chrome_driver="F:\chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver)
driver.execute_script("window.alert('Python dosyasina geciniz');")


def open_linkedin():
    url="https://www.linkedin.com"
    driver.get(url)
    driver.maximize_window()

def login():
    id="**
    pw="**"
    id_input = driver.find_element_by_xpath('//*[@id="login-email"]')
    pw_input = driver.find_element_by_xpath('//*[@id="login-password"]')
    buton = driver.find_element_by_xpath('//*[@id="login-submit"]')

    time.sleep(1)
    id_input.send_keys(id)
    time.sleep(1)
    pw_input.send_keys(pw)
    time.sleep(1)
    buton.click()
    time.sleep(10)

def scrape():
    get_urls=()
    my_cursor=realdb.cursor()
    my_cursor.execute("SELECT person_id , person_link FROM person")
    get_urls=my_cursor.fetchall()
    for url in list(get_urls):
        driver.get(url[1])

        #Set x=0,y=0 default page.
        driver.execute_script("window.scrollTo(0, 0)")

        #Linkedin profile's name.
        name=driver.find_element_by_xpath('//*[contains(@id, "ember")]/div[1]/div[1]/h1').text
        print(name)
        
        #Linkedin profile's contact area.
        contact_location=driver.find_element_by_xpath('//*[contains(@class, "pv-top-card-v2-section__entity-name pv-top-card-v2-section__contact-info ml2 t-14 t-black t-bold")]').click()
        time.sleep(1)
        try: 
            contact=driver.find_element_by_xpath('//a[contains(@href,"mailto")]').text
            if contact:
                contact=contact.strip()
        except NoSuchElementException:
            contact="NULL"

        
        time.sleep(1)
        contact_exit=driver.find_element_by_xpath('//*[contains(@id, "ember")]/artdeco-modal/button').click()
        print(contact)

        
        #Scrolling!
        for i in range(17): 
               driver.execute_script("window.scrollBy(0, 250)")

               #Linkedin profile's school data.
               try:
                   school=driver.find_element_by_xpath('//*[contains(@id, "ember")]/div[2]/div/h3').text
                   if school:
                       school=school.strip()
               except NoSuchElementException:
                   school="NULL"

               #Linkedin profile's experience
               experience=[]
               try:
                   experience=driver.find_elements_by_xpath('//*[contains(@id,"ember")]/div[2]/h4[1]/span[2]')
               except NoSuchElementException:
                   for takeNullex in experience:
                       experience.append("NULL")

               time.sleep(1)
               #Linkedin profile's skills.
               abilities=[]
               try:
                   abilities=driver.find_elements_by_xpath('//*[contains(@class,"pv-skill-category-entity__name-text t-16 t-black t-bold")]')
               except NoSuchElementException:
                   for takeNullab in abilities:
                       abilities.append("NULL")
               time.sleep(2)
    
               upp="UPDATE person SET person_school=(%s), person_contact=(%s) WHERE person_id= (%s); "
               update_ex="INSERT INTO experience (experience_name,Person_person_id) VALUES ((%s) ,(%s)); "
               update_ab="INSERT INTO skill (skill_name,Person_person_id) VALUES ((%s) , (%s));"

        #INSERTING NEW DATAS
        my_cursor.execute(upp,(school,contact,url[0]))
        realdb.commit()
        for get_experience in experience:
            my_cursor.execute(update_ex,(get_experience.text ,url[0]))
            realdb.commit()
        for get_abilities in abilities:
            my_cursor.execute(update_ab,(get_abilities.text , url[0]))
            realdb.commit()


