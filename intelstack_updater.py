import os


bot_list = []
mal_list = []
tor_list = []
blk_list = []


def get_ips(dat_content):
    arr = []
    for i in range(1, len(dat_content)):
        if "." in dat_content[i][0]:
            arr.append(dat_content[i][0])
    return arr


def create_list(db, keys):
    for i in keys:
        t = i.split(':')
        os.system("sudo -u intel-stack-client -g intel-stack-client intel-stack-client config --set zeek.include=false")
        os.system("intel-stack-client api "+t[0])
        os.system("intel-stack-client pull")
        dat_content = [j.strip().split() for j in open(db).readlines()]
        if t[1] == "Bot":
            global bot_list
            bot_list = get_ips(dat_content)
        elif t[1] == "Malware":
            global mal_list
            mal_list = get_ips(dat_content)
        elif t[1] == "Tor":
            global tor_list
            tor_list = get_ips(dat_content)
        elif t[1] == "Blacklisted":
            global blk_list
            blk_list = get_ips(dat_content)

