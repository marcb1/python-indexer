import operator

class parsedDictionary:
    def __init__(self):
        self.Dict = new_dict = dict()

    #key is domain, element is how many times it occured so far
    def addElement(self, key):
        if key in self.Dict:
            self.Dict[key] = self.Dict[key] + 1
        else:
            self.Dict.update({key:1})

    def sortByValue(self):
        sortedDict = sorted(self.Dict.iteritems(), key=operator.itemgetter(1))
        return sortedDict

    def exists(self, key):
        return key in self.Dict

    def add(self, dict):
        for k, v in dict.Dict.iteritems():
            if k in self.Dict:
                self.Dict[k] = self.Dict[k] + v
            else:
                self.Dict.update({k:1})
