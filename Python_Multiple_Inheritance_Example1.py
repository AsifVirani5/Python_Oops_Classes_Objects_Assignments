import logging
logging.basicConfig(filename = "log17.log", level = logging.DEBUG, format = '%(asctime)s''%(levelname)s''%(message)s''%(name)s')
logging.info("We are now about to begin writing a code for multilevel inheritance")

class ineuron_techneuron1:
    try:
        def studentname(self):
            print("This will take the studentname input")

        def contact(self):
            print("Please provide your contact number")

        def loc(self):
            print("please provide your location")

        def emailid(self):
            print("please provide your email id")

        def course(self):
            print("please provide the course name you are interested in")

        def internship(self):
            print("Are you interested to do internship with ineuron and be a part of next unicon")



    except Exception as e:
           logging.exception(e)

class ineuron_techneuron_analysis():
    try:
        def total_no_of_students(self):
            print("The total number of students enrolled for techneuron is 1.5 million")

    except Exception as e:
           logging.exception(e)


class ineuron_techneuron_Revenue(ineuron_techneuron1,ineuron_techneuron_analysis):
    pass

obj_sudhanshu15 = ineuron_techneuron_Revenue()
obj_sudhanshu15.emailid()
obj_sudhanshu15.total_no_of_students()
