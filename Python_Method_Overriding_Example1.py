import logging
logging.basicConfig(filename= "log25.log", level = logging.DEBUG, format = ' %(asctime)s ' ' %(levelname)s ' ' %(message)s ')
logging.info("In this example, we will see how method overriding works. As the name suggest, when the same method is written with a different logic inside a child class and we try to call the this duplicated method then it will show the result of the child class method and not the parent class. This is the meaning of method overriding")

class ineuron_fsds:
    try:
        def name(self):
            name = input("Please enter your name")

        def application_id(self):
            application_id = input("Please share us your application id")

    except Exception as e:
        logging.exception(e)

class ineuron_star_performer_fsdsbatch(ineuron_fsds):
    try:
        logging.info("we are creating a duplicate method called name with different logic below to see how method overriding works")
        def name(self):
            print("Ineuron star performer for the month of July'22 is Asif")


    except Exception as e:
        logging.exception(e)

Obj_sudhanshu25 = ineuron_star_performer_fsdsbatch()
Obj_sudhanshu25.name()

