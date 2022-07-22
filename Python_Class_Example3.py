import logging

logging.basicConfig(filename = "log3.log", level = logging.INFO, format = '%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s' )
class ineuron3:
    logging.info("This is an assignment for Oops classes and objects. The code has been initiated")
    def __init__(self, student, emailid, contact,course, job):
        try:
            self.student = student
            self.emailid = emailid
            self.contact = contact
            self.course = course
            self.job = job
            logging.info("We will now fetch the details of ineuron students")
        except Exception as e:
            logging.exception(e)
Obj_ineuron3 = ineuron3("Asif", "asif1234@gmail", "73389777", "FSDS", "TCS")
print(Obj_ineuron3.student)
print(Obj_ineuron3.emailid)
print(Obj_ineuron3.contact)
print(Obj_ineuron3.course)
print(Obj_ineuron3.job)