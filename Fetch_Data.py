def fetch():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    import datetime
    import pandas as pd

    chromedriver = "D:\\chromedriver_win32\\chromedriver"
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

    driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

    driver.get("http://www.lordswm.com")

    time.sleep(1)

    username = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[1]/table[1]/tbody/tr[2]/td[2]/input[1]")
    username.send_keys("viju")

    time.sleep(1)

    password = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[1]/table[1]/tbody/tr[4]/td[2]/input[1]")
    password.send_keys("Inazuma11")

    time.sleep(1)

    submit = driver.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td[2]/table/tbody/tr[2]/td[1]/table[2]/tbody/tr/td/div/input")
    submit.submit()

    time.sleep(1)

    roulette = driver.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr[3]/td/table/tbody/tr/td[4]/table/tbody/tr/td[9]')
    roulette.click()

    time.sleep(1)

    spinhistory = driver.find_element_by_xpath("/html/body/center/table[2]/tbody/tr/td/form/table/tbody/tr/td/table/tbody/tr[2]/td/div/a[4]")
    spinhistory.click()

    time.sleep(1)

    url = driver.current_url

    driver.quit()

    urlresp = urlopen(url)
    data = urlresp.read()
    urlresp.close()

    soup = BeautifulSoup(data, "html.parser")

    table = list(soup.find("table", attrs={"class": "wbwhite"}))
    div = table[0].find_all("div")

    times = div[0].text.split()
    number = div[1].text.split()

    now = datetime.datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M").split()

    datetime = str(date[0]) + " " + str(times[-1])

    dicto = {}
    dicto["DateTime"] = datetime
    dicto["Number"] = number[-1]


    df = pd.read_csv("document.csv")
    new_df = pd.DataFrame([dicto], columns=dicto.keys())
    df = df.append(new_df, sort=False, ignore_index=True)
    df.to_csv("document.csv", index=False)
