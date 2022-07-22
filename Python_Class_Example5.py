import logging

logging.basicConfig(filename = "log4.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s' )
class ineuron5:
    logging.info("This is an assignment for Oops classes and objects. The code has been initiated")
    def __init__(self, name, classes, classtype, emailid, internship,course, job, affiliates, blogs):
        try:
            self.name = name
            self.classes = classes
            self.classtype = classtype
            self.emailid = emailid
            self.internship = internship
            self.course = course
            self.job = job
            self.affiliates = affiliates
            self.blogs = blogs
            logging.info("We will now fetch the details of ineuron students")
        except Exception as e:
            logging.exception(e)
Obj_ineuron5 = ineuron5("Asif", "FSDS1", "DATA SCIENCE", "asif1234@gmail", "online", "FSDS", "TCS", "musigma", "linkedinblogs")
print(Obj_ineuron5.name)
print(Obj_ineuron5.classes)
print(Obj_ineuron5.classtype)
print(Obj_ineuron5.emailid)
print(Obj_ineuron5.internship)
print(Obj_ineuron5.course)
print(Obj_ineuron5.affiliates)
print(Obj_ineuron5.blogs)