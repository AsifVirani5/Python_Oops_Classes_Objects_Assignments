import logging
logging.basicConfig(filename = "log11.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(message)s' )
logging.info("In this example, we will write a code and add private class variables")
class ineuron11:
    def __init__(self, name, contact, course, internship, blogs):
        try:
            self.name = name
            self.__contact = contact
            self.course = course
            self.internship = internship
            self.blogs = blogs

        except Exception as e:
            logging.exception(e)

# Lets, instantiate the objects

Obj_sudhanshu11 = ineuron11("Sudhanshu", "73379734", "fsds", "online", "linkedin")

#Lets try to access protected class variable which is indicated with "__" and it can be called by using "object._classname__classvariablename".
print(Obj_sudhanshu11._ineuron11__contact)