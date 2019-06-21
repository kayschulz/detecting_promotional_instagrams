import time
import urllib.request
from collections import Counter
from selenium.webdriver import Chrome
import pickle


def recent_25_posts(username):
    """With the input of an account page, scrape
       the 25 most recent posts urls"""
    url = "https://www.instagram.com/" + username + "/"
    browser = Chrome()
    browser.get(url)
    post = 'https://www.instagram.com/p/'
    post_links = []
    while len(post_links) < 25:
        links = [a.get_attribute('href')
                 for a in browser.find_elements_by_tag_name('a')]
        for link in links:
            if post in link and link not in post_links:
                post_links.append(link)
        scroll_down = "window.scrollTo(0, document.body.scrollHeight);"
        browser.execute_script(scroll_down)
        time.sleep(10)
    else:
        return post_links[:25]


def insta_details(urls):
    """Take a post url and return post details"""
    browser = Chrome()
    post_details = []
    for link in urls:
        browser.get(link)
        try:
            # This captures the standard like count.
            likes = browser.find_element_by_partial_link_text(' likes').text
        except:
            # This captures the like count for videos which is stored
            xpath_view = '''//*[@id="react-root"]/section/main/div/
                            div/article/div[2]/section[2]/div/span/span'''
            likes = browser.find_element_by_xpath(xpath_view).text
        age = browser.find_element_by_css_selector('a time').text
        try:
            xpath_comment = '''//*[@id="react-root"]/section/main/div/
                               div/article/div[2]/div[1]/ul/li[1]/div/
                               div/div[2]/span'''
            comment = browser.find_element_by_xpath(xpath_comment).text
            insta_link = link.replace('https://www.instagram.com/p', '')
            username_path = '''//*[@id="react-root"]/section/main/div/div/
                               article/header/div[2]/div[1]/div[1]/h2/a'''
            username = browser.find_element_by_xpath(username_path).text
            post_details.append({'user': username, 'link': insta_link,
                                 'likes/views': likes, 'age': age,
                                 'comment': comment})
        except:
            continue
        time.sleep(10)
    return post_details


def add_promo_key(user, labels):
    """Add the promo label to each post by a user"""
    filepath = '../data/raw_data/' + user + '.pkl'
    posts = pickle.load(open(filepath, 'rb'))
    for ind, post in enumerate(posts):
        post['promo'] = labels[ind]
    return posts
