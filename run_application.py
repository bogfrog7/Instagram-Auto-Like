from instapy import InstaPy
from instapy import smart_run
import os

username = input("Enter your username: ")
password = input("Enter your password: ")

print("Please choose the following choices\n"
      "\n"
      "1.Follow user's followers\n"
      "2.Grab user's followers\n"
      "3.Grab user's following\n"
      "4.Follow user's likers\n"
      "5.Follow user's commenters\n"
      "\n")

choice = input("Pick a option of your choice: ")

if int(choice) == 5:
        target = input("Please enter the target's username: ")
        amount = input("Please enter the amount of users to like: ")

        if int(amount) > 0:
                session = InstaPy(username=username, password=password)

                session.follow_commenters(usernames=[target],amount=int(amount))

elif int(choice) == 4:
        target = input("Please enter the username of the target account: ")
        amount = input("Please enter the amount of photos to grab: ")
        user_amount = input("Please enter the amount of users to follow: ")

        if int(amount) > 3 and int(user_amount) > 3:
                session = InstaPy(username=username, password=password)


                with smart_run(session):
                        session.follow_likers(usernames=[target],photos_grab_amount=int(amount),follow_likers_per_photo=int(user_amount))


elif int(choice) == 3:
        target = input("Please enter the username of the target account: ")
        amount = input("Please enter the amount of followers to grab: ")


        if int(amount) > 0:
                session = InstaPy(username=username, password=password)
                with smart_run(session):
                        session.grab_following(username=target, amount=int(amount))
                        


elif int(choice) == 2:
        target = input("Please enter the username of the target account: ")
        amount = input("Please enter the amount of followers to grab: ")

        if int(amount) > 0:
                session = InstaPy(username=username, password=password)
                with smart_run(session):
                        session.grab_followers(username=target, amount=int(amount))
        else:
                print("You must pick a amount bigger than 0")


elif int(choice) == 1:
        target = input("Please enter the username of the target account: ")
        amount = input("Please enter the amount of users to follow: ")

        if int(amount) > 0:
                session = InstaPy(username=username, password=password)
                with smart_run(session):
                        session.follow_user_followers(usernames=[target],amount=int(amount))


        else:
                print("You must pick a amount bigger than 0")

