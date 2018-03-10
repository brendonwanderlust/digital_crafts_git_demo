class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []

    def print_contact_info(self):
        print "%s's email: %s, s phone number: %s" % (self.name, self.email, self.name, self.phone)    
    
    def add_friend(self, friend):
        self.friends.append(friend)
    
    def num_friends(self):
        print len(self.friends)

    

brendon = Person('Brendon', 'brendoncarrasquillo@gmail.com', '770.335.9529')
charlie = Person('Charlie', 'charlie@gmail.com', '770.555.1234')

brendon.add_friend(charlie)
print brendon.friends[0].name
brendon.num_friends()

# class vehicle(object):
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model 
#         self.year = year

#     def print_info(self):
#         print self.make
#         print self.model 
#         print self.year
    
# my_dream_car = vehicle('Jeep', 'Wrangler', '1998')
