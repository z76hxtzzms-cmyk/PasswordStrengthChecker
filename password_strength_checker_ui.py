# Password Strength Checker UI
import tkinter as tk
# Import the check_password_strength function from password_strength_checker.py
# THIS IS CRUICAL: We need to import the function so that we can get our password 
# strength score and rating to display in the UI.
import password_strength_checker

def check_password():
    password = user_input.get() # This gets the password from the entry when button is clicked.

    # pass password into our check_strength function in our other file.
    # Then return to variable their respective values so we can use them in the UI.
    score, rating, color, results = password_strength_checker.check_strength(password)

    # Update the rating label
    rating_label.config(text=f"Result: {rating}  ({score}/6)", fg=color)

    #TODO: Fix UI, right now it shows the checks at first before inputting anything. Looks 
    # Kind of ugly.

    # Checklist items mapped to display labels
    checks = {
        "length_8":   "8+ characters",
        "length_12":  "12+ characters (bonus)",
        "has_upper":  "Uppercase letter",
        "has_lower":  "Lowercase letter",
        "has_number": "Number included",
        "has_special": "Special character"
    }

    # Update each checklist label based on results dictionary (AI HELP)
    for key, label_widget in check_labels.items():
        passed = results[key]
        symbol = "✓" if passed else "✗"
        text   = checks[key]
        check_color  = GREEN if passed else RED
        label_widget.config(text=f"  {symbol}  {text}", fg=check_color)

# AI helped with the UI development!
# Defining colors as variables makes them easy to change later
BG_DARK      = "#1a1a2e"   # Main background
BG_CARD      = "#16213e"   # Input and checklist background
ACCENT       = "#0f3460"   # Button background
TEXT_PRIMARY = "#e0e0e0"   # Main text
TEXT_MUTED   = "#888888"   # Subtle text
GREEN        = "#00b894"   # Pass color
RED          = "#e74c3c"   # Fail color

# Window setup down here

window = tk.Tk()
window.title("Password Strength Checker")
window.geometry("380x520")
# This locks the window size to ensure compact UI and consistent layout.
# I do not want to deal with resizing issues, so I will make the window non-resizable.
window.resizable(False, False) 
window.configure(bg=BG_DARK)   # This applies the dark background 


# Title section down here.

# Ew code formatting looks wonky. I will fix this later, but for now, I want to get the UI working first.
title_label = tk.Label(window, text = "Password Strength Checker",
                       bg = BG_DARK,
                       fg = TEXT_PRIMARY,
                       font = ("Helvetica", 18, "bold")
                       )
title_label.pack(pady = (30,4)) # This adds space above and below the title
subtitle_label = tk.Label(window, text = "Analyze your password's security",
                          bg = BG_DARK,
                          fg = TEXT_MUTED,
                          font = ("Helvetica", 10))
subtitle_label.pack(pady = (0,20)) # This adds space below the subtitle

# Input section down here.
input_frame = tk.Frame(window, bg = BG_CARD, padx = 10, pady = 10)
input_frame.pack(padx = 20, fill = "x") # This adds horizontal padding and makes the frame fill the width of the window

input_label = tk.Label(input_frame,
                       text = "Password",
                       bg = BG_CARD,
                       fg = TEXT_MUTED,
                       font = ("Helvetica", 9))

input_label.pack(anchor = "w") # This aligns the label to the left

user_input = tk.Entry(input_frame,
                      show="*",
                      bg = BG_DARK,
                      fg = TEXT_PRIMARY,
                      insertbackground = TEXT_PRIMARY, # This changes the cursor color to match the text color
                      relief = "flat", # This removes the border around the entry widget for a cleaner look
                      font = ("Helvetica", 12))
user_input.pack(fill = "x", pady = (4,0)) # This makes the entry widget fill the width of the frame and adds space below it

check_button = tk.Button(window, 
                         text = "Check Strength", 
                         bg = ACCENT,
                         fg = TEXT_PRIMARY, 
                         font = ("Helvetica", 11, "bold"),
                         relief = "flat", 
                         cursor = "hand2", # This changes the cursor to a hand when hovering over the button
                         command = check_password
                         ) 
check_button.pack(padx = 20, pady = 15, fill = "x")


# Results down here (AI PLAYED A HUGE ROLE IN MAKING THE UI LOOK NICE!)
rating_label = tk.Label(
    window,
    text="Enter a password to begin",
    bg=BG_DARK,
    fg=TEXT_MUTED,
    font=("Helvetica", 12, "bold")
)
rating_label.pack(pady=(0, 10))

# ---- Checklist Section ----
checklist_frame = tk.Frame(window, bg=BG_CARD, padx=15, pady=12)
checklist_frame.pack(padx=20, fill="x")

# These are the checklist items we will update dynamically
check_keys = ["length_8", "length_12", "has_upper", 
              "has_lower", "has_number", "has_special"]

# Dictionary to store label widgets so we can update them later
check_labels = {}

for key in check_keys:
    lbl = tk.Label(
        checklist_frame,
        text=f"  -  {key}",
        bg=BG_CARD,
        fg=TEXT_MUTED,
        font=("Helvetica", 10),
        anchor="w"
    )
    lbl.pack(fill="x", pady=2)
    check_labels[key] = lbl  # Store widget reference in dictionary


window.mainloop()