#from bs4 import BeautifulSoup
import selenium.webdriver as webdriver
import  nancy as n
import speech as sp
 

def get_results(search_term):
    url = 'http://www.startpage.com'
    browser = webdriver.Chrome()
    browser.get(url)
    search_box = browser.find_element_by_id('query')
    search_box.send_keys(search_term)
    search_box.submit()
    
    try:
        links = browser.find_elements_by_xpath("//ol[@class='web_regular_results']//h3//a")
        
    except:
        links = browser.find_elements_by_xpath("//h3//a")
        
    result =[]
    for link in links:
        href =link.get_attribute('href')
        print(href)
        result.append(href)
    q = sp.Take_Command()
    if 'close' in q:    
        browser.close()
        return result
    else:
        get_results(q)
        
    
#n.speak('what you want to search')
'''q =n.Take_Command()
get_results(q)
'''
'''
import webbrowser

new = 2
taburl='http://google.com/?#q='

term = input('enter search query')

webbrowser.open(taburl+term,new=new)
    
'''