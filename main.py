from objects.Home.Room import Room
from objects.Subscription.Plan import SubscriptionPlan
from colorama import Fore, Back, Style

room_bathroom = Room('Street, 5a', 'bathroom')
room_livingroom = Room('Street, 5a', 'limingroom')
room_badroom = Room('Street, 5a', 'badroom')

subscription_home1 = SubscriptionPlan('week', room_badroom.address)
home1 = {'address': room_bathroom.address,
         'room_list': [room_badroom, room_livingroom, room_bathroom],
         'floors': 2,
         'owner': 'Joe Brawn',
         'account': {
             'subscription_plan': subscription_home1,
             'balance': 0
         }}


room_bathroom_h2 = Room('Street, 1a', 'bathroom')
room_livingroom_h2 = Room('Street, 1a', 'limingroom')
room_badroom_h2 = Room('Street, 1a', 'badroom')
subscription_home2 = SubscriptionPlan('year', room_badroom_h2.address)

home2 = {'address': room_bathroom.address,
         'room_list': [room_badroom_h2, room_livingroom_h2, room_bathroom_h2],
         'floors': 3,
         'owner': 'Smith Baker',
         'account': {
             'subscription_plan': subscription_home2,
             'balance': 120
         }}


homes = [home1, home2]

for home in homes:
    if home['account']['balance'] <= 0:
        print(Fore.RED + 'Home address', home['address'])
        print('Home owner:', home['owner'])
        home_subscription = home['account']['subscription_plan']
        print('Subscription:', home_subscription.subscription_type)
        print('=====================================================')
    else:
        print(Fore.GREEN + 'Home address', home['address'])
        print('Home owner:', home['owner'])
        home_subscription = home['account']['subscription_plan']
        print('Subscription:', home_subscription.subscription_type)
        print('=====================================================')


