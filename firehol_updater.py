import os

blk_list = []
tor_list = []
bot_list = []
dos_list = []


def clear_list(arr):
    ret = []
    for line in arr:
        if "#" not in line and " " not in line and "*" not in line and line[0] != '.':
            ret.append(line)
    return ret


def sort_list(arr):
    ret = []
    for element_arr in arr:
        for element in element_arr:
            ret.append(element)
    ret.sort()
    fr = [ret[0]]
    for i in range(1, len(ret)):
        if ret[i] != ret[i-1]:
            fr.append(ret[i])
    return fr

# defaul url = "git clone https://github.com/firehol/blocklist-ipsets.git"


block_rr = [[]]
bot_rr = [[]]
dos_rr = [[]]
tor_rr = [[]]


def create_list(url):
    cues = "blocklist cleantalk dronebl firehol_abusers ipblocklist stopforspam sblam proxylists proxy ri_connect ri_web " \
       "socks_proxy ssl_proxy xroxy bi_any bi_apache bi_as bi_cms bi_default bi_dns bi_dov bi_ftp bi_htt bi_mail bi_ " \
       "blocklist_de blueliv dataplane dshield_ firehol_ normshield_ urandomusto".split(
        " ")
    os.system("git clone "+url)
    files_list = os.listdir("./blocklist-ipsets")
    for file_name in files_list:
        if os.path.isfile("./blocklist-ipsets/" + file_name):
            for cue in cues:
                if cue in file_name and "bot" and "dos" and "tor" not in file_name:
                    with open("./blocklist-ipsets/" + file_name, "r+") as file:
                        block_rr.append(clear_list(file.readlines()))
                    break
                elif "bot" in file_name:
                    with open("./blocklist-ipsets/" + file_name, "r+") as file:
                        bot_rr.append(clear_list(file.readlines()))
                    break
                elif "dos" in file_name:
                    with open("./blocklist-ipsets/" + file_name, "r+") as file:
                        dos_rr.append(clear_list(file.readlines()))
                    break
                elif "tor" in file_name:
                    with open("./blocklist-ipsets/" + file_name, "r+") as file:
                        tor_rr.append(clear_list(file.readlines()))
                    break
    global blk_list
    global tor_list
    global bot_list
    global dos_list
    blk_list = sort_list(block_rr)
    tor_list = sort_list(tor_rr)
    bot_list = sort_list(bot_rr)
    dos_list = sort_list(dos_rr)

