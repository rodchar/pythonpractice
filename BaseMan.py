class BaseMan(object):
    #age = None
    #job = None
    #address = None

    def __init__(self, name):
        self.name = name
        self.age = None
        self.job = None
        self.address = None

    def set_age(self, age):
        if isinstance(age, int):
            self.age = age
        else:
            raise TypeError("Must be an int")

    def set_job(self, job):
        if job != self.job:
            self.job = job

    def set_address(self, address):
        if address != self.address:
            self.address = address

    def great_peeps(self):

        print("Hello peeps, my name is {}".format(self.name))

class Cory(BaseMan):
    def __init__(self):
        BaseMan.__init__(self, 'Cory')
    def execute_skill(self):
        print("I can do headstand")

#Start
cory = Cory()
cory.set_age(3)
print(cory)
print(cory.age)
