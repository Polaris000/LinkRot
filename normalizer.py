def normalize(url, main_url_domain, extension):
	if url[0] == "#":

		url = "https://" + main_url_domain + extension + "/" + url

	elif url.startswith('//'):
		url = "https:" + url

	elif url.startswith('/'):
		url = "https://" + main_url_domain + extension + url

	elif url.startswith("mailto:"):
		url = None

	return url
