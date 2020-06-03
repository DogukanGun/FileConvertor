from lxml import etree as tree
import json
"""
XmlConvert
----------
According to demand,file is converted to a new file (Json or Csv)
"""
class XmlConvert:
    def __init__(self, type,source,destination,key):
        self.type = type
        self.source=source
        self.destination=destination
        self.key=key

    #Decide output file type
    def encode(self):
        if self.type==2:
            self.xmlToCsv()
        elif self.type==3:
            self.xmlToJson()

    #Converting to Csv file
    def xmlToCsv(self):
        rootTree=tree.parse(self.source)
        root = rootTree.getroot()
        csvFile=open(self.destination,"w")
        titles=self.key.split(",")
        csvFile.write(self.key)
        string = str()
        for tag1 in root:#First tag
            tempDict = dict(tag1.attrib)
            if len(tempDict) != 0:
                string +=str(tempDict.get(titles[0])) + ","
            for tag2 in tag1:
                tempDict = dict(tag2.attrib)
                print(tempDict)
                if len(tempDict) != 0:
                    string +=str(tempDict.get(titles[1])) + ","
                temp_num=2
                for tag3 in tag2:
                    tempDict = dict(tag3.attrib)
                    if len(tempDict) != 0:
                        string += tag3.text+","+str(tempDict.get(temp_num)) + ","
                    temp_num+=1
            string += "\n"
        csvFile.write(string)

    #Converting to Json
    def xmlToJson(self):
        rootTree = tree.parse(self.source) #Taking xml file and parsing it
        root = rootTree.getroot() #Root of xml file
        tempDict = dict()
        mainDict=dict()
        titles=str(self.key).split(",")
        indentNum=0
        id=0
        for tag1 in root:
            tempDict[titles[0]] = dict(tag1.attrib).get(titles[0])
            for item in tag1:
                counter=0
                for index in item: #Taking rest of tag of xml file
                    tempDict[titles[counter]]={titles[counter]:index.text }
                    counter+=1
                if indentNum==0:
                    indentNum=counter
            mainDict[id]=tempDict
            id+=1
        with open(self.destination, 'w', encoding='utf8') as json_file:
            json.dump(mainDict, json_file, ensure_ascii=False,skipkeys = True, allow_nan = True,indent=indentNum)




