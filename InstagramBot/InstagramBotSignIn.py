from selenium import webdriver
import time

# this program uses the selenium libary to sign into and operate aspects of an instagram account

url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
drv = webdriver.Chrome()
username = # enter your username here
password =  # enter you password here
home = 'https://www.instagram.com/'


def path():
    global drv
    drv = webdriver.Chrome()

def url_name(url):
    drv.get(url)
    time.sleep(3)

# logins into the account
def login(username, password):
    #enter in your username and password
    drv.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(username)
    drv.find_element_by_xpath('/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)

    # Finds and clicks the login button
    loginButton = drv.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
    loginButton.click()


# turns off notifications
def NoNotifications():
    time.sleep(4)

    # Finds and clicks Not now on the notifications option
    Notnow = drv.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
    time.sleep(1)
    Notnow.click()


def follow():

    # Finds explore page of suggested people to follow
    time.sleep(3)
    drv.get('https://www.instagram.com/explore/people/suggested/')

    # Follows the first 40 in the list
    for i in range(1,40):
        i = str(i)
        time.sleep(2)
        followButton = drv.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/div/div/div[' + i + ']/div[3]/button')
        followButton.click()


# accepts everyone trying to follow you
def accept():
    time.sleep(4)
    drv.get('https://www.instagram.com/accounts/activity?followRequests=1')
    for l in range(1, 20):
        l = str(l)
        time.sleep(2)
        acceptbutton = drv.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div[1]/div/div[' + l + ']/div[3]/div/div[1]/button')
        acceptbutton.click()

        
# the link to all of the people you are following
def following():
    drv.get('https://www.instagram.com/farm_sends/following/')



# likes images from a list of hashtags 
def liker():
    hashtag_list = ['hunting', 'hunt', 'hunter', 'outdoors', 'deerhunting', 'fishing', 'bowhunting', 'nature', 'deer', 'huntingseason', 'whitetail', 'archery', 'photography', 'huntinglife', 'duckhunting', 'wildlife']
    j = len(hashtag_list)
    for i in range(1, j):
        hash = hashtag_list[i]
        hashlink = ('https://www.instagram.com/explore/tags/' + hash + '/')
        drv.get(hashlink)
        time.sleep(3)
        picture1 = drv.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]')
        time.sleep(2)
        picture1.click()
        for m in range(1,25):
            m = str(m)
            m2 = ('[2]')
            m3 = int(m)
            time.sleep(2)
            likeButt = drv.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button')
            time.sleep(1)
            likeButt.click()
            if m3 > 1:
                xpath = ('/html/body/div[4]/div[1]/div/div/a' + m2)
            else:
                xpath = '/html/body/div[4]/div[1]/div/div/a'

            imgnex = drv.find_element_by_xpath(xpath)
            time.sleep(1)
            imgnex.click()


# watches everyone you follows story
def watchAll():
    drv.get(home)
    watch = drv.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[1]/a/div')
    time.sleep(2)
    watch.click()
    fastforward = drv.find_element_by_xpath('/section/div[2]/button[2]/div')
    fastforward.click()






    
    

    
        
path()
time.sleep(1)

url_name(url)

login(username, password)
NoNotifications()

liker()
watchAll()








