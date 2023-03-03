# -*- coding:utf-8 -*-
# The author is Sympathy
from bs4 import BeautifulSoup
import requests
import csv
import bs4


# 用于抓取湖大硕士生招生初试线表格数据
def check_link(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print('无法连接服务器')


def get_contents(ulist, rurl):
    soup = BeautifulSoup(rurl, 'lxml')
    trs = soup.find_all('tr')
    for tr in trs:
        ui = []
        for td in tr:
            ui.append(td.string)
        ulist.append(ui)


def save_contents(urlist):
    with open("股市分析.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['企业债券兑付/付息/服务费提示（2023年2月）'])
        for i in range(len(urlist)):
            # for p in range(1, 13):
            #     urlist[i].append(' ')
            # if i in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            #     for p in range(2):
            #         urlist[i].insert(0, ' ')
            # elif i not in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            #     for p in range(13):
            #         urlist[i].insert(0, ' ')
            # elif i in [35, 37]:
            #     for p in range(6):
            #         urlist[i].insert(0, ' ')
            writer.writerow([urlist[i][0], urlist[i][1], urlist[i][2], urlist[i][3], urlist[i][4], urlist[i][5], urlist[i][6], urlist[i][5], urlist[i][7], urlist[i][8], urlist[i][9], urlist[i][10], urlist[i][11],
                             urlist[i][12]])


def main():
    urli = []
    url = "https://www.chinabond.com.cn/cb/cn/xxpl/ywgg/tgywgg/20230129/161991420.shtml"
    rs = check_link(url)
    get_contents(urli, rs)
    save_contents(urli)


main()