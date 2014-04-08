###Python HTML Crawler 
#####CS 578 project
===========

####About:

This project collects popular third party tracking javascript on the web.

The Python script takes either a single HTTP address, or a file with a list of addresses. The script will then output the javascript on the page(s). If given a file with a list of addresses, a sorted list is outputted.

####Usage:

To print a list of external javascript on a page:
```
src/main-crawler.py -u http://some.domain 
```


To index a list of sites from a file
```
src/main-crawler.py -r file_name
```


####More information
#####Required modules:
For centos/fedora:
```
yum -y install python-pip
pip install tldextract
```

#####Collected Data
The data I collected from running this script, and their corresponding indexed addresses are located under
```
src/domain-lists
```

#####Technical Stuff

This script will download the HTTP response and parse the HTML looking for a ```<script * src='URL'>``` tag. It will parse the URL from the tag and add its top level domain to the dictionary. 
If a file is given as input, the dictionary will be updated on each GET request and sorted at the end.

Please note, even though this python script will not execute any javascript, your IP address, some headers sent with the GET request, and the DNS query can be recorded.

The current user agent that the script sends in the HTTP header is:  ```"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0"```

The browser may execute javascript code which in turn creates a link to an external code. Such javascript is not added to the output, as this script does not execute any javascript, it only parses the HTTP response.
