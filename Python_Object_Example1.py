import logging
logging.basicConfig(filename = "log6.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s')
class ineuron6:
    logging.info("This is an example of single object which is otherwise known as entity. The code is initiated..")
    def __init__(self, name, emailid, contact, classes, course, job):
        try:
            self.name = name
            self.emailid = emailid
            self.contact = contact
            self.classes = classes
            self.course = course
            self.job = job
        except Exception as e:
            logging.exception(e)
# Now, let's instantiate an object otherwise known as entity
obj_asif = ineuron6("asif", "asif@gmail.com","7333733", "FSDS1", "FSDS", "TCS")
#Now, Lets call the above object and print the data one by one
print(obj_asif.name)
print(obj_asif.job)
print(obj_asif.course)
print(obj_asif.emailid)


