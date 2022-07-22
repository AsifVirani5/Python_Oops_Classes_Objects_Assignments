import logging
logging.basicConfig(filename = "log18.log", level = logging.DEBUG, format = '%(asctime)s''%(levelname)s''%(message)s''%(name)s')
logging.info("In this multiple inheritance example, we are going to see how we can call entities from a child class based on priority")

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
        def studentname(self):
            studentname = input("This is a filtered students lists")

        def total_no_of_students(self):
            print("The total number of students enrolled for techneuron is 1.5 million")

    except Exception as e:
           logging.exception(e)

#Let us see that we can call entities from a child class based on its priority simply by parsing the class name as an argument depends on its priority"
class ineuron_techneuron_Revenue(ineuron_techneuron_analysis,ineuron_techneuron1):
    pass

obj_sudhanshu16 = ineuron_techneuron_Revenue()
obj_sudhanshu16.studentname()
obj_sudhanshu16.contact()
obj_sudhanshu16.loc()
obj_sudhanshu16.emailid()
obj_sudhanshu16.course()
obj_sudhanshu16.internship()



