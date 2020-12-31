def create_record (name,telephone, address):
      record = {
        'name': name,
        'phone': telephone,
        'address': address,
              }
      return record
user1 = create_record ("Vasia","123456789456", "Tinusia")
user2 = create_record ("Peya","98564884", "Likusia")
print(user1)
print(user2)

def give_award (medal, *persons):
    for person in persons:
        print("Tovarish " +person.title()+" nagrajdenie medaliu" +medal)

give_award("Za Berlin ", "Vasia1")
give_award("Za London ", "Vasia1","Petia","Valentin")
