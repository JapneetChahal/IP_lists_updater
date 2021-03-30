#!/usr/bin/env python3.6

import firehol_updater
import suricata_updater
import intelstack_updater
import os
import yaml

db = ""
keys = []
suricata_url = ""
firehol_url = ""
folder_path = ""


def read_yml():
    with open("config.yaml") as file:
        conf = yaml.full_load(file)
        global db, keys, suricata_url, firehol_url, folder_path
        db = conf.get("db_path")
        keys = conf.get("api")
        suricata_url = conf.get("suricata_url")
        firehol_url = conf.get("firehol_url")
        folder_path = conf.get("input_folder_path")


def merge_and_sort(arr1, arr2, arr3, name):
    for i in arr2:
        arr1.append(i)
    for i in arr3:
        arr1.append(i)
    arr1.sort()
    arr1.append(name)
    return arr1


def create_file(path, arr):
    with open(path, "w+") as file:
        file.writelines(arr)


def update_folder(frr):
    for i in frr:
        print(i[len(i)-1]+" list updated")
        with open(folder_path+"/"+i[len(i)-1]+".txt", "w+") as file:
            file.writelines(i)


def get_lists():
    suricata_updater.create_list(suricata_url)
    intelstack_updater.create_list(db, keys)
    firehol_updater.create_list(firehol_url)

    botcc_list = merge_and_sort(suricata_updater.bot_list, intelstack_updater.bot_list, firehol_updater.bot_list, "botcc")
    torr_list = merge_and_sort(suricata_updater.tor_list, intelstack_updater.tor_list, firehol_updater.tor_list, "torr")
    blacklist_list = merge_and_sort(firehol_updater.blk_list, intelstack_updater.blk_list, [""], "blacklisted IP")
    dos_list = firehol_updater.dos_list
    dos_list.append("dos")
    malware_list = intelstack_updater.mal_list
    malware_list.append("malware")
    arr = [blacklist_list, botcc_list, torr_list, dos_list, malware_list]
    return arr


def main():
    read_yml()
    update_folder(get_lists())
    os.system("rm -r blocklist-ipsets && rm -r __pycache__")


main()

