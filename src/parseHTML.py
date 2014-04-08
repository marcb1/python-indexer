import urllib2

class parseHTML:
    #constructor takes html data
    def __init__(self, _html):
        self.toParse = _html

    def countTag(self, htmlTag):
        return self.toParse.count('</'+htmlTag+'>')

    #function takes a tag example: a, and returns an array of all the found tags <a href ....>
    def tagData(self, htmlTag):
        self.Value = []
        count = self.toParse.count('</'+htmlTag+'>')
        x = 0
        start = 0
        while x<count:
            first = self.toParse.find('<'+htmlTag,start)
            end   = self.toParse.find('>',first+1)
            inner = self.toParse[first+1:end]
            self.Value.append(inner)
            x=x+1
            start = end+1
        return self.Value


    #takes tag and will return an array of what is actually inside this tag
    def tag_Data(self, tag):
        self.Data = []
        count = self.toParse.count('</'+tag+'>')
        x = 0
        start = 0
        while x<count:
            first = self.toParse.find('<'+tag,start)
            end   = self.toParse.find('>',first+1)
            last  = self.toParse.find('</'+tag+'>',end+1)
            x = x+1
            start = last+len('</'+tag+'>')
            data  = self.toParse[end+1:last]
            self.Data.append(data)
        return self.Data
