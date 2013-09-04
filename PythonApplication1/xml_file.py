import xml.etree.ElementTree as ET
class xml_file(object):
    """description of class"""
    def __init__(self):
        self.__elements = {}

    def create_root(self, name):
        self.__elements["root"] = ET.Element(name)

    def create_element(self, name):
        self.__elements[name] = ET.Element(name)

    def create_sub_element(self, child, parent):
        created = ET.Element(child)
        self.__elements[parent].append(created)
        self.__elements[child] = created

    def set_value(self, attribute, value, element):
        self.__elements[element].set(attribute, value)

    def set_text(self, text, element):
        self.__elements[element].text = text
        

    def save_file(self):
        tree = ET.ElementTree(self.__elements["root"])
        tree.write("page.xml")

        

