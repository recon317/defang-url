from argparse import ArgumentParser, Namespace
parser = ArgumentParser()
parser.add_argument('url', help='Input the URL to defang', type=str)
args: Namespace = parser.parse_args()

url = args.url

def defang(url):
    url_list = list(url)
    for i in url_list:
        if i == '.':
            index = url_list.index(i)
            url_list[index] = '[.]'
        if i == 't':
            index = url_list.index(i)
            before = url_list[index - 1]
            after = url_list[index + 1]
            if before == 'h' or before == 't' or before=='x':
                if after == 't' or after == 'p':
                    url_list[index] = 'x'
        if i == ':':
            index = url_list.index(i)
            before = url_list[index - 1]
            after = url_list[index + 1]
            if before == 'p' or before == 's':
                if after == '/':
                    url_list[index] = '[:'
        if i == '/':
            index = url_list.index(i) + 1
            before = url_list[index - 1]
            after = url_list[index + 1]
            if before == '/':
                url_list[index] = '/]'
    defanged_url = ''.join(url_list)
    print(defanged_url)


defang(url)