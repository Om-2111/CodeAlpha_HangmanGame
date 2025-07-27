import random

# List of words with categories and hints
word_data = [
    {"word": "apple", "category": "Fruit", "hint": "Keeps the doctor away "},
    {"word": "banana", "category": "Fruit", "hint": "Long and yellow "},
    {"word": "cherry", "category": "Fruit", "hint": "Small red fruit often on cakes "},
    {"word": "grape", "category": "Fruit", "hint": "Used to make wine "},
    {"word": "mango", "category": "Fruit", "hint": "King of fruits in India "},
    {"word": "orange", "category": "Fruit", "hint": "A citrus fruit rich in Vitamin C "},
    {"word": "pineapple", "category": "Fruit", "hint": "Tropical fruit with a spiky outside "}
]

# Select a random word
selected_data = random.choice(word_data)
selected_word = selected_data["word"]
category = selected_data["category"]
hint = selected_data["hint"]

max_attempts = 5
attempts = 0

print("🎮 Welcome to the Word Guessing Game!")
print("📂 Category:", category)
print("💡 Hint:", hint)
print("🧠 You have", max_attempts, "attempts to guess the correct word.\n")

# Main game loop
while attempts < max_attempts:
    guess = input(f"Enter your guess ({max_attempts - attempts} attempts left): ").lower()

    if guess == selected_word:
        print("🎉 Congratulations! You guessed the word correctly:", selected_word)
        break
    else:
        attempts += 1
        print("❌ Incorrect guess!")

if attempts == max_attempts:
    print("\n😢 You ran out of attempts! The correct word was:", selected_word)

print("🙏 Thanks for playing!")
