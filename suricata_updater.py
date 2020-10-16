import requests
from bs4 import BeautifulSoup
import suricata_helper as sh

tor_list = []
bot_list = []


def get_links(url, att):
    links_list = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    for hlink in soup.findAll('a'):
        temp = hlink.get('href')
        if att in temp:
            links_list.append(url+temp)
    return links_list


def create_list(url):
    global tor_list
    global bot_list
    tor = get_links(url, "tor")
    bot = get_links(url, "bot")
    for link in tor:
        sh.merge_lists(tor_list, sh.get_ips(link))
    for link in bot:
        sh.merge_lists(bot_list, sh.get_ips(link))

