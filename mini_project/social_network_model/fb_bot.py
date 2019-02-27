from browser_framework import driver_util
from time import sleep
from bs4 import BeautifulSoup

import re
import argparse
import variables


def facebook_bot(driver, user, password):

    print("[+] Bot started!!")

    send = 'send her a friend request.'
    sent = {}

    driver.get(variables.FACEBOOK_URL)

    driver_util.wait_for_object(driver, 'email')
    print("[+] Facebook page loaded!")

    email = driver.find_element_by_id('email')
    email.clear()
    email.send_keys(user)

    pwd = driver.find_element_by_id('pass')
    pwd.send_keys(password)

    email.submit()
    driver_util.wait_for_object(driver, 'q')
    print("[+] Login successful!")

    # Search
    search = driver.find_element_by_name('q')
    search.send_keys('teena')
    search.submit()

    print("[ ] Waiting for page to load...")
    sleep(10)
    print("[+] Search successful!")

    try:
        see_more = driver.find_element_by_link_text('See more')
        see_more.click()
        print("[+] Clicked see more!")
        sleep(5)
    except:
        pass

    # Fetch all results and access second user
    i = 0
    users = get_user_links(BeautifulSoup(driver.page_source))

    for link in users:
        if link not in sent:
            print("Going to access user: {}".format(link))

            driver.get(link)
            sleep(5)
            print("User loaded successfully!")

            try:
                driver_util.wait_for_object(driver, send)
                driver.find_element_by_link_text(send).click()
                i += 1
                print("[+] Friend request sent to {}/{} persons".format(i, len(users)))
                sleep(2)
            except:
                continue

            sent.update(link=1)

    sleep(5)


def get_user_links(page):
    links = []

    for link in page.find_all('a'):
        url = link.get('href')

        if url and re.search(variables.FACEBOOK_URL + '\w+\.\w+.\S+' + '\?ref=br_rs', url):
            links.append(url)

    return links


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('email', help='Facebook login email')
    parser.add_argument('password', help='Facebook login password')

    args = parser.parse_args()

    print("Logging in with facebook user: '{}'".format(args.email))

    driver = driver_util.get_driver('chrome')
    try:
        facebook_bot(driver, args.email, args.password)
    finally:
        # print("[-] Unexpected error occured. Quitting browser...")
        sleep(3)
        driver.quit()

if __name__ == '__main__':
    main()