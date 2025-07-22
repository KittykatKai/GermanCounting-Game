#Add numbers and German names
#Allow user to guess German name for random number
#Return correct/incorrect
#Repeat for all numbers until 0-20 is done
#Print result (how many correct, which ones were correct)
#Also add option for both Swiss and High German
import random

#Swiss German Numbers
import SGN
# High German Numbers
import HGN
#Allows user to choose dialect
def choose_dialect():

    while True:
        choice = input("Choose dialect: (s) Swiss German or (h) High German: ").strip().lower()
        if choice in ('s', 'swiss'):
            return SGN.sgn, 'Swiss German'
        elif choice in ('h', 'high'):
            return HGN.hgn, 'High German'
        else:
            print("Invalid choice. Please enter 's' or 'h'.")


def play_game(numbers_dict):
    all_numbers = list(numbers_dict.keys())
    random_order = random.sample(all_numbers, len(all_numbers))

    correct = []
    incorrect = []
    for num in random_order:
        guess = input(f"What is the German for {num}? ").strip().lower()
        answer = numbers_dict[num].lower()
        if guess == answer:
            print("Correct!\n")
            correct.append(num)
        else:
            print(f"Incorrect. The right answer is '{answer}'.\n")
            incorrect.append((num, guess, answer))
    return len(correct), correct, incorrect


def summary(dialect_name, correct_count, correct_list, incorrect_list):
    total = 21  # numbers 0 through 20 inclusive
    print("\nGame Over")
    print(f"Dialect: {dialect_name}")
    print(f"You got {correct_count} out of {total} correct.")
    if correct_list:
        print("Correct numbers:", ", ".join(str(n) for n in sorted(correct_list)))
    if incorrect_list:
        print("\nIncorrect answers:")
        for num, guess, answer in sorted(incorrect_list, key=lambda x: x[0]):
            print(f"  {num}: you answered '{guess}', correct is '{answer}'")


def main():
    print("Welcome to the German Counting Game (0-20)!")
    numbers_dict, dialect = choose_dialect()
    correct_count, correct_list, incorrect_list = play_game(numbers_dict)
    summary(dialect, correct_count, correct_list, incorrect_list)


if __name__ == "__main__":
    main()

