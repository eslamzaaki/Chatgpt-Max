from selenium import webdriver
from selenium_stealth import stealth
from bs4 import BeautifulSoup
from urllib.parse import urlparse



def GetTop1GoogleResults(input):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(
        options=options, executable_path="\chromedriver.exe")

    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            ) 

    query = input
    n_pages = 10
    results = []
    counter = 0
    for page in range(1, n_pages):
        url = "http://www.google.com/search?q=" + \
            query + "&start=" + str((page - 1) * 10)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        search = soup.find_all('div', class_="yuRUbf")
        for h in search:
            counter = counter + 1
            title = h.a.h3.text
            link = h.a.get('href')
            rank = counter
            results.append({'title': h.a.h3.text, 'url': link,
                            'domain': urlparse(link).netloc, 'rank': rank})
    return results[0]['url']
    # for i, result in enumerate(results):
    #    firstResult  = result['url']
    #    print(
    #        f"Result {i+1}: {result['title']}\n{result['url']}\n{result['domain']}\n{result['rank']}")
