from Convertor.CsvConvert import CsvConvert
from Convertor.JsonConvert import JsonConvert
from Convertor.XmlConvert import XmlConvert
from Convertor.XsdConvert import XsdConvert
import argparse
'''
File Adapter
------------
Given code is decoded here. According to decoding procces, decision which is about which class works, is made.
'''
class FileAdapter:
    def __init__(self):
        parser=argparse.ArgumentParser("File Format Convertor\n6 options exist:\n1.Csv to Xml\n2.Xml to Csv\n3.Xml to Json\n4.Json to Xml\n5.Csv to Json\n6.Json to Csv")
        parser.add_argument('-inp','--input_file',type=str,required=True,help="Target value")
        parser.add_argument('-out','--output_file',type=str,required=True,help="Output File")
        parser.add_argument('-xsd','--xsd_file',type=str,help="Xsd File")
        parser.add_argument('-type','--type_file',type=int,required=True,help="Type")
        parser.add_argument('-key','--key',type=str,help="Titles use , between indexes")
        args=parser.parse_args()
        self.inputfileName=args.input_file
        self.outputFile=args.output_file
        self.type=args.type_file
        if self.type==2 or self.type==3 or self.type==6 or self.type==4:
            self.key=args.key
    #Decision making
    def decode(self): 
        if self.type==1 or self.type==5:
            csvConvertor=CsvConvert(self.type,self.inputfileName,self.outputFile)
            csvConvertor.encode()
        elif self.type==2 or self.type==3:
            xmlConvertor=XmlConvert(self.type,self.inputfileName,self.outputFile,self.key)
            xmlConvertor.encode()
        elif self.type==4 or self.type==6:
            jsonConvertor=JsonConvert(self.type,self.inputfileName,self.outputFile,self.key)
            jsonConvertor.encode()
        elif self.type==7:
            xsdConvertor=XsdConvert(self.inputfileName,self.outputFile)
            xsdConvertor.validate()
        else:
            self.error=2