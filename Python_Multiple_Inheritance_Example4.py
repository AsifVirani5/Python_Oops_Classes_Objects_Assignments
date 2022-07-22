import logging
logging.basicConfig(filename= "log23.log", level = logging.DEBUG, format = ' %(asctime)s ' ' %(levelname)s ' ' %(message)s ')
logging.info("In this example, we will see how we can call as many classes as possible without rewriting the methods or functions and this will be useful in real time when we want to call all the classes developed by multiple people")

class ineuron_Personal:
    try:
        logging.info("We need your personal details to process your ineuron application")
        def studentname(self):
            studentname = input("Please enter your name")

        def emailid(self):
            emailid = input("Please tell me your email id")

        def contact(self):
            contact = input("please enter your contact number for our executive to reach you out")

        def course(self):
            course = input("Please tell me the name of the course you are interested in")

        def internship(self):
            internship = input("Please let us know if you are interested in ineuron internships")

    except Exception as e:
        logging.exception(e)

class Ineuron_FSDS_stats:
    try:
        def total_no_of_student(self):
            print("The total number of students enrolled are 1.5 million")

        def total_no_of_students_internship(self):
            print("The total number of students enrolled for internship are 50million")

        def students_experienced(self):
            print("The total students who are above 8 years are 40 million")

        def student_freshers(self):
            print("The total students who are freshers are 1.1 million")

    except Exception as e:
        logging.exception(e)

class ineuron_faculty_stats:
    try:
        def total_employees(self):
            print("The total ineuron employees are 500")

    except Exception as e:
        logging.exception(e)

class student_location:
    try:
        def total_employees(self):
            print("The total ineuron employees are 500")

        def south(self):
            print("Total application received from south is 50 million")

        def north(self):
            print("total application received from north is 80million")

        def east(self):
            print("total application received from east is 50lakhs")

        def west(self):
            print("total application received from west is 1lakhs")

    except Exception as e:
        logging.exception(e)

class Ineuron_Hiring(student_location,ineuron_Personal,Ineuron_FSDS_stats):
    try:
        def south_hiring(self):
            print("Ineuron needs to hire minimum of 80 lakhs data scientist for south in this year")

        def north_hiring(self):
            print("Ineuron must hire atleast 1million Data Scientist for north within this year")

        def east_hiring(self):
            print("Ineuron must hire 50thousand data scientist for east")

        def west_hiring(self):
            print("Ineuron must hire atleast 1 lakh data scientist for west location")

    except Exception as e:
        logging.exception(e)

obj_sudhanshu23 =  Ineuron_Hiring()
obj_sudhanshu23.total_employees()
obj_sudhanshu23.studentname()
obj_sudhanshu23.emailid()
obj_sudhanshu23.contact()
obj_sudhanshu23.internship()
obj_sudhanshu23.course()
obj_sudhanshu23.total_no_of_student()
obj_sudhanshu23.total_no_of_students_internship()
obj_sudhanshu23.students_experienced()
obj_sudhanshu23.student_freshers()
obj_sudhanshu23.south()
obj_sudhanshu23.north()
obj_sudhanshu23.west()
obj_sudhanshu23.east()
obj_sudhanshu23.south_hiring()
obj_sudhanshu23.east_hiring()
obj_sudhanshu23.north_hiring()
obj_sudhanshu23.west_hiring()






