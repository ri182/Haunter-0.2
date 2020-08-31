from selenium import webdriver

hostname = "p.webshare.io"
port = "19999"

while True:
    try:
        options = webdriver.ChromeOptions()
        #  options.add_argument('--proxy-server=%s' % hostname + ":" + port)
        options.add_argument('-headless')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(options=options)

        driver.get("https://www.ebay.co.uk")
        driver.get(
            "https://www.ebay.co.uk/sch/i.html?_from=R35&_nkw=pokemon&_sacat=0&LH_TitleDesc=0&_sop=10&LH_BIN=1&_oac=1&_ipg=25")

        item_title_1 = driver.find_element_by_css_selector(
            "#srp-river-results > ul > li:nth-child(2)")
        item1_href = driver.find_element_by_css_selector(
            "#srp-river-results > ul > li:nth-child(2) > div > div.s-item__info.clearfix > a").get_attribute('href')

        item_title_2 = driver.find_element_by_css_selector(
            "#srp-river-results > ul > li:nth-child(3)")
        item2_href = driver.find_element_by_css_selector(
            "#srp-river-results > ul > li:nth-child(3) > div > div.s-item__info.clearfix > a").get_attribute('href')

        item_title_3 = driver.find_element_by_css_selector(
            "#srp-river-results > ul > li:nth-child(4)")
        item3_href = driver.find_element_by_css_selector(
            "#srp-river-results > ul > li:nth-child(4) > div > div.s-item__info.clearfix > a").get_attribute('href')
        with open('log.csv', 'w') as f:
            print(
                '''
                           -._                                   _.
                            \ `-.._                           _,' |
                             \     `-._    _,.--------.._  _."    '
                              \        `--'              ``.     /
                               \                                j    __
            __         __       \                               |.-"' /
             `.`-.`-.__`.`'"----"\                              |    /
                `.       `.       '        ._                       /
                `..        \               | `.               /|   /
                  `.        `.             |   `._          .' |  /
                    `.  .-----`            |      `.       /   ' '""''
                      `. `.            .    ._      `_    /  ,'    .'
                        `. `.           `._   `'""'"'     ""' ,  ,'   haunter.py 0.2
                          `. `.          `.`.              ,-/ ,'
                            `. `.          \|,---..  ,--"./ / ,--------".
                              `._           `.     `/ , .`.',:           \\
                                 `._          `..".,./ ' _.' :            \  `.
                               ,-'" `-._              _."     .   |.-"`.   \  |
                              .         `-..........-'        |   `..   \   |_'
                              |           `".                 `.._   .  '  ,'
                              |         |   |                     `"'    .'
                              |   /\    |'  '
                              '  /  \   ||   .
                             '   \  '   |'   ;
                              \  '  \   `...'
                               `""   `,'
            '''
            , file=open("log.csv", "a", encoding='utf-8'))
            print('-------------------', file=open("log.csv", "a", encoding='utf-8'))
            print(item_title_1.text.replace("NEW LISTING", "").replace("Watch", ""), item1_href, file=open("log.csv", "a", encoding='utf-8'))
            print('-------------------', file=open("log.csv", "a", encoding='utf-8'))
            print(item_title_2.text.replace("NEW LISTING", "").replace("Watch", ""), item2_href, file=open("log.csv", "a", encoding='utf-8'))
            print('-------------------', file=open("log.csv", "a", encoding='utf-8'))
            print(item_title_3.text.replace("NEW LISTING", "").replace("Watch", ""), item3_href, file=open("log.csv", "a", encoding='utf-8'))
            print('coffee............', file=open("log.csv", "a", encoding='utf-8'))
            print(' ', file=open("log.csv", "a", encoding='utf-8'))
            print(' ', file=open("log.csv", "a", encoding='utf-8'))
            print(' ', file=open("log.csv", "a", encoding='utf-8'))
            driver.quit()
    except:
        pass