from Settings import Settings
class item(object):
    """description of class"""
    def __init__(self):
        self.__attributes = {}
        self.__actions = []
        self.__definitions = []
        self.__needed_item_types = []
        self.__effects = {}
        self.__linked_items = {}

    def define_quality(self):
        s = Settings()
        #try:
        quality = self.__attributes["quality"]
        quality_text = s.quality_rating[quality]
        self.__attributes["quality_text"] = quality_text
        #except Exception:
         #   print("error in define quality")
            

    def set_quality(self, quality):
        self.__attributes["quality"] = quality

    def set_attribute(self, attribute, value):
        self.__attributes[attribute] = value

    def get_attribute(self, attribute):
        return self.__attributes[attribute]

    def add_linked_item(self, item):
        self.__linked_items[item.get_attribute("type")] = item
        


