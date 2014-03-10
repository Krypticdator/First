import xml.etree.ElementTree as ET
class xml_control(object):
    """description of class"""
    def __init__(self):
        pass
    def create_xml_file(self, root_name, path):
        self.root=ET.Element(root_name)
        self.tree=ET.ElementTree(self.root)
        
        self.tree.write(path)
    
    def load_xml_file(self, path):
        try:
            self.tree = ET.parse(path)
            self.root = self.tree.getroot()
        except Exception:
            print('whoops xml load')

    def add_child_element(self, parent, child_name):
        child = ET.Element(child_name)
        ET.SubElement(self.tree.find(parent), child)
    def add_to_root(self, child_name):
        child = ET.Element(child_name)
        ET.SubElement(self.root, child)


    def save(self):
        self.tree.write(path)


