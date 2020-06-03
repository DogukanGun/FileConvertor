from lxml import etree

"""
XsdConvert
----------
XML file is checked by xsd file.
"""
class XsdConvert:
    def __init__(self,source,destination):
        self.destination=destination
        self.source=source

    def validate(self):
        xmlschema_doc = etree.parse(self.source)
        xmlschema = etree.XMLSchema(xmlschema_doc)
        xml_doc = etree.parse(self.destination)
        print(xmlschema.validate(xml_doc))