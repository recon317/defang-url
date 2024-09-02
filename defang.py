from argparse import ArgumentParser, Namespace

parser = ArgumentParser()
parser.add_argument('url', help='Input the URL to defang', type=str)
args: Namespace = parser.parse_args()

url = args.url

def parse_schema(url): 

    if url.startswith('https://'):
        return ('hxxps[://]')
    if url.startswith('http://'):
        return ('hxxp[://]')

def parse_domain(url): 

    domain = url.split('/')[2]
    parsed_domain = domain.replace(".","[.]")
    return (parsed_domain)

def parse_path(url): 

    path = url.split("/")[3:]
    joined_path = '/'.join(path)
    return ('/' + joined_path)


def defang(url):
    path = parse_path(url)
    schema = parse_schema(url)
    domain = parse_domain(url)
    
    parsed_sections = schema, domain, path
    print(''.join(parsed_sections))

defang(url)