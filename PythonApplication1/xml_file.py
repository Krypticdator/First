import xml.etree.ElementTree as ET
class xml_file(object):
    """description of class"""
    def __init__(self):
        self.__elements = {}

    def create_root(self, name):
        name = str(name)
        self.__elements["root"] = ET.Element(name)
    def get_root(self):
        return self.__elements['root']

    def create_element(self, name):
        name = str(name)
        self.__elements[name] = ET.Element(name)

    def create_sub_element(self, child, parent):
        child = str(child)
        created = ET.Element(child)
        self.__elements[parent].append(created)
        self.__elements[child] = created

    def set_value(self, attribute, value, element):
        value = str(value)
        self.__elements[element].set(attribute, value)

    def set_text(self, text, element):
        text = str(text)
        self.__elements[element].text = text
        

    def save_file(self,filepath):
        tree = ET.ElementTree(self.__elements["root"])
        tree.write(filepath)

    def load_file(self, path):
        try:
            tree = ET.parse(path)
            
            self.root = tree.getroot()
            self.__elements['root']=self.root
            return tree
        except Exception:
            return 'error'
        
        

