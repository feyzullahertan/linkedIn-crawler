from scraping import open_linkedin,login,scrape#get_salt_links
from checkdata import check
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import time


def main_menu():
    while(True):
        print("1 -> Adding salt linkedin link with Google API & Scraping")
        print("2 -> Check database vs real time")
        print("3 -> EXIT")
        ch=int(input("Enter Choice: "))
        if ch==1:
            #get_salt_links()
            open_linkedin()
            login()
            scrape()
        elif ch==2:
            check()
        elif ch==3:
            break
        else:
            print("Enter 1-2")

main_menu()
