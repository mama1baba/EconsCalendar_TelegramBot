#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from datetime import date
import telegram


# In[2]:


# Save screenshot from URL in current directory
URL = 'https://ph.investing.com/economic-calendar/'


options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options = options)
driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
driver.set_window_size(S('Width'),S('Height')) # May need manual adjustment
driver.find_element_by_tag_name('body').screenshot("EconomicCalendar" + str(date.today()) + ".png")
driver.quit()


# In[3]:


f = open('Token.txt', mode = 'r')
token = f.read()

bot = telegram.Bot(token = token)


# In[5]:


bot.sendDocument(chat_id = "@testnews32", document = open("EconomicCalendar" + str(date.today()) + ".png", 
                                                         mode = 'rb'),
                caption = 'Source:' + URL)
    


# In[ ]:




