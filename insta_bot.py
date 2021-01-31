from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from random import randint

chromewebdriver = webdriver.Chrome(ChromeDriverManager().install())
chromewebdriver.get('https://instagram.com')
accept = chromewebdriver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/button[1]')
accept.click()
sleep(3)
username = chromewebdriver.find_element_by_name('username')
password = chromewebdriver.find_element_by_name('password')
username.send_keys('#USRNAME')
password.send_keys('#PASSWORD')
lbutton = chromewebdriver.find_element_by_css_selector('#loginForm > div > div:nth-child(3)')
lbutton.click()
sleep(3)
notnow1 = chromewebdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
notnow1.click()
sleep(2)
notnow2 = chromewebdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
notnow2.click()
chromewebdriver.get('https://www.instagram.com/explore/')
sleep(randint(3,8))
post = chromewebdriver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div[1]/div[2]')
post.click()
comment_list = ['Awesome Post', 'Amazing Content', 'Brilliant', 'Best thing on Internet Today']
for x in range(0,5):                # Number of posts you want to follow, comment and like
    sleep(randint(2,7))
    if chromewebdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').text == 'Follow':
        chromewebdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/header/div[2]/div[1]/div[2]/button').click()
        like = chromewebdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span')
        like.click()
        sleep(randint(1,4))
        comment = chromewebdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[2]/button/div')
        comment.click()
        commentbox = chromewebdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea')
        commentbox.click()
        commentbox.send_keys(comment_list[randint(0,3)])
        sleep(randint(2,4))
        postcomment = chromewebdriver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button[2]')
        postcomment.click()
        chromewebdriver.find_element_by_link_text('Next').click()

    else:
        chromewebdriver.find_element_by_link_text('Next').click()


