import random
target_number = random.randint(1, 100)
attempts = 0
while True:
	user_guess = int(input("Guess the secret number: "))
	attempts += 1
	if user_guess == target_number:
		print("Correct!")
		print("Total attempts :", attempts)
	elif user_guess < target_number:
		print("Too small. Try a bigger number")
	else:
		print("Too big. Try a smaller number.")

print("Congratulations !")