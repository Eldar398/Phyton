from objects.Department.Department import Department
from objects.Home.Room import Room
from objects.Subscription.Plan import SubscriptionPlan
from colorama import Fore, Back, Style

room_bathroom = Room('Street, 5a', 'bathroom')
room_livingroom = Room('Street, 5a', 'limingroom')
room_badroom = Room('Street, 5a', 'badroom')

subscription_home1 = SubscriptionPlan('week', room_badroom.address)
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
         }}


room_bathroom_h2 = Room('Street, 1a', 'bathroom')
room_livingroom_h2 = Room('Street, 1a', 'livingroom')
room_bedroom_h2 = Room('Street, 1a', 'bedroom')
subscription_home2 = SubscriptionPlan('year', room_bedroom_h2.address)

home2 = {'address': room_bathroom.address,
         'room_list': [room_bedroom_h2, room_livingroom_h2, room_bathroom_h2],
         'floors': 3,
         'owner': 'Smith Baker',
         'department': home2_department,
         'account': {
             'subscription_plan': subscription_home2,
             'balance': 120
         }}


homes = [home1, home2]

for home in homes:
    if home['account']['balance'] <= 0:
        home_department = home['department']
        print(Fore.RED + 'department',home_department.name)
        print('Home address', home['address'])
        print('Home owner:', home['owner'])
        home_subscription = home['account']['subscription_plan']
        print('Subscription:', home_subscription.subscription_type)
        print('=====================================================')
    else:
        home_department = home['department']
        print(Fore.GREEN + 'department', home_department.name)
        print('Home address', home['address'])
        print('Home owner:', home['owner'])
        home_subscription = home['account']['subscription_plan']
        print('Subscription:', home_subscription.subscription_type)
        print('=====================================================')


