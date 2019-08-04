'''
-----------------------------
This script is created to screenshot Investing.com webpage via selenium chrome driver,
save into local machine and send it out via telegram bot to respective channels
-----------------------------
'''

from selenium import webdriver #webdriver to launch chrome
from datetime import date
import telegram #for telegram bot


URL = 'https://ph.investing.com/economic-calendar/'

# Launch Chrome without Header
options = webdriver.ChromeOptions()
options.headless = True

# Save screenshot from URL in current directory
driver = webdriver.Chrome(options = options)
driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X) # to obtain dynamic width and height
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element_by_tag_name('body').screenshot("EconomicCalendar" + str(date.today()) + ".png")
driver.quit() # remember to quit driver

#Read your telegram bot API keys
f = open('Token.txt', mode = 'r')
token = f.read()

bot = telegram.Bot(token = token)

# Send out screenshot with link as captions ; chat_id = channel_name
bot.sendDocument(chat_id = "@testnews32", document = open("EconomicCalendar" + str(date.today()) + ".png", 
                                                         mode = 'rb'),
                caption = 'Source:' + URL)
    





