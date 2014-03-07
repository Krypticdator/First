class GameObject(object):
    """description of class"""
    def __init__(self):
        self.__attributes = {}

    def set_attribute(name, value):
        self.__attributes[name] = value

    def get_attribute(name):
        try:
            return self.__attributes[name]
        except Exception:
            return 'failed'


