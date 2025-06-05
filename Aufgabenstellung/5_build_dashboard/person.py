import json
from PIL import Image

def get_person_data():
    """
    Returns the person data loaded from the JSON file.
    """
    with open("data/person_db.json", "r", encoding="utf-8") as file:
        person_data = json.load(file)

    person_object_list = []
    for person_dict in person_data:
        person_object = Person( person_dict["id"],
                                person_dict["date_of_birth"],
                                person_dict["firstname"],
                                person_dict["lastname"],
                                person_dict["picture_path"],
                                person_dict["ekg_tests"],
                                person_dict["gender"]
                                )
        person_object_list.append(person_object)
    return person_object_list


def get_person_object_by_full_name(full_name):
    persons = get_person_data()
    firstname = full_name.split(", ")[1]
    lastname = full_name.split(", ")[0]

    for person in persons:
        if person.firstname==firstname and person.lastname==lastname:
            return person

class Person:

    def __init__(self, id : int, date_of_birth : int, firstname, lastname, picture_path, ekg_tests, gender = "Male"):
        self.id = id
        self.date_of_birth = date_of_birth
        self.firstname = firstname
        self.lastname = lastname
        self.picture_path = picture_path
        self.ekg_tests = ekg_tests
        self.hr_max = 220 - (2025-int(date_of_birth))
        self.gender = gender


    def set_hr(self, hr):
        self.hr_max = hr

    def get_full_name(self):
        return self.lastname + ", " + self.firstname


    def get_image(self):
        image = Image.open(self.picture_path)
        return image
    



if __name__ == "__main__":
    print("This is a module with some functions to read the person data")
    persons = Person.load_person_data()
    person_names = Person.get_person_list(persons)
    print(person_names)
    print(Person.find_person_data_by_name("Huber, Julian"))