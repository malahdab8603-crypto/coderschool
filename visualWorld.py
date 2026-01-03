import tkinter as tk
from tkinter import messagebox
import random

# ---------- DATA ----------
world = {
    1:{"up": 2, "down": 16, "right": 4},
    2:{"up": 3, "down": 1, "right": 15, "left":5},
    3:{"down": 2, "left":4},
    4:{"down": 6, "right": 3},
    5:{"down": 7, "right": 2},
    6:{"up": 4, "right": 7},
    7:{"up": 5, "down": 8, "right": 16, "left":6},
    8:{"up": 7, "right": 9},
    9:{"down": 11, "right": 10, "left":8},
    10:{"up": 14, "left":9},
    11:{"up": 9, "right": 12},
    12:{"up": 13, "left":11},
    13:{"down": 12,"left":14},
    14:{"up": 15, "down": 10, "right": 13, "left":1},
    15:{"down": 14, "left":2},
    16:{"up": 1, "left":7},
}

locationNames = {
    6: "Entrance",
    4: "Exit",
    3: "Checkout",
    12: "Produce",
    11: "Dairy",
    10: "Essentials",
    8: "Clothing",
    7: "Pharmacy",
    15: "Help Desk",
    2: "Returns",
    5: "Restaurant",
    13: "Bathroom"
}

storeItems = {
    # Produce
    12: {
        "Apple": 2,
        "Banana": 1,
        "Orange": 2,
        "Lettuce": 3,
        "Tomato": 2,
        "Potato": 1,
        "Grapes": 4
    },

    # Dairy
    11: {
        "Milk": 4,
        "Cheese": 5,
        "Yogurt": 3,
        "Butter": 4,
        "Eggs": 5,
        "Cream": 3
    },

    # Essentials
    10: {
        "Soap": 3,
        "Toothpaste": 4,
        "Shampoo": 6,
        "Conditioner": 6,
        "Toilet Paper": 8,
        "Paper Towels": 7,
        "Laundry Detergent": 10
    },

    # Clothing
    8: {
        "Shirt": 10,
        "Pants": 20,
        "Jacket": 35,
        "Socks": 5,
        "Shoes": 40,
        "Hat": 8
    },

    # Pharmacy
    7: {
        "Medicine": 8,
        "Bandages": 4,
        "Pain Reliever": 6,
        "Vitamins": 10,
        "Cough Syrup": 7,
        "Hand Sanitizer": 3
    },

    # Restaurant / Food Court
    5: {
        "Burger": 6,
        "Fries": 3,
        "Soda": 2,
        "Pizza Slice": 4,
        "Hot Dog": 4,
        "Ice Cream": 3
    }
}

# ---------- NPC DATA ----------
npcs = {
    12: {  # Produce
        "name": "Farmer Joe",
        "personality": "cheerful",
        "face": "😊",
        "dialogues": [
            "Fresh produce today! Everything's organic!",
            "These tomatoes are the best in town!",
            "Want to know a secret? The grapes are my favorite!",
            "Nothing beats farm-fresh vegetables!",
            "I grew these with my own two hands!"
        ]
    },
    11: {  # Dairy
        "name": "Mildred",
        "personality": "grumpy",
        "face": "😤",
        "dialogues": [
            "What do you want? Make it quick!",
            "The milk's in the damn cooler, can't you see?",
            "Don't just stand there staring!",
            "I've been here since 6 AM, so excuse me if I'm not chipper!",
            "Buy something or move along, for crying out loud!"
        ]
    },
    10: {  # Essentials
        "name": "Karen",
        "personality": "demanding",
        "face": "😠",
        "dialogues": [
            "Where's your manager? These prices are ridiculous!",
            "In MY day, soap didn't cost this much!",
            "I need to speak to someone in charge RIGHT NOW!",
            "This is absolutely unacceptable!",
            "You better give me a discount or I'm writing a review!"
        ]
    },
    8: {  # Clothing
        "name": "Fashionista Fran",
        "personality": "sassy",
        "face": "💅",
        "dialogues": [
            "Honey, those shoes are SO last season!",
            "You need a complete wardrobe makeover, darling!",
            "I can tell you have potential... buried deep down.",
            "Let me guess, you dress in the dark?",
            "Fashion isn't for everyone, but you could try!"
        ]
    },
    7: {  # Pharmacy
        "name": "Dr. Phil",
        "personality": "helpful",
        "face": "🩺",
        "dialogues": [
            "Take two aspirin and call me in the morning!",
            "Make sure to read the dosage instructions carefully.",
            "Health is wealth, my friend!",
            "Don't forget to stay hydrated!",
            "Prevention is better than cure!"
        ]
    },
    5: {  # Restaurant
        "name": "Chef Tony",
        "personality": "angry",
        "face": "👨‍🍳",
        "dialogues": [
            "What the hell took you so long? Food's getting cold!",
            "You want fries with that or are you gonna waste my time?",
            "I'm running a damn restaurant here, not a charity!",
            "Order something or get out of my kitchen!",
            "I didn't bust my ass cooking for you to just stand there!"
        ]
    },
    2: {  # Returns
        "name": "Bored Betty",
        "personality": "bored",
        "face": "😑",
        "dialogues": [
            "*sigh* Another return? Great...",
            "Do you have your receipt or are we doing this the hard way?",
            "I've processed like 50 returns today...",
            "Yeah, sure, whatever. Just put it on the counter.",
            "This job is slowly killing my soul..."
        ]
    },
    3: {  # Checkout
        "name": "Cashier Mike",
        "personality": "friendly",
        "face": "😄",
        "dialogues": [
            "Hello! Find everything okay today?",
            "Having a great day? Me too!",
            "Thanks for shopping with us!",
            "Would you like a bag with that?",
            "Have a wonderful rest of your day!"
        ]
    },
    15: {  # Help Desk
        "name": "Helper Hannah",
        "personality": "helpful",
        "face": "🤓",
        "dialogues": [
            "Lost? I can help you find anything!",
            "Just let me know what you're looking for!",
            "I know this store like the back of my hand!",
            "Need directions? That's what I'm here for!",
            "Don't be shy, ask me anything!"
        ]
    },
    6: {  # Entrance
        "name": "Greeter Gary",
        "personality": "cheerful",
        "face": "👋",
        "dialogues": [
            "Welcome to the store! Glad you're here!",
            "Have a fantastic shopping experience!",
            "Don't forget to check out our sales!",
            "It's a beautiful day for shopping!",
            "Welcome, welcome! Come on in!"
        ]
    },
    13: {  # Bathroom
        "name": "Janitor Jim",
        "personality": "grumpy",
        "face": "🧹",
        "dialogues": [
            "I just mopped that floor, damn it!",
            "Can people not make a mess for FIVE MINUTES?",
            "This bathroom was spotless an hour ago...",
            "You better not track dirt everywhere!",
            "Why do I even bother cleaning?"
        ]
    },
    # Hallway NPCs - Homeless people
    1: {
        "name": "Old Tom",
        "personality": "sad",
        "face": "🧓",
        "dialogues": [
            "Spare some change? I haven't eaten today...",
            "Times are tough, friend. Real tough.",
            "I used to work here, believe it or not.",
            "Just trying to get by, one day at a time.",
            "God bless you, kind soul."
        ]
    },
    9: {
        "name": "Rita",
        "personality": "hopeful",
        "face": "👵",
        "dialogues": [
            "Every little bit helps. Thank you for noticing me.",
            "I'm saving up to get back on my feet.",
            "My kids don't even know I'm here...",
            "Tomorrow will be better, I just know it.",
            "You're one of the few who stops to talk."
        ]
    },
    14: {
        "name": "Veteran Mike",
        "personality": "proud",
        "face": "🪖",
        "dialogues": [
            "Served my country, but fell on hard times.",
            "I don't want pity, just a fair chance.",
            "Not all heroes get happy endings, kid.",
            "Lost my job, then my home. Story as old as time.",
            "Still got my dignity, even if I lost everything else."
        ]
    },
    16: {
        "name": "Young Sam",
        "personality": "desperate",
        "face": "🧑",
        "dialogues": [
            "I'm trying to find work, I swear!",
            "Got kicked out... nowhere else to go.",
            "Please, I'm really hungry...",
            "Life hit me hard. Real damn hard.",
            "I didn't think I'd end up like this..."
        ]
    }
}

playerLocation = 6
money = 100
cart = []
checkedOut = False
npc_interactions = {}

# ---------- THEME ----------
BG = "#1e1e2e"
PANEL = "#313244"
ACCENT = "#89b4fa"
TEXT = "#cdd6f4"
SUCCESS = "#a6e3a1"
DANGER = "#f38ba8"

# ---------- GUI ----------
root = tk.Tk()
root.title("🛍️ Store Adventure")
root.geometry("1050x600")
root.configure(bg=BG)

# ---------- TOP BAR ----------
top = tk.Frame(root, bg=PANEL, pady=10)
top.pack(fill="x")

location_label = tk.Label(top, font=("Arial", 18, "bold"), bg=PANEL, fg=ACCENT)
location_label.pack(side="left", padx=20)

money_label = tk.Label(top, font=("Arial", 14), bg=PANEL, fg=SUCCESS)
money_label.pack(side="right", padx=20)

# ---------- MAIN ----------
main = tk.Frame(root, bg=BG)
main.pack(expand=True, fill="both", padx=10, pady=10)

# ---------- ITEMS ----------
items_frame = tk.LabelFrame(main, text="Items", bg=PANEL, fg=TEXT)
items_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

items_list = tk.Listbox(items_frame, bg=BG, fg=TEXT)
items_list.pack(fill="both", expand=True, padx=10, pady=10)

add_button = tk.Button(items_frame, text="Add to Cart", bg=ACCENT, fg="black")
add_button.pack(pady=10)

# ---------- MOVEMENT ----------
movement_frame = tk.LabelFrame(main, text="Move", bg=PANEL, fg=TEXT)
movement_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# ---------- CART ----------
cart_frame = tk.LabelFrame(main, text="Cart", bg=PANEL, fg=TEXT)
cart_frame.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

cart_list = tk.Listbox(cart_frame, bg=BG, fg=TEXT)
cart_list.pack(fill="both", expand=True, padx=10, pady=10)

return_button = tk.Button(cart_frame, text="Return Item", bg=DANGER, fg="black")
return_button.pack(pady=10)

# ---------- MINI MAP ----------
map_frame = tk.LabelFrame(main, text="Mini Map", bg=PANEL, fg=TEXT)
map_frame.grid(row=0, column=3, sticky="nsew", padx=10, pady=10)

map_cells = {}

# ---------- GRID ----------
main.columnconfigure((0,1,2,3), weight=1)
main.rowconfigure(0, weight=1)

# ---------- HELPERS ----------
def get_item_price(item):
    for store in storeItems.values():
        if item in store:
            return store[item]
    return 0

# ---------- NPC INTERACTION ----------
def show_npc_dialogue():
    if playerLocation not in npcs:
        return
    
    npc = npcs[playerLocation]
    dialogue = random.choice(npc["dialogues"])
    
    # Create popup window
    npc_window = tk.Toplevel(root)
    npc_window.title(f"💬 {npc['name']}")
    npc_window.geometry("400x250")
    npc_window.configure(bg=PANEL)
    npc_window.transient(root)
    npc_window.grab_set()
    
    # Center the window
    npc_window.update_idletasks()
    x = root.winfo_x() + (root.winfo_width() // 2) - (npc_window.winfo_width() // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (npc_window.winfo_height() // 2)
    npc_window.geometry(f"+{x}+{y}")
    
    # NPC Face
    face_label = tk.Label(
        npc_window, 
        text=npc["face"], 
        font=("Arial", 72),
        bg=PANEL,
        fg=TEXT
    )
    face_label.pack(pady=20)
    
    # NPC Name
    name_label = tk.Label(
        npc_window,
        text=npc["name"],
        font=("Arial", 16, "bold"),
        bg=PANEL,
        fg=ACCENT
    )
    name_label.pack()
    
    # Dialogue
    dialogue_label = tk.Label(
        npc_window,
        text=dialogue,
        font=("Arial", 12),
        bg=PANEL,
        fg=TEXT,
        wraplength=350,
        justify="center"
    )
    dialogue_label.pack(pady=10)
    
    # Close button
    close_btn = tk.Button(
        npc_window,
        text="Okay",
        bg=ACCENT,
        fg="black",
        font=("Arial", 12),
        command=npc_window.destroy,
        width=15
    )
    close_btn.pack(pady=15)

# ---------- MINI MAP ----------
def draw_minimap():
    for widget in map_frame.winfo_children():
        widget.destroy()

    for loc in range(1, 17):
        row = (loc - 1) // 4
        col = (loc - 1) % 4

        color = "#585b70"
        if loc == playerLocation:
            color = "#a6e3a1"
        elif loc == 4:
            color = "#f38ba8"
        elif loc == 3:
            color = "#f9e2af"
        elif loc == 15:
            color = "#89b4fa"
        elif loc == 2:
            color = "#cba6f7"

        tk.Label(
            map_frame,
            text=str(loc),
            bg=color,
            fg="black",
            width=6,
            height=3,
            relief="ridge"
        ).grid(row=row, column=col, padx=2, pady=2)

# ---------- FUNCTIONS ----------
def update_screen():
    location_label.config(text=f"📍 {locationNames.get(playerLocation, 'Hallway')}")
    money_label.config(text=f"💰 ${money}")

    items_list.delete(0, tk.END)
    if playerLocation in storeItems:
        for item, price in storeItems[playerLocation].items():
            items_list.insert(tk.END, f"{item} - ${price}")

    cart_list.delete(0, tk.END)
    for item in cart:
        cart_list.insert(tk.END, item)

    for w in movement_frame.winfo_children():
        w.destroy()

    # Add NPC button if there's an NPC at this location
    if playerLocation in npcs:
        npc_btn = tk.Button(
            movement_frame,
            text=f"💬 Talk to {npcs[playerLocation]['name']}",
            bg=SUCCESS,
            fg="black",
            command=show_npc_dialogue
        )
        npc_btn.pack(fill="x", pady=5, padx=10)

    for direction, dest in world[playerLocation].items():
        tk.Button(
            movement_frame,
            text=f"{direction.upper()} → {locationNames.get(dest,'Hallway')}",
            bg=ACCENT,
            fg="black",
            command=lambda d=direction: move(d)
        ).pack(fill="x", pady=5, padx=10)

    add_button.config(state="normal" if playerLocation in storeItems else "disabled")
    draw_minimap()

    if playerLocation == 15:
        open_helpdesk()

def add_to_cart():
    if not items_list.curselection():
        return
    item = items_list.get(items_list.curselection()[0]).split(" - ")[0]
    cart.append(item)
    update_screen()

def checkout():
    global money, checkedOut
    total = sum(get_item_price(item) for item in cart)
    money -= total
    checkedOut = True
    messagebox.showinfo("Checkout", f"Paid ${total}")
    update_screen()

def return_item():
    global money
    if playerLocation != 2 or not checkedOut or not cart_list.curselection():
        return
    item = cart.pop(cart_list.curselection()[0])
    money += get_item_price(item)
    update_screen()

def open_helpdesk():
    helpdesk = tk.Toplevel(root)
    helpdesk.title("Help Desk")
    helpdesk.geometry("300x400")
    helpdesk.configure(bg=BG)

    listbox = tk.Listbox(helpdesk, bg=PANEL, fg=TEXT)
    listbox.pack(fill="both", expand=True, padx=10, pady=10)

    for loc, name in locationNames.items():
        listbox.insert(tk.END, f"{loc} - {name}")

    def teleport():
        global playerLocation
        if not listbox.curselection():
            return
        playerLocation = int(listbox.get(listbox.curselection()[0]).split(" - ")[0])
        helpdesk.destroy()
        update_screen()

    tk.Button(helpdesk, text="Teleport", bg=ACCENT, command=teleport).pack(pady=10)

def move(direction):
    global playerLocation
    playerLocation = world[playerLocation][direction]
    if playerLocation == 3 and not checkedOut:
        checkout()
    if playerLocation == 4 and checkedOut:
        root.destroy()
    update_screen()

# ---------- BUTTONS ----------
add_button.config(command=add_to_cart)
return_button.config(command=return_item)

# ---------- START ----------
update_screen()
root.mainloop()