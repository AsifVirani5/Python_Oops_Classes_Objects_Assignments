import logging
logging.basicConfig(filename = "log16.log", level = logging.DEBUG, format = '%(asctime)s''%(levelname)s''%(message)s''%(name)s')
logging.info("We are now about to begin writing a code for multilevel inheritance")

class ineuron_techneuron1:
    try:
        def studentname(self):
            studentname = input("Please enter your name")

        def contact(self):
            contact = input("Please enter your contact number for our support executive to reach you out")

        def loc(self):
            loc = input("Please provide your cityname")

        def emailid(self):
            emailid = input("Please provide your email id for us to send you the offer letter")

        def course(self):
            course = input("please provide the course name you are interested in")

        def internship(self):
            internship = input("Are you interested to do internship with ineuron and be a part of next unicon")



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
obj_sudhanshu15.studentname()
obj_sudhanshu15.contact()
obj_sudhanshu15.loc()
obj_sudhanshu15.emailid()
obj_sudhanshu15.course()
obj_sudhanshu15.internship()



