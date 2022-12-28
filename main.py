# IMPORTS
# IMPORT TKINTER
import tkinter as tk
# IMPORT REGULAR EXPRESSION
import re


# GLOBAL VARIABLES
# INITIALIZE TKINTER WINDOW
WINDOW = tk.Tk()
# INITIALIZE TIME COUNTER
TIME_COUNTER = 0
# INITIALIZE WORD COUNTER
WORD_COUNTER = 0
# INITIALIZE EMPTY TEXT STRING
TEXT = ""


# WINDOW TITLE
WINDOW.title("Disappearing Text Writing App")
# WINDOW SIZE
WINDOW.minsize(500, 500)


# RESTART FUNCTION
def restart():
    # REFERENCE GLOBAL VARIABLES
    global TIME_COUNTER, WORD_COUNTER
    # RESET TIME COUNTER
    TIME_COUNTER = 0
    # RESET WORD COUNTER
    WORD_COUNTER = 0
    # DELETE DATA IN TEXTBOX
    textbox.delete(1.0, tk.END)
    # INSERT EMPTY STRING INTO TEXTBOX
    textbox.insert(tk.END, "")
    # UPDATE WORD COUNTER LABEL
    word_counter_label.config(text=f"Words: {WORD_COUNTER}")
    # UPDATE TIME COUNTER LABEL
    time_counter_label.config(text=f"Time Left: {10 - TIME_COUNTER}")


# WORD COUNTER FUNCTION
def word_counter():
    # REFERENCE GLOBAL VARIABLE
    global WORD_COUNTER
    # OBTAIN USER TYPED WORDS
    words = textbox.get('1.0', 'end-1c')
    # COUNT WORDS
    WORD_COUNTER = len(re.findall('\w+', words))
    # UPDATE WORD COUNT LABEL
    word_counter_label.config(text=f'Words: {WORD_COUNTER}')


# CHECK FUNCTION
def check():
    # REFERENCE GLOBAL VARIABLES
    global TIME_COUNTER, WORD_COUNTER, TEXT, WINDOW
    # IF USER HAS NOT TYPED
    if TEXT == textbox.get(1.0, tk.END):
        # IF COUNTER HAS REACHED 10 SECONDS
        if TIME_COUNTER == 10:
            # CALL RESTART METHOD AFTER 1 SECOND
            WINDOW.after(1000, restart)
            # CALL CHECK METHOD AFTER 1 SECOND
            WINDOW.after(1000, check)
        # IF COUNTER IS NOT AT 10 SECONDS
        else:
            # INCREMENT COUNTER BY 1
            TIME_COUNTER += 1
            # UPDATE TIME COUNTER LABEL
            time_counter_label.config(text=f"Time Left: {10 - TIME_COUNTER}")
            # CALL CHECK METHOD AFTER 1 SECOND
            WINDOW.after(1000, check)
    # IF USER HAS TYPED
    else:
        # UPDATE TEXT STRING
        TEXT = textbox.get(1.0, tk.END)
        # CALL WORD COUNTER METHOD AFTER 1 SECONDS
        WINDOW.after(1000, word_counter)
        # RESET TIME COUNTER
        TIME_COUNTER = 0
        # UPDATE TIME COUNTER LABEL
        time_counter_label.config(text=f"Time Left: {10 - TIME_COUNTER}")
        # RECALL CHECK METHOD AFTER 1 SECOND
        WINDOW.after(1000, check)


# CREATE TITLE LABEL
title_label = tk.Label(WINDOW, text="Welcome to the Disappearing Text Writing App", font=('Consolas', 20))
# PACK TITLE LABEL
title_label.pack(padx=10, pady=10)

# CREATE TIME COUNTER LABEL
time_counter_label = tk.Label(WINDOW, text=f"Time Left: {10 - TIME_COUNTER}", font=('Consolas', 12))
# PACK TIME COUNTER LABEL
time_counter_label.pack(pady=10)

# CREATE TEXTBOX
textbox = tk.Text(height=20, width=50)
# ACTIVATE TEXTBOX FOR INPUT
textbox.focus()
# PACK TEXTBOX
textbox.pack(pady=10)

# CREATE WORD COUNTER LABEL
word_counter_label = tk.Label(WINDOW, text=f"Words: {WORD_COUNTER}", font=('Consolas', 12))
# PACK WORD COUNTER LABEL
word_counter_label.pack(pady=10)

# CREATE RESTART BUTTON
restart_button = tk.Button(WINDOW, text="Restart", font=('Consolas', 12), command=restart)
# PACK RESTART BUTTON
restart_button.pack(pady=10)

# AFTER 1 SECOND, CALL CHECK METHOD
WINDOW.after(1000, check)
# RUN WINDOW
WINDOW.mainloop()
