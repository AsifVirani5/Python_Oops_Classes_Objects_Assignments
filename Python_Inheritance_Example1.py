import logging
logging.basicConfig(filename = "log12.log", level = logging.DEBUG, format = '%(asctime)s''%(levelname)s''%(message)s''%(name)s')
logging.info("In this example, we are going to see how inheritance in Oops concept works. let us now initiate the code")

class ineuron12:
    def __init__(self, name, contact, course, job, internship):
        try:
            self.name = name
            self.contact = contact
            self.course = course
            self.job = job
            self.internship = internship

        except Exception as e:
            logging.exception(e)

# Let us now instantiate an object for the class

Obj_sudhanshu12 = ineuron12("Sudhanshu", "7335675", "FSDS", "ineuron", "Online")
print(Obj_sudhanshu12.job)

# Now, Lets add a child class called ineuron13 and see if we can call the parent class data
class ineuron13(ineuron12):
    pass

#Now, lets instantiate the object for the child class

obj_sudhanshu13 = ineuron13("Sudhanshu1", "722345", "FSDS1", "ineuron1", "online1")
print(obj_sudhanshu13.internship)

# Lets us now try to inherit the entities of parent class by calling parent class object
print(Obj_sudhanshu12.internship)





