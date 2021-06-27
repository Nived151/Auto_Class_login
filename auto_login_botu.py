from discord_webhook.webhook import DiscordEmbed
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from discord_webhook import DiscordWebhook
from datetime import datetime
from os import environ
import schedule
import time

now = datetime.now()
x = now.strftime("%H:%M")
y = environ['discord_webhook']

def login_domain():
    driver = webdriver.Chrome()
    url = environ['domain_link']
    driver.get(url)
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/input').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[2]/input').send_keys(environ['time_username'])
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[5]/input').click()
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/div[1]/div[5]/input').send_keys(environ['time_password'])
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/section/div/div[2]/div/div[1]/div[2]/form/input[2]').click()
    driver.find_element_by_xpath('/html/body/div[4]/div/section/div/div[2]/div/a/div').click()

def login_ccc():
    driver = webdriver.Chrome()
    url = environ['ccc_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='CCC class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()
def login_aptitude():
    driver = webdriver.Chrome()
    url = environ['aptitude_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='Aptitude class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()
def login_verbal():
    driver = webdriver.Chrome()
    url = environ['verbal_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='Verbal class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()
def login_resume():
    driver = webdriver.Chrome()
    url = environ['resume_link']
    driver.get(url)
    webhook = DiscordWebhook(url=y)
    embed = DiscordEmbed(title='resume class Logined at', description=x, color='03b2f8')
    webhook.add_embed(embed)
    response = webhook.execute()

schedule.every().monday.at("07:00").do(login_ccc)
schedule.every().monday.at("09:00").do(login_verbal)
schedule.every().monday.at("10:30").do(login_domain)

schedule.every().tuesday.at("07:00").do(login_ccc)
schedule.every().tuesday.at("09:00").do(login_verbal)
schedule.every().tuesday.at("10:30").do(login_domain)

schedule.every().wednesday.at("07:00").do(login_ccc)
schedule.every().wednesday.at("09:00").do(login_verbal)
schedule.every().wednesday.at("10:30").do(login_domain)

schedule.every().thursday.at("07:00").do(login_ccc)
schedule.every().thursday.at("09:00").do(login_resume)
schedule.every().thursday.at("10:30").do(login_domain)

schedule.every().friday.at("07:00").do(login_ccc)
schedule.every().friday.at("09:00").do(login_resume)
schedule.every().friday.at("10:30").do(login_domain)

schedule.every().saturday.at("09:00").do(login_verbal)

while True:
    schedule.run_pending()
    time.sleep(1)