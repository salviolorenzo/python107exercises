ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}
#Write a python expression that gets the email address of Ramit.
email = ramit['email']
print (email)

#Write a python expression that gets the first of Ramit's interests.
interest = ramit['interests'][0]
print(interest) 

#Write a python expression that gets the email address of Jasmine.
jasmine = ramit['friends'][0]['email']
print(jasmine)

#Write a python expression that gets the second of Jan's two interests.
jan = ramit['friends'][1]['interests'][1]
print(jan)