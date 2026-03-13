import random
import re
import time
import sys

botName = "guy"
userName = ""
messages = 0

greetings = ["hi", "hello", "hey", "greetings", "what's up", "howdy"]
default_responses = ["That's interesting!","Tell me more!","I see...","Cool!","Thanks for sharing!"]
howAreYou = ["how are you", "hows it going", "whats up", "sup", "hows your day"]
askingForName = ["what's your name?", "who are you?", "what should I call you?"]
goodbyes = ["bye", "goodbye", "see you later", "farewell", "take care"]
jokes = ["Why can't you hear a pterodactyl go to the bathroom? Because the 'P' is silent.",
         "what do you call a well-balaced horse? Stable.",
         "What would bears be without bees? Ears.",
         "What do you call a fish without an eye? Fsh.",
         "Why do pirated pirates not know the alphabet? They always get stuck at 'C'."]
riddlesQuestions = ["What has keys but can't open locks?", "What has a heart that doesn't beat?", "What has a neck but no head?", "What is at the end of a rainbow?"]
riddlesAnswers = ["A piano.", "An artichoke.", "A bottle.", "The letter 'W'."]
confusedResponses = ["I'm not sure I understand.", "Can you please rephrase that?", "Sorry, I don't know how to respond to that."]
happyWords = ["happy", "joy", "excited", "glad", "pleased"]
sadWords = ["sad", "unhappy", "depressed", "down", "miserable", "angry"]


def seperator():
    print("=" * 100)

def BotMessage(message):
    prefix = f"🤖 {botName}: "
    sys.stdout.write(prefix)
    sys.stdout.flush()
    for char in str(message):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()

def UserInput():
    global messages
    messages += 1
    return input(f"👤 {userName}: ")

def show_help():
    seperator()
    BotMessage("Here are some things you can ask me:")
    print("tell a joke \n ask a riddle \n play games \n calculate a number(end the equation in '=') \n analyze your mood \n you can say 'help' to see this message again \n you can say 'exit' to end the conversation")

def GreetUser():
    global userName
    greeting = random.choice(greetings)
    BotMessage(f"{greeting} I'm {botName}, your friendly chatbot!")
    print(random.choice(askingForName))
    userName = input("👤 You: ")
    BotMessage(f"Nice to meet you, {userName}! How can I assist you today?")

def TellJoke():
    seperator()
    joke = random.choice(jokes)
    BotMessage(joke)

def AskRiddle():
    seperator()
    index = random.randint(0, len(riddlesQuestions) - 1)
    BotMessage(riddlesQuestions[index])
    print("type anything to see the answer...")
    UserInput()
    BotMessage(riddlesAnswers[index])

def NumberGuessingGame():
    seperator()
    BotMessage("Welcome to the Number Guessing Game! I'm thinking of a number between 1 and 20. Can you guess it? type your guess below or type 'exit' to end the game.")
    number = random.randint(1, 20)
    attempts = 0
    guess = 21
    while guess != number:
        guess = UserInput()
        if guess.lower() == "exit":
            BotMessage("Thanks for playing! Let's play again sometime.")
            return
        try:
            guess = int(guess)
            attempts += 1
        except ValueError:
            BotMessage("Please enter a valid number.")
            continue
        if guess < number:
            BotMessage("Too low! Try again.")
        elif guess > number:
            BotMessage("Too high! Try again.")
    BotMessage(f"Congratulations! You've guessed the number {number} in {attempts} attempts!")
    print("type 'exit' to end the game or anything else to play again...")
    if UserInput().lower() != "exit":
        NumberGuessingGame()

def analyze_mood(user_input):
    for word in happyWords:
        if word in user_input:
            BotMessage("I'm glad to hear that! Keep up the positive vibes!")
            return
    for word in sadWords:
        if word in user_input:
            BotMessage("I'm sorry to hear that. Remember, it's okay to feel down sometimes. If you want to talk about it, I'm here to listen.")
            return
    BotMessage("seems like you're feeling neutral. If you want to share more about how you're feeling, I'm here to listen.")

def strip_punctuation(text):
    punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''
    for char in punctuation:
        text = text.replace(char, "")
    return text.lower()

def calculate(expression):
    # Only allow numbers, operators, spaces, decimals, and parentheses
    if not re.match(r'^[\d\s\+\-\*\/\.\(\)]+$', expression):
        BotMessage("I can only calculate math expressions! (e.g. 5 + 3 =)")
        return
    try:
        result = eval(expression)
        BotMessage(f"The answer is: {result}")
    except ZeroDivisionError:
        BotMessage("You can't divide by zero!")
    except Exception:
        BotMessage("That doesn't look like a valid math expression.")

def GetResponse(userInput):
    strippedInput = strip_punctuation(userInput)
    if any(greeting in strippedInput for greeting in greetings):
        GreetUser()
    elif any(phrase in strippedInput for phrase in howAreYou):
        BotMessage("I'm great! How are you?")
    elif any(phrase in strippedInput for phrase in askingForName):
        BotMessage(f"My name is {botName}.")
    elif "funny" in strippedInput or "joke" in strippedInput:
        TellJoke()
    elif "riddle" in strippedInput:
        AskRiddle()
    elif "game" in strippedInput:
        NumberGuessingGame()
    elif "help" in strippedInput or "options" in strippedInput or "commands" in strippedInput:
        show_help()
    elif "exit" in strippedInput or "quit" in strippedInput or "goodbye" in strippedInput or "bye" in strippedInput:
        BotMessage("Goodbye! It was nice chatting with you.")
        exit()
    elif "=" in userInput:
        calculate(userInput[:-1])
    elif "analyze mood" in strippedInput:
        BotMessage("Sure! Please tell me how you're feeling.")
        mood_input = UserInput()
        analyze_mood(mood_input)
    else:
        BotMessage(random.choice(default_responses))


def chat():
    GreetUser()
    show_help()
    while True:
        userInput = UserInput()
        if userInput.strip() == "":
            continue
        if userInput.lower() == "exit":
            BotMessage(f"{random.choice(goodbyes)} {userName}! It was nice chatting with you.")
            BotMessage(f"we exchanged {messages} messages")
            break
        GetResponse(userInput)


if __name__ == "__main__":
    chat()
