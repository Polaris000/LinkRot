def extract(url):
	#file with tld extensions
	f = open("tld.txt", 'r')

	tld_list = (f.read()).split(",\n  ")

	url = url.replace("https://", "")
	if '/' in url:
		url = url[:url.index('/')]

	for i in tld_list:
		if url.endswith(i):
			url_tld = i

			url = url.replace(url_tld, "")
			# print(i)
			break

	else:
		url_tld = ""

	url_domain = url.strip('.')

	url_contents = {"url_domain": url_domain, "url_tld": url_tld}
	return url_contents
