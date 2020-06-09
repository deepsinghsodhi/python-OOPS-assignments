'''
======================
1) The Puppy Age Calculator
Write a function named calculateDogAge that:
takes 1 argument: your puppy's age.
calculates your dog's age based on the conversion rate of 1 human year to 7 dog years.
outputs the result to the screen like so: "Your doggie is NN years old in dog years!"

Call the function three times with different sets of values.
Bonus: Add an additional argument to the function that takes the conversion rate of human to dog years.

'''
def calculateDogAge(age_in_human_year, human_to_dog):
    if age_in_human_year < 0:
    	print("Age must be a positive number!")
    else:
        dog_age = age_in_human_year * 7
        human_age = human_to_dog / 7
        
        month = human_age * 12
        year = month // 12
        re_month = month % 12

        print("\nYour doggie is", dog_age, "years old in dog years!")
        print("Human age in dog's year is:", round(year), 'years and', round(re_month), 'months')

calculateDogAge(1, 15)
calculateDogAge(12, 1)
calculateDogAge(5, 65)

