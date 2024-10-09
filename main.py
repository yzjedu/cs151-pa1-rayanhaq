# Start the game
print("Welcome to the haunted mansions, I will be guiding you throughout this adventure.")
name = input("What is your name? ")
print(f"Hello {name}, how old are you?")

# Get user's age
age = int(input("Enter your age: "))

# Check age eligibility
if 20 <= age <= 40:
    response = input("You are eligible to go in the haunted mansion. But only the brave succeed. Do you want to go in? (yes/no): ")

    if response.lower() == "yes":
        door_choice = int( input("There are three doors to go in but you can only choose one. Choose one: Door one, Door two, Door three (1, 2, or 3): "))

        # Door 1 scenario
        if door_choice == 1:
            jump = input("You have reached a bridge. Only the brave can jump. Will you jump? (yes/no): ")
            if jump.lower() == "yes":
                print(
                    "Congratulations! There is gold at the end of the trail, but you must answer these three questions correctly.")
                q1 = int(input("What is 5 * 5? "))
                q2 = int(input("What is 6 * 6? "))
                q3 = int(input("What is 7 * 7? "))

                if q1 == 25 and q2 == 36 and q3 == 49:
                    print("You have earned 100 gold!")
                else:
                    print("Wrong answers! You are sent back to the beginning.")
            else:
                print("You can go back to the intro.")

        # Door 2 scenario
        elif door_choice == 2:
            print("You have reached a dead end.")

        # Door 3 scenario
        elif door_choice == 3:
            climb = input("You have reached a diamond mountain. Do you wish to climb it? (yes/no): ")
            if climb.lower() == "yes":
                print("Congratulations on making it to the top of the mountain! Look at the amazing view.")
            else:
                print("You can go to the exit screen.")

    # User says no to entering the mansion
    else:
        scared = input("Are you scared to go in? (yes/no): ")
        if scared.lower() == "yes":
            print("You can leave.")
        else:
            # User chooses to continue despite being scared
            door_choice = int(
                input("There are three doors to go in. Choose one: Door one, Door two, Door three (1, 2, or 3): "))
            # Repeat the same door conditions as above
            if door_choice == 1:
                jump = input("You have reached a bridge. Only the brave can jump. Will you jump? (yes/no): ")
                if jump.lower() == "yes":
                    print(
                        "Congratulations! There is gold at the end of the trail, but you must answer these three questions correctly.")
                    q1 = int(input("What is 5 * 5? "))
                    q2 = int(input("What is 6 * 6? "))
                    q3 = int(input("What is 7 * 7? "))

                    if q1 == 25 and q2 == 36 and q3 == 49:
                        print("You have earned 100 gold!")
                    else:
                        print("Wrong answers! You are sent back to the beginning.")
                else:
                    print("You can go back to the intro.")
            elif door_choice == 2:
                print("You have reached a dead end.")
            elif door_choice == 3:
                climb = input("You have reached a diamond mountain. Do you wish to climb it? (yes/no): ")
                if climb.lower() == "yes":
                    print("Congratulations on making it to the top of the mountain! Look at the amazing view.")
                else:
                    print("You can go to the exit screen.")

else:
    print("You are not eligible to enter the haunted mansion.")

# Call the function to run the game