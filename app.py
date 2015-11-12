__author__ = 'Zach'


def age_in_seconds():
    your_age = input("Enter your age:")
    age_seconds = int(your_age) *365 *24 *60 *60
    print("Your age in seconds is {}".format(age_seconds))

age_in_seconds()
