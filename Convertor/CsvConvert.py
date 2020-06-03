from lxml import etree as etree
import json
"""
JsonConvert
----------- 
According to demand,file is converted to a new file (Xml or Csv)
"""
class CsvConvert:
    def __init__(self,type,source,destination):
        self.type=type
        self.source=source
        self.destination=destination

    # Decide output file type
    def encode(self):
        if self.type==1:
            self.convertToXml()
        elif self.type==5:
            self.convertToJson()

    # Converting to Xml file
    def convertToXml(self):
        f = open(self.source, "r",encoding='utf-8')
        root = etree.Element(str(self.source)[:int(str(self.source).index("."))])
        titles = []
        counter = 0
        id=0
        for index in f:
            if counter == 0:
                titles = index.split(";")
                counter += 1
            else:
                fileArray = (index.split(";"))
                xmlRow=etree.SubElement(root,"row")
                xmlRow.set("id",str(id))
                item=etree.SubElement(xmlRow, "item")
                temp_counter=0
                for row in fileArray:
                    try:
                        tempItem=etree.SubElement(item,titles[temp_counter])
                        tempItem.set("value",row)
                        temp_counter+=1
                    except Exception :
                        pass
                id+=1
        mydata = etree.tostring(root, pretty_print=True, encoding="unicode")
        myfile = open(self.destination, "w")
        myfile.write(mydata)

    # Converting to Json
    def convertToJson(self):
        jsonfile = open(self.destination, 'w')
        f = open(self.source, "r")
        counter=0
        mainDict=dict()
        id=0
        indentNum=0
        for index in f:
            if counter==0:
                titleList = index.split(",")
                mainDict[counter]=titleList
            else:
                fileArray=index.split(",")
                tempDict=dict()
                tempDict[id]={titleList[0]:fileArray[0]}
                tempDict[str(str(id)+"-items")]={titleList[1]:fileArray[1]}
                temp_index=2

                for item_index in fileArray:
                    tempDict[str(str(id)+"-items")][titleList[temp_index]]=item_index
                    temp_index+=1
                if indentNum == 0:
                    indentNum = counter
                mainDict[id]=tempDict
                id+=1
            counter += 1
        jsonfile.write(json.dumps(mainDict,ensure_ascii=False,skipkeys = True, allow_nan = True,indent=indentNum))


