
import json
from lxml import etree as tree
"""
JsonConvert
----------- 
According to demand,file is converted to a new file (Xml or Csv)
"""
class JsonConvert:
    def __init__(self, type,source,destination,key):
        self.type = type
        self.source=source
        self.destination=destination
        self.key=key

    # Decide output file type
    def encode(self):
        if(self.type==4):
            self.jsonToXml()
        elif self.type==6:
            self.jsonToCsv()

    # Converting to Csv file
    def jsonToCsv(self):
        self.jsonfile = open(self.source, 'r', encoding='utf-8')
        self.data = dict()
        string=str()
        self.data = dict(json.load(self.jsonfile))
        csvwriter = open(self.destination,"w")
        number=len(self.data)
        titles=str(self.key).split(",")
        string+=self.key
        id=0
        for index in range(number):
            dict_=self.data.get(str(index))

            string+=str(dict_.get(str(index))[titles[0]])+","
            print(dict_.get(str(index)+"-items"))
            for index2 in range(1,len(titles)):
                try:
                    string+=str(dict_.get(str(index)+"-items")[titles[index2]])+","
                except Exception as E:
                    pass
        csvwriter.write(string)

    # Converting to Xml
    def jsonToXml(self):
        self.jsonfile = open(self.source, 'r', encoding='utf-8')
        self.data = dict()
        self.data = dict(json.load(self.jsonfile))
        root = tree.Element(str(self.destination)[:int(str(self.destination).index("."))])
        counter=0
        id=0
        for index in range(len(self.data)):
            if counter == 0:
                titles = self.key.split(",")
                counter += 1
            else:
                print(titles)
                index_ = self.data.get(str(index-1))
                fileArray = (index_.get(str(index-1)))
                print(fileArray[titles[0]])
                xmlRow=tree.SubElement(root,"row")
                xmlRow.set("id",str(id))
                item=tree.SubElement(xmlRow, "item")
                item.set("value",fileArray.get(titles[0]))
                temp_counter=0
                fileArray=index_.get(str(index-1)+"-items")
                for row in fileArray.values():
                    tempItem=tree.SubElement(item,titles[temp_counter])
                    tempItem.set("value",row)
                    temp_counter+=1
                id+=1
        mydata = tree.tostring(root, pretty_print=True, encoding="unicode")
        myfile = open(self.destination, "w")
        myfile.write(mydata)
