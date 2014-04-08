import parseHTML
import parsedDictionary
import json
import urllib2
import tldextract
import re

#return a list of the actual embedded javascript code
def GetFullScripts(domain_name):
        html = getPage(domain_name)
        parse = parseHTML.parseHTML(html)
        data = parse.tag_Data("script")
        return data

#just get the URL's to the externally linked javascript
def getScripts(domain_name):
        html = getPage(domain_name)
        parse = parseHTML.parseHTML(html)
        data = parse.tagData("script")
        arr = []

        #add the script's URLs to the list
        for i in range(0, len(data)):
                url = extractSrc(data[i])
                if(type(url) is str):
                        arr.append(url)
        return arr

#write a list to a json file
def writeDataToJson(file_name, data):
        with open(file_name, 'w') as outfile:
                json.dump(data, outfile)

def printList(list):
        #print URL's parsed
        for i in range(0, len(list)):
              print list[i]

def extractSrc(data):
        begin =  data.find('src=')
        if(begin < 0):
          return
        if((data.find('"'), begin+5) >= 0):
          end = data.find('"', begin+5)
        else:
          end = data.find("'", begin+5)
        data = data[begin+5:end]
        return data


#will extract url from a string if one exists
def extractURL(data):
        match = re.search("(?P<url>https?://[^\s]+)", data)
        if match is not None: 
              return match.group("url")
        #begin =  data.find('http')
        #if(begin <= 0):
        #        return
        #end = data.find('"', begin+1)
        #data = data[begin:end]
        #return data

#returns a string of html from a get request
def getPage(domain_name):
        #let's pretend to be ie
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:25.0) Gecko/20100101 Firefox/25.0'
        req = urllib2.Request(domain_name, headers={"User-Agent" : user_agent})
        html = urllib2.urlopen(req).read()
        return html

def readFile(fname):
        f = open(fname, "r" )
        lines = [line.rstrip('\n') for line in f]
        f.close()
        return lines

def crawlList(list):

        main_dict = parsedDictionary.parsedDictionary()

        #iterate through domains
        for i in range(0, len(list)):
                print "Scripts present at " + list[i]
                scripts = getScripts(list[i])
                printList(scripts)
                
                #iterate through this domain's scripts
                #this codes checks if the script is linked externally or is hosted on the same domain (given by a relative URL)
                dict = parsedDictionary.parsedDictionary()
                for y in range(0, len(scripts)):
                      full = ''
                      if( (scripts[y].startswith("//")) or (scripts[y].startswith("http"))):
                          full = tldextract.extract(scripts[y])
                          if(len(full.domain) <= 1):
                            full = tldextract.extract(list[i])
                      else:
                          full = tldextract.extract(list[i])

                      link = full.domain + '.' + full.suffix
                      if(not dict.exists(link)):
                            dict.addElement(link)
                main_dict.add(dict)
                print main_dict.Dict
                print "}}}}}"
                print dict.Dict
                print "\n -------------------------------"
        sortedlist = main_dict.sortByValue()
        print " \n Top scripts: "
        printList(sortedlist)

