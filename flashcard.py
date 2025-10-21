import random


def add(flash):
    question = input("Enter the question: ")
    answer = input("Enter the answer: ")
    flash.append({"question": question, "answer": answer})
    print("Flashcard added successfully!")


def quiz(flash):
    if not flash:
        print("No flashcards available. Please add some first.")
        return

    score = 0
    random.shuffle(flash)
    for card in flash:
        print("\nQuestion: " + card["question"])
        user = input("Your answer: ")
        if user.lower() == card["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print(f"Opps Try Again! The correct answer was: {card['answer']}")

    print(f"\nYou scored {score} out of {len(flash)}!")


def view(flash):
    if not flash:
        print("No flashcards available.")
    else:
        print("\nYour Flashcards:")
        for index, card in enumerate(flash, 1):
            print(f"{index}. {card['question']} -> {card['answer']}")


def main():
    flash = []
    while True:
        print("\nFlashcard Quiz App")
        print("1. Add a flashcard")
        print("2. Take the quiz")
        print("3. View all flashcards")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add(flash)
        elif choice == "2":
            quiz(flash)
        elif choice == "3":
            view(flash)
        elif choice == "4":
            print("Thank You For Using!")
            break
        else:
            print("Invalid choice, please try again.")


main()
