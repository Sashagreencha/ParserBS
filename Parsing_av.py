import csv
import json


from bs4 import BeautifulSoup
import requests


def par_av(refer):
    page = requests.get(refer)

    soup = BeautifulSoup(page.text, 'html.parser')
    lst_refer = []
    lst_rub = []
    lst_usd = []
    lst_year = []
    lst_volume = []
    lst_engine = []
    lst_dist = []
    lst_dict = ['reference', 'cost_rub', 'cost_usd',
                'year_issue', 'volume', 'engine', 'run']

    for link_ref in soup.find_all("a", class_="listing-item__link"):
        href_ = link_ref.get("href")
        lst_refer.append([refer + href_])

    for link_rub in soup.find_all("div", class_="listing-item__price"):
        lst_rub.append(int("".join([rub for rub in link_rub.text if rub.isdigit()])))

    for link_usd in soup.find_all("div", class_="listing-item__priceusd"):
        lst_usd.append(int("".join([usd for usd in link_usd.text if usd.isdigit()])))

    for link_param in soup.find_all("div", class_="listing-item__params"):
        lst_year.append(link_param.text.split(',')[0])
        lst_volume.append(link_param.text.split(',')[1])
        lst_engine.append(link_param.text.split(',')[2])
        distance = link_param.find('span')
        lst_dist.append(int("".join([dis for dis in distance.text if dis.isdigit()])))

    for ref in range(len(lst_refer)):
        for ru in range(len(lst_rub)):
            if ref == ru:
                lst_refer[ref].append(lst_rub[ru])
        for us in range(len(lst_usd)):
            if ref == us:
                lst_refer[ref].append(lst_usd[us])
        for y in range(len(lst_year)):
            if ref == y:
                lst_refer[ref].append(lst_year[y])
        for vol in range(len(lst_volume)):
            if ref == vol:
                lst_refer[ref].append(lst_volume[vol])
        for eng in range(len(lst_engine)):
            if ref == eng:
                lst_refer[ref].append(lst_engine[eng])
        for dist in range(len(lst_dist)):
            if ref == dist:
                lst_refer[ref].append(lst_dist[dist])

    dict_res = dict(zip(lst_usd, lst_refer))
    sorted_dict = dict(sorted(dict_res.items()))
    print(sorted_dict)
    with open('av_.csv', 'w', encoding="UTF-8", newline="") as file:
        avFile_csv = csv.writer(file, delimiter=";")
        for row in dict_res.values():
            avFile_csv.writerow(row)

    with open('av.json', 'w', encoding="UTF-8") as file:
        for row in dict_res.values():
            dict_json = dict(zip(lst_dict, row))
            json.dump(dict_json, file)


par_av('https://cars.av.by/bmw/x5')
