def normalize(url, main_url_domain, extension):

    updated_url = {
      "#": "https://" + main_url_domain + extension + "/" + url,
      "//": "https:" + url,
      "/": "https://" + main_url_domain + extension + url,
      "mailto:": None
    }

    for key in updated_url.keys():
        if url.startswith(key):
            return updated_url[key]
    return url
