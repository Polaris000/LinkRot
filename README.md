## LinkRot

LinkRot recursively checks all urls on a page and reports any broken links.
The script outputs a brief summary of the scan. For a more detailed view -- including all verified links and broken links -- the script outputs `checked_urls.csv` and `broken_urls.csv`.

To check for valid extensions, the script consults `tld.txt`, which has a list of several commonly used tld's.

### Usage
```bash
$ python3 finder.py <url>
```

### Examples

- Invalid URL
```bash
$ python3 finder.py https://polaris000.github.com

Received url:  https://polaris000.github.com
--------------------------------------------------
Starting...

Checking  https://polaris000.github.com
Fetching page at https://polaris000.github.com......done
Broken url:  https://polaris000.github.com

Summary
--------------------------------------------------
URL: 		 	 https://polaris000.github.com
URL Domain: 	 polaris000.github
URL Extension: 	 .com
Links Checked: 	 1
Broken Links: 	 1
Link Rot: 	 	 100.00%
--------------------------------------------------
```

- Valid URL (limiting to about 30 urls)
```
$ python3 finder.py https://polaris000.github.io

Received url:  https://polaris000.github.io
--------------------------------------------------
Starting...

Checking  https://polaris000.github.io
Fetching page at https://polaris000.github.io......done
Looking for links on the webpage......done

Fetching page at https://polaris000.github.io/......done
Checking:  https://polaris000.github.io/
Looking for links on the webpage......done

Fetching page at https://polaris000.github.io/archives/......done
Checking:  https://polaris000.github.io/archives/
Looking for links on the webpage......done
.
.

Fetching page at https://www.linkedin.com/in/polaris000......done
Checking:  https://www.linkedin.com/in/polaris000
* Broken url:  https://www.linkedin.com/in/polaris000
.
.

Fetching page at https://polaris000.github.io/#1......done
Checking:  https://polaris000.github.io/#1
Looking for links on the webpage......done

Fetching page at https://it.telangana.gov.in/sectors/e-governance/...Could not read url...

Summary
--------------------------------------------------
URL: 		 	 https://polaris000.github.io
URL Domain: 	 polaris000.github
URL Extension: 	 .io
Links Checked: 	 31
Broken Links: 	 1
Link Rot: 	 	 3.22%
--------------------------------------------------
```

### Requirements
```
bs4==0.0.1
requests==2.20.0
```