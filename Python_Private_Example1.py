import logging
logging.basicConfig(filename = "log10.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(message)s' )
logging.info("In this example, we will write a code and add private class variables")
class ineuron10:
    def __init__(self, name, contact, course, internship, blogs):
        try:
            self.name = name
            self._contact = contact
            self.course = course
            self.internship = internship
            self.blogs = blogs

        except Exception as e:
            logging.exception(e)

# Lets, instantiate the objects

Obj_sudhanshu10 = ineuron10("Sudhanshu", "73379734", "fsds", "online", "linkedin")

#Lets try to access private class variable which is indicated with "_"
print(Obj_sudhanshu10._contact)