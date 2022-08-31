import csv
import json


def read_json():
    with open('av.json', encoding='UTF-8') as file_json:
        for i in list(file_json):
            print(i, end="")


read_json()


def read_csv():
    file_csv = open('av_.csv', encoding='UTF-8')
    file_csv_r = csv.reader(file_csv, delimiter=';')
    file_csv_data = list(file_csv_r)
    for row in file_csv_data:
        for str_ in row:
            print(str_ + ' ')


read_csv()
