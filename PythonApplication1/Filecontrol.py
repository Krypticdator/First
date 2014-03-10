class Filecontrol(object):
    """description of class"""
    def __init__(self):
        self.segmented_file_array = []
    def read_file(self, filepath ,target):
        f = open(filepath, 'r')
        for line in f:
           merkkijono = line.strip()
           target.append(merkkijono)
        f.close()

    def read_file_to_segments(self, filepath, separator, external_array = False):
        f = open(filepath, 'r')
        if external_array:
            array = []

        for line in f:
            merkkijono = line[:-1]
            rivitiedot = merkkijono.split(separator, -1)
            if external_array == False:
                self.segmented_file_array.append(rivitiedot)
            else:
                array.append(rivitiedot)
        f.close()
        if external_array:
            return array

