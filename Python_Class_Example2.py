# Class 2
import logging
logging.basicConfig(filename = "log2.log", level = logging.DEBUG, format='%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s' )
class ineuron1:
    logging.info("This is an assignment for Oops classes and objects. The code has been initiated")


    def __init__(self, studentname, affiliates, blogs):
        try:
            self.studentname = studentname
            self.affiliates = affiliates
            self.blogs = blogs



        except Exception as e:
           logging.exception(e)

obj_ineuron1 = ineuron1("Asif", "musigma", "DATA SCIENCE")
print(obj_ineuron1.studentname)
print(obj_ineuron1.affiliates)
print(obj_ineuron1.blogs)














