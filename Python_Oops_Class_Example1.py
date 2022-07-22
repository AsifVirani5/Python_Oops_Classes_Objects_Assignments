# Assignment Oops by Sudhanshu Sir.
#Instruction : you have to make sure that use ineuron studnets , class , class type , number of courses
#, affiliates , blog, internship , jobs as a reference example
# Class Topic

#import pandas as pd
#import numpy as np
import logging
logging.basicConfig(filename = "log1.log", level = logging.DEBUG, format='%(asctime)s' '%(levelname)s' '%(name)s' '%(message)s' )
class ineuron:
    logging.info("This is an assignment for Oops classes and objects. The code has been initiated")


    def __init__(self, name, class1, classtype, noofcourses, internship, jobs):
        try:
            self.name = name
            self.class1 = class1
            self.classtype = classtype
            self.noofcourses = noofcourses
            self.internship = internship
            self.jobs = jobs


        except Exception as e:
           logging.exception(e)

obj_ineuron = ineuron("Asif", "FSDS", "DATA SCIENCE", "1", "onlineinternship", "TCS")
print(obj_ineuron.name)
print(obj_ineuron.class1)
print(obj_ineuron.classtype)
print(obj_ineuron.noofcourses)
print(obj_ineuron.internship)
print(obj_ineuron.jobs)








