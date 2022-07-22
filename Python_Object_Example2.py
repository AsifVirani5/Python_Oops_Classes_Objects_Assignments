import logging
logging.basicConfig(filename = "log7.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s')
logging.info("We are about to start our object example 2 code")
class ineuron7:
    def __init__(self, student, contact, course, job,):
        try:
            self.student = student
            self.contact = contact
            self.course = course
            self.job = job
        except Exception as e:
            logging.exception(e)
# Lets, use multiple objects and multiple data otherwise known as multiple entities
obj_anuj = ineuron7("anuj", "777744455", "FSDS", "ineuron")
obj_swapna = ineuron7("swapna", "77756455", "FSDS", "ineuron")
obj_sudhanshu = ineuron7("sudhanshu", "777124455", "FSDS", "ineuron")
obj_Krish = ineuron7("krish", "777364455", "FSDS", "ineuron")
obj_sunny = ineuron7("sunny", "7777544455", "FSDS", "ineuron")

#Lets print these multiple entities or objects of the class
print(obj_anuj.contact)
print(obj_swapna.course)
print(obj_sudhanshu.job)
print(obj_Krish.student)
print(obj_sunny.course)



