import logging
logging.basicConfig(filename = "log19.log", level = logging.DEBUG, format = '%(asctime)s''%(levelname)s''%(message)s''%(name)s')
logging.info("In this multi level inheritance, we will see how if a same method or function is define in two different classes, we can only call the last method or function and not the first")

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

class ineuron_techneuron_analysis(ineuron_techneuron1):
    try:
#Here, We are defining the same method called studentname that we had already define in the previous class
        logging.info("Now, We are defining the same method called studentname that we had already define in the previous class")
        def studentname(self):
            studentname = input("These are filtered students lists")

        def total_no_of_students(self):
            print("The total number of students enrolled for techneuron is 1.5 million")

    except Exception as e:
           logging.exception(e)


class ineuron_techneuron_Revenue(ineuron_techneuron_analysis):
    pass

obj_sudhanshu15 = ineuron_techneuron_Revenue()
obj_sudhanshu15.studentname() # Here, we are calling the duplicate method name and it will call the latest method only
obj_sudhanshu15.contact()
obj_sudhanshu15.loc()
obj_sudhanshu15.emailid()
obj_sudhanshu15.course()
obj_sudhanshu15.internship()



