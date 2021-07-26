def to_check_when_you_will_be_100_years():
    age = int(input("Enter your age : "))
    year_of_birth = 2021 - age

    if age <= 0:
        print("You're not yet born. ")
    elif 0 < age < 100:
        print("You will turn 100 years old in year : ")
        print(year_of_birth + 100)
    elif age >= 1900:
        print("You will turn 100 years old in year : ")
        print(age + 100)
    else:
        print("You are not dead ")

def to_check_your_age_at_2090():
    age = int(input("Enter your age : "))
    year_of_birth = 2021 - age

    if age <= 0:
        print("You're not yet born. ")
    elif 0 < age < 150:
        print("You age at 2090 will be : ")
        print(2090 - year_of_birth)
    elif 0 < age < 1950:
        print("You seem to be the oldest person alive. ")
    elif 1950 < age < 2021:
        print(2090 - age)
    else:
        print("You Entered a wrong input. ")

def optional_year():
    age = int(input("Enter your age : "))
    year_of_birth = 2021 - age
    optional_year_you_want_to_enter = int(input("Enter the year to which you want to know your age : "))
    if optional_year_you_want_to_enter <= 0:
        print("You're not yet born. ")
    elif age < 150 and 2021 < optional_year_you_want_to_enter:
        print(optional_year_you_want_to_enter - year_of_birth)
    elif 2021 < optional_year_you_want_to_enter and 1950 < age < optional_year_you_want_to_enter:
        print(optional_year_you_want_to_enter - age )
    elif 1950 > age:
        print("You seem to be the oldest person alive. ")
    else:
        print("You Entered a wrong input. ")

if __name__ == '__main__':
    while True:
        print("What do you want to do ?")
        print("1.  To check when you will be 100 years old : ")
        print("2.  To check your age at 2090 : ")
        print("3.  To check your age at any Optional Year : ")
        user_choice = int(input())
        if user_choice == 1:
            to_check_when_you_will_be_100_years()
            break
        elif user_choice == 2:
            to_check_your_age_at_2090()
            break
        elif user_choice == 3:
            optional_year()
            break
        else:
            print("You entered a wrong input. ")
            break
