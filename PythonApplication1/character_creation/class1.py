class ModDemo(object):
    """description of class"""

    def viidellaJaollinen(syote):
        if syote % 5 == 0:
            return True
        else:
            return False

    def __init__(self):
        for i in range(0, 11):
            print("Onko luku " + i + " viidella jaollinen" + self.viidellaJaollinen())
