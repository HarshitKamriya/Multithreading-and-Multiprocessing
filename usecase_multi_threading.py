'''
Real - world Exampel: Multithreading for I/O -bound Tasks
Scenario : web Scraping
Web scraping often involves making numerous network requests to 
fetch web pages. These tasks are I/o-bound because they spenad a log 
of tiem waiting for responese from ervers. Multithreading can
significantly improve the perfrmance by allowing multiple by 
allowing multiple web pages to be fetched concurrently.'''


import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://blog.langchain.com/?_gl=1*yahdgb*_gcl_au*MTk4OTY5NDU4My4xNzUzNzA4MDEx',
    'https://www.langchain.com/?_gl=1*1waf16h*_gcl_au*MTk4OTY5NDU4My4xNzUzNzA4MDEx',
    'https://langchain-ai.github.io/langgraph/concepts/why-langgraph/'
]


def  fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Fetchecd {len(soup.text)} Character from {url}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("All web pages fethced")

