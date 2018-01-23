# import os
import time
from selenium import webdriver
# chromedriver = "./chromedriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# browser = webdriver.Chrome(chromedriver)
browser = webdriver.Firefox();
links = []

def load(browser):
    browser.get('https://www.linkedin.com');

    password = browser.find_element_by_css_selector('#login-password');
    password.send_keys('qwaszx321')

    user = browser.find_element_by_css_selector('#login-email');
    user.send_keys('huascarmc@hotmail.com');

    submit = browser.find_element_by_css_selector('#login-submit');
    submit.click();

    browser.get('https://www.linkedin.com/search/results/people/?facetCurrentCompany=%5B%2210049434%22%5D');


def clickNext(browser):
    time.sleep(5)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(5)
    nextButton = browser.find_element_by_css_selector('.next');
    nextButton.click()

def printName(links):
    for link in links:
        print(link)

def getLinks(browser, links):
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    thisPageLinks = browser.find_elements_by_css_selector('.search-result__result-link');
    for i in range(0, len(thisPageLinks) - 1, 2):
        links.append(thisPageLinks[i].get_attribute('href'));
    print(len(links));

load(browser)
getLinks(browser, links)
printName(links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)
clickNext(browser)
getLinks(browser, links)


for i in range(0, len(links), 1):
    time.sleep(3)
    browser.get(links[i])




# browser.close()
