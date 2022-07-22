import logging
logging.basicConfig(filename = "log8.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s')
logging.info("We are about to start our object example 3 code")
class ineuron7:
    def __init__(self, student, contact, course, job,yob):
        try:
            self.student = student
            self.contact = contact
            self.course = course
            self.job = job
            self.yob = yob
        except Exception as e:
            logging.exception(e)

    def age(self, current_year):
        logging.info("We are now trying to find the age of students in ineuron to better understand how we call function age using the object or entity")
        try:
            return current_year - self.yob

        except Exception as e:
            logging.exception(e)


# Lets, use multiple objects and multiple data otherwise known as multiple entities
obj_anuj = ineuron7("anuj", "777744455", "FSDS", "ineuron", 1994)
obj_swapna = ineuron7("swapna", "77756455", "FSDS", "ineuron", 1995)
obj_sudhanshu = ineuron7("sudhanshu", "777124455", "FSDS", "ineuron", 1999)
obj_Krish = ineuron7("krish", "777364455", "FSDS", "ineuron", 1989)
obj_sunny = ineuron7("sunny", "7777544455", "FSDS", "ineuron", 1987)

#Lets print these multiple entities or objects of the class
print("This is the age", obj_anuj.age(2022))
print(obj_swapna.course)
print(obj_sudhanshu.job)
print(obj_Krish.student)
print(obj_sunny.course)
print(obj_sudhanshu.yob)













