people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    update_people = [] # Create an empty list to store the new people

    for person in people:
        if person != person_name:
            update_people.append(person)

    return update_people

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
