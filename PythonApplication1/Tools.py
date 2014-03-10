from random import choice
class File_control(object):
    """description of class"""
    
    def Read_file(self, filepath ,target):
        f = open(filepath, 'r')
        for line in f:
           merkkijono = line.strip()
           target.append(merkkijono)
        f.close()

class Randomizer(object):
    def name(self, gender='Male'):
        firstnames = []
        lastnames = []
        f_nick_name = []
        l_nick_name = []
        full_name = []
        f=File_control()
        try:
            if gender == "Male":
                f.Read_file('source/firstnames.txt', firstnames)
            if gender == "Female":
                f.Read_file('source/female_names.txt', firstnames)

            f.Read_file('source/lastnames.txt', lastnames)
            f.Read_file('source/first_nick_name.txt',f_nick_name)
            f.Read_file('source/last_nick_name.txt',l_nick_name)

            first_name = choice(firstnames)
            second_name = choice(firstnames)
            last_name = choice(lastnames)
            first_nick = choice(f_nick_name)
            last_nick = choice(l_nick_name)

            full_name.append(str.capitalize(first_name))
            full_name.append(str.capitalize(second_name))
            full_name.append(str.capitalize(last_name))
            full_name.append(str.capitalize(first_nick))
            full_name.append(str.capitalize(last_nick))

            return full_name
            
        except Exception:
            pass

        

