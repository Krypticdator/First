class GameObject(object):
    """description of class"""
    def __init__(self):
        self.__attributes = {}

    def set_attribute(self, name, value):
        self.__attributes[name] = value

    def get_attribute(self, name):
        try:
            return self.__attributes[name]
        except Exception:
            return 0


