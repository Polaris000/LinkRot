import requests
from bs4 import BeautifulSoup
import sldextract as s
import sys
import normalizer as n


broken_links = []
checked_links = []
count = 0

checked_file = open("checked_urls.csv", "w")
broken_file = open("broken_urls.csv", "w")

headers_checked_file = "Sr_No." + "," + "url" + "," + "status_code" + "," + "Proper" + "\n"
headers_broken_file = "url" + "," + "status_code" + "\n"

checked_file.write(headers_checked_file)
broken_file.write(headers_broken_file)

main_url = ""


def read_url(url):

	global count

	url = n.normalize(url, main_url_domain, main_url_ext)

	#check normalizer.py mailto: condition
	if url is not None:
		url_request = requests.get(url)

		count += 1
		print(count)
		url_domain = s.extract(url)["url_domain"]

		is_ok = True

		if url_request.status_code >= 400:

			broken_links.append(url)
			is_ok = False

			write_broken = url + "," + str(url_request.status_code) + "\n"
			broken_file.write(write_broken)

		print(url_request.status_code)
		soup = BeautifulSoup(url_request.content, "html.parser", from_encoding="iso-8859-1")

		url_list = soup.find_all('a', href=True)
		checked_links.append(url)

		write_checked = str(count) + "," + url + "," + str(url_request.status_code) + "," + str(is_ok) + "\n"
		checked_file.write(write_checked)

		if url_domain == main_url_domain:

			for link in url_list:

				if link['href'] not in checked_links:
					print(link['href'])
					read_url(link['href'])


if __name__ == '__main__':

	main_url = sys.argv[1]
	main_url_domain = s.extract(main_url)['url_domain']
	main_url_ext = s.extract(main_url)['url_tld']

	read_url(main_url)
	checked_file.close()
	broken_file.close()
