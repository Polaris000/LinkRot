tld_list = []
tld_cache_list = []


def read_tld_list():
    global tld_list

    with open("tld.txt", 'r') as f:
        tld_list = [line.rstrip(',\n') for line in f]


def extract(url):

    url = url.replace("https://", "")
    if '/' in url:
        url = url[:url.index('/')]

    for i in tld_cache_list:
        if url.endswith(i):
            url_tld = i
            url = url.replace(url_tld, "")
            break

    else:
        for i in tld_list:
            if url.endswith(i):

                url_tld = i
                tld_cache_list.append(i)
                url = url.replace(url_tld, "")
                break

        else:
            url_tld = ""

    url_domain = url.strip('.')

    url_contents = {
        "url_domain": url_domain,
        "url_tld": url_tld
        }

    return url_contents
