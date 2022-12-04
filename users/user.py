from data.dataBase import data


class User():
    def __init__(self,id:str) -> None:
        self._id = id
        self._name = ""
        self._email = ""
        self._age = 0
        self._city = ""

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name
    
    @property
    def email(self):
        return self._email
    
    @property
    def age(self):
        return self._age
    
    @property
    def city(self):
        return self._city
    
    @name.setter
    def name(self, world):
        self._name = world
    
    @email.setter
    def email(self, gmail):
        self._gmail = gmail
    
    @age.setter
    def age(self, agee):
        self._age = agee
    
    @city.setter
    def city(self, state):
        self._city = state

    def add_user(self,name,email,age,city):
        self._name = name
        self._email = email
        self._age = age
        self._city = city

    def convert_to_dict(self):
        return {"id": self.id,"name" : self.name, "email" : self.email,"age": self.age, "city":self.city}
        
    def create_user(self):
        data.append(self.convert_to_dict()) 
    
    def delete_user(self,id):
        for c in range(len(data)):
            if data[c]['id'] == id:
                data.pop(c)
                return
    
    def read_unique_user(self,id):
        for c in range(len(data)):
            if data[c]['id'] == id:
                return data[c]
    
    def read_all_users(self):
        return data
    
    def update_user(self,id,name,age,city):
        for c in range(len(data)):
            if data[c]['id'] == id:
                data[c]['name'] = name
                data[c]['age'] = age
                data[c]['city'] = city