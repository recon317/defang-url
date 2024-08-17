from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
parser.add_argument('url', help='Input the URL to defang', type=str)
args: Namespace = parser.parse_args()

url = args.url

def defang(url):
    url_list = list(url)
    for index, char in enumerate(url_list):
        if char == '.':
            url_list[index] = '[.]'
        if char == 't':
            before = url_list[index - 1]
            after = url_list[index + 1]
            if before in ('h', 't', 'x') and after in ('t', 'p'):
                url_list[index] = 'x'
        if char == ':':
            before = url_list[index - 1]
            after = url_list[index + 1]
            if (before == 'p' or before == 's') and after == '/':
                url_list[index] = '[:'
        if char == '/' and url_list[index + 1] == '/':
            url_list[index + 1] = '/]'
    defanged_url = ''.join(url_list)
    print(defanged_url)

defang(url)