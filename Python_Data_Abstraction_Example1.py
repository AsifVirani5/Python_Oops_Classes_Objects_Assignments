import logging
logging.basicConfig(filename= "log27.log", level = logging.DEBUG, format = ' %(asctime)s ' ' %(levelname)s ' ' %(message)s ')
logging.info("In this example, we will see how we are hiding a variable from the person who is trying to access it. This  phenomenon is called data Abstraction. We are making it private variable and hiding the accessibility")

class ineuronventurefunding:
    __funding = "One billion dollars"
    try:
        def ineuron_worldbank_funding(self):
            print("ineuron total funding received for 2022 is Two billion dollars")

    except Exception as e:
        logging.exception(e)

i =  ineuronventurefunding()


#Lets try to access the class variable normally

i.ineuron_worldbank_funding


#lets try to access the class variable __funding by using the _classvariable__funding

print(i._ineuronventurefunding__funding)

