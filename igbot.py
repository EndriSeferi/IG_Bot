from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from threading import Thread
import time


class Ig_Bot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        self.login()
        self.stop_thread=True

    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        ig_username = self.driver.find_element_by_name('username')
        ig_password = self.driver.find_element_by_name('password')
        time.sleep(2)
        ig_username.send_keys(self.username)
        time.sleep(1)
        ig_password.send_keys(self.password)
        time.sleep(1)
        ig_password.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            if self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button'):
                self.driver.find_element_by_xpath(
                    '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[3]/button[2]').click()
        except:
            pass

    
    #Creating thread so it doesnt freeze
    def contrl_suggestions(self):
        su=Thread(target=self.suggestions)
        su.start()
        if not (self.stop_thread):
            su._stop()

    def contrl_accept(self):
        Thread(target=self.follow_followers).start()
    def contrl_get_followers(self,x):
        Thread(target=self.get_followers(x)).start()


    def suggestions(self):
        print(self.stop_thread)
        self.driver.get('https://www.instagram.com/explore/people/suggested/')
        time.sleep(2)
        container = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/div[2]')
        a = 1
        contain = []
        while a < 10:
            contain.append(container.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[2]/div/div/div['+str(a)+']'))
            a += 1
            try:
                if self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]'):
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/button[2]').click()
                    break
            except:
                pass
        for user in contain:
            user.find_element_by_tag_name('button').click()
            time.sleep(2)
            try:
                if self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]'):
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/button[2]').click()
                    break
            except:
                pass
            time.sleep(20)
        return self.suggestions()

    def follow_followers(self):
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a').click()
        time.sleep(3)
        followers_container = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/div/div/div[2]/div[2]/div/div/div/div')
        time.sleep(1)
        follower = followers_container.find_elements_by_tag_name('button')
        for accept in follower:
            accept.click()
            try:
                if self.driver.find_elements_by_xpath(
                        '/html/body/div[4]/div/div/div[3]/button[2]'):
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[3]/button[2]').click()
            except:
                pass
            time.sleep(20)

    def get_followers(self, page):
        self.driver.get('https://www.instagram.com/'+page+'/')
        time.sleep(4)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        time.sleep(1)
        tabel = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]')
        time.sleep(3)
        last_ht, ht = 0, 1
        counter = 0
        # Here is the loading of all followers (scrolling)
        # if want to scroll all followers than replace counter <3 with the comment
        while counter < 7:  # last_ht != ht:
            last_ht = ht
            time.sleep(3)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0 ,arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
            """, tabel)
            counter += 1
        # Selecting the followers
        follower_tabel = self.driver.find_element_by_xpath(
            '/html/body/div[4]/div/div[2]/ul/div')

        time.sleep(1)
        # targeting the followers
        followers = follower_tabel.find_elements_by_tag_name('li')
        time.sleep(3)
        # going through every follow and clikc follow
        for followit in followers:
            follow = followit.find_element_by_tag_name("button")
            time.sleep(2)
            follow.click()
            # if we get a window with unfollow click cancel
            try:
                if self.driver.find_elements_by_xpath(
                        '/html/body/div[5]/div/div'):
                    self.driver.find_element_by_xpath(
                        '/html/body/div[5]/div/div/div[3]/button[2]').click()
                elif self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/button[2]'):
                    self.driver.find_element_by_xpath(
                        '/html/body/div[4]/div/div/div[2]/button[2]').click()
            except:
                pass
            time.sleep(20)
