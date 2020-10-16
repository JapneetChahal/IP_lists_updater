import requests
from bs4 import BeautifulSoup


def merge_lists(arr, brr):
    for ip in brr:
        arr.append(ip+"\n")


def append_list(arr, big_arr):
    for i in arr:
        if len(i) != 0:
            big_arr.append(i)


def clean_string(st, list_ip):
    arr = st.split(" ")
    if not len(st) == 0 and st[0] == "#":
        return
    elif len(arr) == 1:
        append_list([arr[0]], list_ip)
    else:
        for word in arr:
            if word[0] == '[':
                append_list(word[1:-1].split(','), list_ip)
            elif len(word.split('.')) == 4:
                append_list([word], list_ip)


def get_ips(url):
    ip_list = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    lines = (soup.prettify().split("\n"))
    for line in lines:
        clean_string(line, ip_list)
    ip_list.sort()
    return ip_list


def write_ips(arr, file_path):
    with open(file_path, "w") as file:
        file.writelines(arr)

