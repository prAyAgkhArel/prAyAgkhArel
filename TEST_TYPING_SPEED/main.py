from tkinter import *
from tkinter import ttk
import random
import time


window = Tk()
window.title("TestYourTypingSpeed")
window.config(padx=30, pady=30)

main_label = Label(window,
                   text = "Here your typing phrase appears!!",
                   wraplength=800,
                   justify="left"
                   )
main_label.pack()

text_entry = Entry(window, width=100)
text_entry.pack()

def get_current_time():
    return time.time()

def select_mode():
    if mode.get() == "word":
        word_numbers.pack()
    else:
        word_numbers.pack_forget()

start_time = None
finished = False
number_of_words = 0

def first_key_pressed(event):
    global start_time

    if start_time is None:
        start_time = time.time()
        print("Timer started:", start_time)



def words_typing(number_of_words):
    global phrase

    selected_words = []

    for _ in range(int(number_of_words)):
        word = random.choice(words)
        selected_words.append(word)

    joined_words = " ".join(selected_words)

    main_label.config(text=joined_words)
    phrase = joined_words



def sentence_typing():
    global phrase
    global number_of_words

    print('sentence typing called')
    sentence = random.choice(texts)
    main_label.config(text=sentence)
    number_of_words = len(sentence.split(' '))
    phrase = sentence

finished = False
def check_typing(event):
    global finished
    if text_entry.get() == phrase and not finished:
        finished = True
        print("Finished!")
        test_speed(len(phrase.split(" ")))



def test_speed(number):
    end_time = get_current_time()
    print(end_time)
    print("no of words", number)
    time_elapsed= end_time - start_time
    print(time_elapsed, " is the time elasped")
    speed = (number*60)/time_elapsed
    print("speed is", speed)
    main_label.config(text=f"Your typing speed is {int(speed)} words/minute.")

# Whenever a key is pressed while the cursor is inside text_entry, call key_pressed().
text_entry.bind("<Key>", first_key_pressed)
text_entry.bind("<KeyRelease>", check_typing)



words = [
    "the", "quick", "brown", "fox", "jumps", "over", "lazy", "dog",
    "computer", "python", "program", "coding", "keyboard", "screen",
    "window", "button", "text", "speed", "typing", "practice",
    "learn", "build", "project", "application", "software", "developer",
    "website", "internet", "system", "data", "information", "technology",
    "language", "function", "variable", "string", "number", "list",
    "object", "class", "method", "value", "input", "output", "user",
    "create", "write", "read", "open", "close", "save", "file",
    "time", "day", "night", "morning", "world", "people", "friend",
    "family", "school", "work", "home", "place", "country", "city",
    "life", "good", "great", "small", "large", "new", "old",
    "first", "last", "next", "back", "start", "stop", "play",
    "test", "result", "correct", "wrong", "answer", "question",
    "easy", "hard", "fast", "slow", "important", "simple", "better",
    "learn", "improve", "focus", "concentration", "challenge", "success",
    "goal", "future", "knowledge", "skill"
]

texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Practice makes perfect when learning to type.",
    "Python is a powerful programming language."
]
punctuations = [",", ":", ".", "?", "-", "(", ")", "\"", "'"]




mode = StringVar(value="word")
Radiobutton(
    window,
    text="Sentence",
    variable=mode,
    value="sentence",
    command=select_mode
).pack()

Radiobutton(
    window,
    text="Word",
    variable=mode,
    value="word",
    command=select_mode
).pack()


word_numbers = ttk.Combobox(
    window,
    values=[10, 20, 30, 50, 100]
)





def start_test():
    global start_time
    global finished

    text_entry.delete(0, END)
    main_label.config(text='')
    start_time = None
    finished = False

    if mode.get() == "sentence":
        sentence_typing()
    else:
        number = word_numbers.get()
        words_typing(number)


start_button = Button(
    window,
    text="Start",
    command=start_test
)
start_button.pack()



window.mainloop()