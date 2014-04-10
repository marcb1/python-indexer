#!/usr/bin/python

import parseHTML
import basicFunctions
import sys, getopt
import json


def main(argv):
    domain = ''
    read_file = ''
    usage = 'usage: main-crawler.py -u <http-url> -r <file-to-read-from> (optional): -h (for help)'
    full_usage = 'something.py \n usage: something.py -u <http-url> (optional): -h (for help)  -w write_to_json_file -r read_from_json_file \n -u Please provide full http address here this field is required \n  \t Will print out the external javascript this page links to \n -r This is optional, provide a file name to read a list of addresses from'
    try:
        opts, args = getopt.getopt(argv,"hu:w:r:",["url=", "output-file=", "read="])
    except getopt.GetoptError:
        print usage
        sys.exit(2)

    #require at least 1 argument and the first argument must be the domain name or help
    if((len(opts) == 0) or  (('-u' not in opts[0]) and  ('-h' not in opts[0]) and ('-r' not in opts[0]))):
        print usage
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print full_usage
            sys.exit()
        elif opt in ("-u", "--http-url"):
            if (arg.find("http") < 0):
                print "invalid address, must start with http://"
                print usage
                sys.exit()
            domain = arg
        elif opt in ("-r", "--read"):
            if(len(arg) < 2):
                print "invalid file name"
                sys.exit()
            read_file = arg
        else:
            print usage
            sys.exit()

    if(len(read_file) > 2):
        lines = basicFunctions.readFile(read_file)
        basicFunctions.crawlList(lines)

    else:
        scripts = basicFunctions.getScripts(domain)
        basicFunctions.printList(scripts)

if __name__ == "__main__":
    main(sys.argv[1:])
