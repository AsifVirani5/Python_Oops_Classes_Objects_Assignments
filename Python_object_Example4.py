import logging
logging.basicConfig(filename = "log9.log", level = logging.DEBUG, format = '%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s')
logging.info("We are about to initiate multiple functions to get input from the users without the constructor __init__ and call the input functions using the objects")
class ineuron8:
    try:
        def age(self, current_year, Year_of_birth):
            return current_year - Year_of_birth

        def name(self):
            name = input("Please enter your name")
            return name

        def emailid(self):
            emailid = input("Tell me your emailid")
            return emailid

        def course(self):
            course = input("Please tell me the course you are interested in")
            return course

        def job(self):
            job = input("Please tell me what type of job you are interested in")
            return job

        def internship_input(self, internship):
            print("Please tell me if you are interested in internship at ineuron " , internship)

    except Exception as e:
         logging.exception(e)

# Now, lets try to instantiate the objects with parsing any data as we have not defined constructor

obj_sudhanshu8 = ineuron8()
obj_krish = ineuron8()
obj_motwani = ineuron8()


#Now, lets get the input from these users
obj_sudhanshu8.emailid()
obj_krish.internship_input("yes")
obj_krish.course()
obj_motwani.job()
