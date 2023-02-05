from objects.Department.Department import Department
from objects.Home.Room import Room
from objects.Subscription.Plan import SubscriptionPlan
from objects.Family.Family import Family
from colorama import Fore, Back, Style
import requests
import random


room_bathroom = Room('Street, 5a', 'bathroom')
room_livingroom = Room('Street, 5a', 'limingroom')
room_badroom = Room('Street, 5a', 'badroom')

subscription_home1 = SubscriptionPlan('week', room_badroom.address)
family1 = Family([{'name': 'Joe', 'age': 12}, {'name': 'Kitty', 'age': 21}])
home1_department = Department('department1')
home2_department = Department('department2')
home1 = {'address': room_bathroom.address,
         'room_list': [room_badroom, room_livingroom, room_bathroom],
         'floors': 2,
         'owner': 'Joe Brawn',
         'department': home1_department,
         'account': {
             'subscription_plan': subscription_home1,
             'balance': 0
         },
         'family': family1.family_list }


room_bathroom_h2 = Room('Street, 1a', 'bathroom')
room_livingroom_h2 = Room('Street, 1a', 'livingroom')
room_bedroom_h2 = Room('Street, 1a', 'bedroom')
subscription_home2 = SubscriptionPlan('year', room_bedroom_h2.address)
family2 = Family([{'name': 'Joe2', 'age': 12}, {'name': 'Kitty2', 'age': 21}])

home2 = {'address': room_bathroom.address,
         'room_list': [room_bedroom_h2, room_livingroom_h2, room_bathroom_h2],
         'floors': 3,
         'owner': 'Smith Baker',
         'department': home2_department,
         'account': {
             'subscription_plan': subscription_home2,
             'balance': 120
         },
         'family': family2.family_list}


homes = [home1, home2]

for home in homes:
    if home['account']['balance'] <= 0:
        home_department = home['department']
        print(Fore.RED + 'department',home_department.name)
        print('Home address', home['address'])
        print('Home owner:', home['owner'])
        home_subscription = home['account']['subscription_plan']
        print('Subscription:', home_subscription.subscription_type)
        print('Family list:')
        for item in home['family']:
            print(item['name'])
        print('=====================================================')
    else:
        home_department = home['department']
        print(Fore.GREEN + 'department', home_department.name)
        print('Home address', home['address'])
        print('Home owner:', home['owner'])
        home_subscription = home['account']['subscription_plan']
        print('Subscription:', home_subscription.subscription_type)
        print('Family list:')
        for item in home['family']:
            print(item['name'])
        print('=====================================================')

home = open('homes.txt', 'r')
homes = home.read()
home.close()
homes_list = homes.split(',')
result_for_file = ""
for item_list in homes_list:
    print(item_list)
    result_for_file = result_for_file + item_list + '_next_record,'

print(result_for_file)
home_file = open('homes.txt', 'w')
home_file.write(result_for_file)
home_file.close()

#
# Create Read Update Delete system
result_html = open('result_dogs.html', 'w')

first_tag = '''
<html>
  <div style="display:flex; flex-direction:column">
'''

last_tag = '''
</div>
</html>
'''

dogs = ""

for get_dog_item in range(1, 2):
    resultDog = requests.get('https://dog.ceo/api/breeds/image/random')
    resultText = resultDog.json()
    print(resultText['message'])
    print(random.randrange(10, 100))
    dogs = dogs + '''
    <div>
      <img src="''' + resultText['message']+ '''" /></div>'''

html_file_result = first_tag + dogs + last_tag
result_html.write(html_file_result)




