import logging

logging.basicConfig(filename = "log4.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s' )
class ineuron4:
    logging.info("This is an assignment for Oops classes and objects. The code has been initiated")
    def __init__(self, studentname, emailid, internship,course, job):
        try:
            self.studentname = studentname
            self.emailid = emailid
            self.internship = internship
            self.course = course
            self.job = job
            logging.info("We will now fetch the details of ineuron students")
        except Exception as e:
            logging.exception(e)
Obj_ineuron4 = ineuron4("Asif", "asif1234@gmail", "online", "FSDS", "TCS")
print(Obj_ineuron4.studentname)
print(Obj_ineuron4.emailid)
print(Obj_ineuron4.internship)
print(Obj_ineuron4.course)
print(Obj_ineuron4.job)