import logging
logging.basicConfig(filename = "log13.log", level = logging.DEBUG, format = '%(asctime)s''%(levelname)s''%(message)s''%(name)s')
logging.info("In this example2, we are going to see how inheritance in Oops concept works. let us now initiate the code")

class ineuron12:
    def __init__(ineuronstars, name, contact, course, job, internship, blog):
        try:
            ineuronstars.studentname = name #Here, we can provide any class variable name and constructor name(self)
            ineuronstars.contact = contact
            ineuronstars.course = course
            ineuronstars.job = job
            ineuronstars.internship = internship
            ineuronstars.blog = blog

        except Exception as e:
            logging.exception(e)

# Let us now instantiate an object for the class

Obj_sudhanshu12 = ineuron12("Sudhanshu", "7335675", "FSDS", "ineuron", "Online", "linkedin")
print(Obj_sudhanshu12.job)

# Now, Lets add a child class called ineuron13 and see if we can call the parent class data
class ineuron13(ineuron12):
    pass

#Now, lets instantiate the object for the child class

obj_sudhanshu13 = ineuron13("Sudhanshu1", "722345", "FSDS1", "ineuron1", "online1", "linkedin1")
print(obj_sudhanshu13.studentname)

# Lets us now try to inherit the entities of parent class by calling parent class object
print(Obj_sudhanshu12.internship)





