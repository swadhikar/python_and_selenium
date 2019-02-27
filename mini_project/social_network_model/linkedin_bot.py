import argparse
import os
import time
import urlparse
import random

from selenium import webdriver
from bs4 import BeautifulSoup

linkedin_root = 'https://www.linkedin.com'
linkedin_roots = linkedin_root
linkedin_url = linkedin_root + '/uas/login'
username_id = 'session_key-login'
password_id = 'session_password-login'
profile_pattern = '/in/'
job_pattern = '/jobs'


def get_people_links(page):
    links = []

    # Fill those links with profile links
    for link in page.find_all('a'):
        url = link.get('href')

        if url and profile_pattern in url and job_pattern not in url:
            links.append(url)

    return links


def get_job_links(page):
    links = []

    # Fill links in jobs page
    for link in page.find_all('a'):
        url = link.get('href')

        if url and job_pattern in url:
            links.append(url)

    return links


def get_user_profile_url(person):
    if linkedin_root not in person:
        person = linkedin_root + person
        return person


def Main():
    parser = argparse.ArgumentParser()
    parser.add_argument('email', help='Linkedin email')
    parser.add_argument('password', help='Linkedin password')

    args = parser.parse_args()

    browser = webdriver.Chrome(executable_path='c:\\chromedriver.exe')
    browser.get(linkedin_url)

    email = browser.find_element_by_id(username_id)
    email.send_keys(args.email)

    passwd = browser.find_element_by_id(password_id)
    passwd.send_keys(args.password)

    passwd.submit()

    # Clear screen
    os.system('clear')

    print("[+] Login success! Bot starting...")
    time.sleep(5)

    # my_network(browser)

    view_bot(browser)

    browser.close()


def my_network(browser):
    """ Switches the screen to My Network tab """
    my_network_button = browser.find_element_by_xpath("//a[contains(@href,'mynetwork')]")

    print("Found 'My Network' tab! Clicking...")
    my_network_button.click()

    retries = 5
    while True:
        if 'Your connections' in browser.page_source:
            break
        if not retries:
            raise Exception("Failed to load my network page")

        retries -=1 
        time.sleep(2)

    print("My Network page loaded successfully")


def view_bot(browser):
    visited = {}
    p_list = [] # People list PLANNED TO VISIT

    count = 0

    while True:
        # Sleep to make sure everything loads
        # add random to make us look human
        time.sleep(random.uniform(4, 10))
        page = BeautifulSoup(browser.page_source)

        people_list = get_people_links(page)

        if not people_list:
            # If in case there is no one found on the home screen
            # Got to 'My Network' and then parse through each user
            my_network(browser)

        if people_list:
            for person in people_list:
                id = get_user_profile_url(person)

                if id not in visited:
                    p_list.append(id)
                    visited[id] = 1

        if p_list:  # If there is people to look at
            person = p_list.pop()
            print("Going to access user: " + person)
            browser.get(person)
            count += 1
        else:  #  Otherwise find people from job pages
            browser.get('https://www.linkedin.com/jobs/')

            jobs = get_job_links(BeautifulSoup(browser.page_source))
            if jobs:
                job = random.choice(jobs)

                if linkedin_root not in job or linkedin_roots not in job:
                    job = linkedin_root + job

                browser.get(job)
            else:
                print("I'm lost! Exiting...")
                break

        print("[+] " + browser.title + " visited!\n("
                     + str(count) + "/" + str(len(p_list)) + "Visited/Queue)")

if __name__ == '__main__':
    Main()