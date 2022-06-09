from header import *


def crawling(id, iter, interval = 3, base_url = BASE_URL_MINOR, start_page = 0):
    """

    Args:
        id (str): sub-url of target gallery, ex) 'genrenovel', 'baseball_new10'
        iter (int): iteration number of pages
    """
    title_list = []
    t = dt.datetime.now()
    time = str(t.time()).split(".")[0]
    time = time.replace(":", "-")
    filename = f"genre_novel_crawling_{t.year}-{t.month}-{t.day}-{time}.csv"
    f = open(filename, mode = "w", encoding='utf-8')
    csv_w = csv.writer(f,delimiter="\n")
    # html
    for page in range(start_page, start_page + iter):
        try:
            params = {'id' : id, "page" : page}
            response = requests.get(base_url, params=params, headers=headers)
        except requests.exceptions.Timeout as errd:
            print(f"Timeout Error : on {page}", errd)
            continue       
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting : on {page}", errc)
            continue
        except requests.exceptions.HTTPError as errb:
            print(f"Http Error : on {page}", errb)
            continue
        # requests.exceptions.RequestException. ingerit
        # Any Error except upper exception
        except requests.exceptions.RequestException as erra:
            print(f"AnyException : on {page}", erra)
            continue
        # print(response.status_code)
        if response.status_code != 200:
            continue
        
        soup = BeautifulSoup(response.content, 'html.parser')
        html_list = soup.find('tbody').find_all('tr')


        for i in html_list:
            if i.find("b"):
                continue

            title = i.find('a', href=True).text # 제목
            title_list.append(title)
       

        if page % interval == 0 and page != 0:
            print(f'[{page-start_page}/{iter}] is done {((page-start_page) / iter * 100):.1f}%')
            csv_w.writerow(title_list)
            title_list = []

    print(f'[{page}/{page}] Crawling is done 100.0%')

    f.close()
    return title_list


# print(str(t.time()).split(".")[0])
for i in range(10):
    crawling("genrenovel", 5700 , interval=50, start_page= i*5700)
    time.sleep(600)
