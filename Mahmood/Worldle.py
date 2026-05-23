import os
import tkinter as tk
from tkinter import messagebox
import random
from collections import Counter

# =====================================
# ULTRA WORDLE — MEGA ADVANCED EDITION
# =====================================

WORD_LENGTH = 5
MAX_ATTEMPTS = 6

def load_words():
    """
    Load 5-letter English words from a local words.txt file first.
    Then try wordfreq, NLTK, or the system dictionary before falling
    back to a small built-in list.
    """
    words = set()
    base_path = os.path.dirname(__file__)
    local_path = os.path.join(base_path, "words.txt")

    if os.path.exists(local_path):
        try:
            with open(local_path, "r", encoding="utf-8") as f:
                for line in f:
                    word = line.strip().lower()
                    if len(word) == 5 and word.isalpha():
                        words.add(word)
            if len(words) >= 1000:
                return sorted(words)
        except Exception:
            pass

    # Try wordfreq package next
    try:
        from wordfreq import top_n_list

        word_list = top_n_list("en", 20000)
        for word in word_list:
            word = word.lower().strip()
            if len(word) == 5 and word.isalpha():
                words.add(word)

        if len(words) >= 1000:
            return sorted(words)
    except Exception:
        pass

    # Try NLTK corpus next
    try:
        import nltk
        from nltk.corpus import words as nltk_words

        try:
            word_list = nltk_words.words()
        except LookupError:
            nltk.download("words")
            word_list = nltk_words.words()

        for word in word_list:
            word = word.lower().strip()
            if len(word) == 5 and word.isalpha():
                words.add(word)

        if len(words) >= 1000:
            return sorted(words)
    except Exception:
        pass

    # Try system dictionary second
    possible_paths = [
        "/usr/share/dict/words",
        "/usr/dict/words"
    ]

    for path in possible_paths:
        try:
            with open(path, "r", encoding="utf-8") as f:
                for line in f:
                    word = line.strip().lower()
                    if len(word) == 5 and word.isalpha():
                        words.add(word)

            if len(words) >= 1000:
                return sorted(words)
        except Exception:
            pass

    # Final fallback list
    if words:
        return sorted(words)

    return [
        "apple", "grape", "stone", "chair", "house",
        "water", "light", "track", "plant", "bread"
    ]


WORDS = load_words()

COLORS = {
    "bg": "#0f0f23",  # Dark blue background
    "tile": "#1b1b30",  # Darker tile
    "text": "#ffffff",  # White text
    "green": "#00ff88",  # Bright green
    "yellow": "#ffaa00",  # Orange yellow
    "gray": "#44475a",  # Gray
    "accent": "#bd93f9",  # Purple accent
    "button_bg": "#6272a4",  # Button background
    "button_fg": "#ffffff",  # Button text
    "highlight": "#50fa7b"  # Highlight color
}


def get_feedback(guess, target):
    feedback = ["gray"] * WORD_LENGTH
    target_chars = list(target)

    for i in range(WORD_LENGTH):
        if guess[i] == target[i]:
            feedback[i] = "green"
            target_chars[i] = None

    for i in range(WORD_LENGTH):
        if feedback[i] == "gray" and guess[i] in target_chars:
            feedback[i] = "yellow"
            target_chars[target_chars.index(guess[i])] = None

    return feedback


class SmartBot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.possible = WORDS.copy()

    def score(self, word):
        freq = Counter("".join(self.possible))
        return sum(freq[c] for c in set(word))

    def guess(self):
        if not self.possible:
            return random.choice(WORDS)
        return max(self.possible, key=self.score)

    def update(self, guess, feedback):
        self.possible = [w for w in self.possible if get_feedback(guess, w) == feedback]


class MegaWordle:
    def __init__(self, root):
        self.root = root
        self.root.title("ULTRA WORDLE — Competitive 2 Player")
        self.root.geometry("1000x1200")
        self.root.configure(bg=COLORS["bg"])

        self.mode_var = tk.StringVar(value="Normal")
        self.bots = [SmartBot(), SmartBot()]
        self.active_player = 0
        self.players = [self.create_player_state(), self.create_player_state()]
        self.match_active = False
        self.keyboard_buttons = [{}, {}]
        self.hard_word_pool = self.build_hard_word_list()

        self.setup_game()
        self.build_ui()
        self.match_active = False

        self.root.bind("<Key>", self.handle_key)
        self.select_player(0)
        self.restart_game()

    def build_hard_word_list(self):
        try:
            from wordfreq import zipf_frequency
            sorted_words = sorted(WORDS, key=lambda w: zipf_frequency(w, "en"))
            return sorted_words[:min(2000, len(sorted_words))]
        except Exception:
            return WORDS.copy()

    def create_player_state(self):
        return {
            "target": "",
            "row": 0,
            "col": 0,
            "current": [""] * WORD_LENGTH,
            "game_over": False,
            "solved": False,
            "guesses": 0,
            "score": 0,
            "wins": 0,
            "streak": 0,
            "grid": [],
            "frame": None,
            "status": None,
            "stats": None,
            "header_label": None,
            "keyboard": {},
            "hint_button": None,
        }

    def get_word_pool(self):
        if self.mode_var.get() == "Mega Hard":
            return self.hard_word_pool
        return WORDS

    def setup_game(self):
        pool = self.get_word_pool()
        targets = random.sample(pool, 2)
        for pid, player in enumerate(self.players):
            player["target"] = targets[pid]
            player["row"] = 0
            player["col"] = 0
            player["current"] = [""] * WORD_LENGTH
            player["game_over"] = False
            player["solved"] = False
            player["guesses"] = 0
        for bot in self.bots:
            bot.reset()
        self.match_active = True

    def build_ui(self):
        self.title = tk.Label(
            self.root,
            text="🔥 ULTRA WORDLE — Competitive 2 Player 🔥",
            font=("Arial", 20, "bold"),
            fg=COLORS["text"],
            bg=COLORS["bg"]
        )
        self.title.pack(pady=15)

        self.current_turn_label = tk.Label(
            self.root,
            text="Current turn: Player 1",
            font=("Arial", 12),
            fg=COLORS["text"],
            bg=COLORS["bg"]
        )
        self.current_turn_label.pack(pady=(0, 10))

        self.stats = tk.Label(
            self.root,
            text=f"Words loaded: {len(WORDS)} | Mode: Normal",
            font=("Arial", 12),
            fg=COLORS["text"],
            bg=COLORS["bg"]
        )
        self.stats.pack(pady=(0, 10))

        restart_btn = tk.Button(
            self.root,
            text="🔄 New Game",
            command=self.restart_game,
            bg=COLORS["button_bg"],
            fg=COLORS["button_fg"],
            font=("Arial", 12, "bold")
        )
        restart_btn.pack(pady=(0, 10))

        for pid in range(2):
            self.build_player_board(pid)
            if pid == 0:
                separator = tk.Frame(self.root, bg=COLORS["accent"], height=3)
                separator.pack(fill="x", pady=8)

    def build_player_board(self, pid):
        player = self.players[pid]
        frame = tk.Frame(self.root, bg=COLORS["bg"], bd=2, relief="ridge", highlightthickness=3)
        frame.pack(padx=10, pady=10, fill="x")
        player["frame"] = frame

        header = tk.Frame(frame, bg=COLORS["bg"])
        header.pack(fill="x", pady=(8, 0))

        player["header_label"] = tk.Label(
            header,
            text=f"PLAYER {pid + 1}",
            font=("Arial", 16, "bold"),
            fg=COLORS["text"],
            bg=COLORS["bg"]
        )
        player["header_label"].pack(side="left", padx=10)

        select_button = tk.Button(
            header,
            text="Select",
            command=lambda pid=pid: self.select_player(pid),
            bg=COLORS["button_bg"],
            fg=COLORS["button_fg"],
            font=("Arial", 9)
        )
        select_button.pack(side="right", padx=10)

        player["stats"] = tk.Label(
            frame,
            text=self.player_stats_text(pid),
            font=("Arial", 11),
            fg=COLORS["text"],
            bg=COLORS["bg"]
        )
        player["stats"].pack(pady=(0, 8))

        grid_frame = tk.Frame(frame, bg=COLORS["bg"])
        grid_frame.pack(pady=8)
        player["grid"] = []
        for r in range(MAX_ATTEMPTS):
            row_tiles = []
            for c in range(WORD_LENGTH):
                tile = tk.Label(
                    grid_frame,
                    text="",
                    width=4,
                    height=2,
                    font=("Arial", 24, "bold"),
                    bg=COLORS["tile"],
                    fg="white",
                    relief="solid",
                    bd=2
                )
                tile.grid(row=r, column=c, padx=4, pady=4)
                row_tiles.append(tile)
            player["grid"].append(row_tiles)

        player["status"] = tk.Label(
            frame,
            text="Waiting to start match...",
            font=("Arial", 12),
            fg=COLORS["text"],
            bg=COLORS["bg"]
        )
        player["status"].pack(pady=(8, 12))

        btn_frame = tk.Frame(frame, bg=COLORS["bg"])
        btn_frame.pack(pady=4)
        player["hint_button"] = tk.Button(btn_frame, text="💡 Hint", command=lambda pid=pid: self.give_hint(pid), bg=COLORS["button_bg"], fg=COLORS["button_fg"], font=("Arial", 9))
        player["hint_button"].pack(side="left", padx=5)
        tk.Button(btn_frame, text="🤖 Bot Move", command=lambda pid=pid: self.bot_move(pid), bg=COLORS["button_bg"], fg=COLORS["button_fg"], font=("Arial", 9)).pack(side="left", padx=5)
        tk.Button(btn_frame, text="🎯 Reveal", command=lambda pid=pid: self.reveal_word(pid), bg=COLORS["button_bg"], fg=COLORS["button_fg"], font=("Arial", 9)).pack(side="left", padx=5)

        self.build_keyboard(pid, frame)

    def build_keyboard(self, pid, parent):
        player = self.players[pid]
        key_frame = tk.Frame(parent, bg=COLORS["bg"])
        key_frame.pack(pady=(10, 14))

        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        for row_keys in rows:
            row_frame = tk.Frame(key_frame, bg=COLORS["bg"])
            row_frame.pack(pady=2)
            for ch in row_keys:
                button = tk.Button(
                    row_frame,
                    text=ch,
                    width=3,
                    bg=COLORS["button_bg"],
                    fg=COLORS["button_fg"],
                    font=("Arial", 9),
                    command=lambda ch=ch, pid=pid: self.add(ch, pid)
                )
                button.pack(side="left", padx=2, pady=2)
                self.keyboard_buttons[pid][ch.lower()] = button

        bottom_row = tk.Frame(key_frame, bg=COLORS["bg"])
        bottom_row.pack(pady=4)
        enter_btn = tk.Button(
            bottom_row,
            text="ENTER",
            width=6,
            bg=COLORS["green"],
            fg=COLORS["text"],
            font=("Arial", 9),
            command=lambda pid=pid: self.submit(pid)
        )
        enter_btn.pack(side="left", padx=8)
        self.keyboard_buttons[pid]["ENTER"] = enter_btn
        del_btn = tk.Button(
            bottom_row,
            text="DEL",
            width=6,
            bg=COLORS["gray"],
            fg=COLORS["text"],
            font=("Arial", 9),
            command=lambda pid=pid: self.delete(pid)
        )
        del_btn.pack(side="left", padx=8)
        self.keyboard_buttons[pid]["DEL"] = del_btn

    def restart_game(self):
        self.match_active = False
        self.setup_game()
        self.reset_boards()
        self.select_player(0)
        self.current_turn_label.config(text="Current turn: Player 1")
        self.update_stats()
        self.match_active = True

    def reset_boards(self):
        for pid, player in enumerate(self.players):
            player["row"] = 0
            player["col"] = 0
            player["current"] = [""] * WORD_LENGTH
            player["game_over"] = False
            player["solved"] = False
            player["guesses"] = 0
            player["status"].config(text="Waiting for the match to start...")
            for r in range(MAX_ATTEMPTS):
                for c in range(WORD_LENGTH):
                    player["grid"][r][c].config(text="", bg=COLORS["tile"])
            for btn in self.keyboard_buttons[pid].values():
                if btn.cget("text") == "ENTER":
                    btn.config(bg=COLORS["green"])
                elif btn.cget("text") == "DEL":
                    btn.config(bg=COLORS["gray"])
                else:
                    btn.config(bg=COLORS["button_bg"])

    def player_stats_text(self, pid):
        player = self.players[pid]
        return f"Guesses: {player['guesses']} | Score: {player['score']} | Wins: {player['wins']}"

    def update_stats(self):
        self.stats.config(text=f"Words loaded: {len(WORDS)} | Mode: {self.mode_var.get()}")
        for pid in range(2):
            self.players[pid]["stats"].config(text=self.player_stats_text(pid))

    def update_mode_ui(self):
        mode = self.mode_var.get()
        no_hints = mode in ("No Hints", "Mega Hard")
        for pid in range(2):
            button = self.players[pid]["hint_button"]
            if button:
                button.config(state="disabled" if no_hints else "normal")
        self.stats.config(text=f"Words loaded: {len(WORDS)} | Mode: {mode}")

    def update_keyboard_keys(self, pid, guess, feedback):
        player = self.players[pid]
        for ch, color in zip(guess, feedback):
            key = ch.lower()
            button = player["keyboard"].get(key)
            if not button:
                continue
            current = button.cget("bg")
            if current == COLORS["green"]:
                continue
            if color == "green":
                button.config(bg=COLORS["green"])
            elif color == "yellow" and current != COLORS["green"]:
                button.config(bg=COLORS["yellow"])
            elif color == "gray" and current not in (COLORS["green"], COLORS["yellow"]):
                button.config(bg=COLORS["gray"])

    def select_player(self, pid):
        self.active_player = pid
        for index, player in enumerate(self.players):
            if index == pid:
                player["frame"].config(highlightbackground=COLORS["accent"])
                player["header_label"].config(bg="#1f6f50")
                if player["game_over"]:
                    player["status"].config(text=f"Player {pid + 1} finished. Waiting...")
                else:
                    player["status"].config(text=f"Player {pid + 1} active. Type your guess.")
            else:
                player["frame"].config(highlightbackground=COLORS["bg"])
                player["header_label"].config(bg=COLORS["bg"])
                if not player["game_over"]:
                    player["status"].config(text=f"Player {index + 1} waiting.")
        self.current_turn_label.config(text=f"Current turn: Player {pid + 1}")
        # Enable active player's keyboard, disable others
        for p in range(2):
            state = 'normal' if p == pid else 'disabled'
            for btn in self.keyboard_buttons[p].values():
                btn.config(state=state)
        self.update_stats()

    def handle_key(self, event):
        key = event.keysym.lower()
        if key in ("tab",):
            self.select_player(1 - self.active_player)
            return
        if key in ("1", "2"):
            self.select_player(int(key) - 1)
            return
        if not self.match_active:
            return
        player = self.players[self.active_player]
        if player["game_over"]:
            return
        if key == "return":
            self.submit(self.active_player)
        elif key == "backspace":
            self.delete(self.active_player)
        elif len(key) == 1 and key.isalpha():
            self.add(key, self.active_player)

    def add(self, ch, pid):
        player = self.players[pid]
        if player["game_over"] or player["col"] >= WORD_LENGTH:
            return
        player["current"][player["col"]] = ch
        player["grid"][player["row"]][player["col"]].config(text=ch.upper())
        player["col"] += 1

    def delete(self, pid):

        player = self.players[pid]
        if player["game_over"] or player["col"] == 0:
            return
        player["col"] -= 1
        player["current"][player["col"]] = ""
        player["grid"][player["row"]][player["col"]].config(text="")

    def submit(self, pid):
        player = self.players[pid]
        if player["game_over"]:
            return
        if player["col"] != WORD_LENGTH:
            player["status"].config(text="Not enough letters!")
            return
        guess = "".join(player["current"]).lower()
        if guess not in WORDS:
            player["status"].config(text="Invalid word!")
            return
        player["guesses"] += 1
        feedback = get_feedback(guess, player["target"])
        for i in range(WORD_LENGTH):
            player["grid"][player["row"]][i].config(bg=COLORS[feedback[i]])
        self.bots[pid].update(guess, feedback)
        self.update_keyboard_keys(pid, guess, feedback)
        if guess == player["target"]:
            player["score"] += 100
            player["wins"] += 1
            player["streak"] += 1
            player["game_over"] = True
            player["solved"] = True
            player["status"].config(text=f"🏆 Player {pid + 1} solved it in {player['guesses']} guesses!")
            self.update_stats()
            self.switch_to_next_player()
            return
        player["row"] += 1
        player["col"] = 0
        player["current"] = [""] * WORD_LENGTH
        if player["row"] >= MAX_ATTEMPTS:
            player["streak"] = 0
            player["game_over"] = True
            player["status"].config(text=f"❌ Player {pid + 1} ran out of guesses. Word was {player['target'].upper()}.")
            self.update_stats()
            self.switch_to_next_player()
            return
        player["status"].config(text=f"Guess {player['guesses']} recorded. Keep going!")
        self.update_stats()
        self.select_player(1 - pid)

    def switch_to_next_player(self):
        if self.players[0]["game_over"] and not self.players[1]["game_over"]:
            self.select_player(1)
            self.players[1]["status"].config(text="Player 2 active. Type your guess.")
            return
        if self.players[0]["game_over"] and self.players[1]["game_over"]:
            self.finish_match()

    def finish_match(self):
        self.match_active = False
        p1 = self.players[0]
        p2 = self.players[1]
        if p1["solved"] and p2["solved"]:
            if p1["guesses"] < p2["guesses"]:
                winner_text = "Player 1 wins!"
            elif p2["guesses"] < p1["guesses"]:
                winner_text = "Player 2 wins!"
            else:
                winner_text = "It's a tie!"
        elif p1["solved"]:
            winner_text = "Player 1 wins!"
        elif p2["solved"]:
            winner_text = "Player 2 wins!"
        else:
            winner_text = "No one solved the word. It's a tie!"
        for pid, player in enumerate(self.players):
            player["status"].config(text=f"Match over. {winner_text}")
        messagebox.showinfo("Match Over", winner_text)

    def bot_move(self, pid):
        player = self.players[pid]
        if player["game_over"]:
            return
        guess = self.bots[pid].guess()
        player["current"] = list(guess)
        player["col"] = WORD_LENGTH
        for i, ch in enumerate(guess):
            player["grid"][player["row"]][i].config(text=ch.upper())
        self.submit(pid)

    def give_hint(self, pid):
        player = self.players[pid]
        if player["game_over"] or not self.match_active:
            return
        reveal_index = random.randint(0, WORD_LENGTH - 1)
        letter = player["target"][reveal_index].upper()
        player["status"].config(text=f"💡 Hint: letter {reveal_index + 1} is '{letter}'")

    def reveal_word(self, pid):
        player = self.players[pid]
        player["status"].config(text=f"🎯 Secret Word: {player['target'].upper()}")

    def restart(self):
        self.active_player = 0
        self.start_match()


if __name__ == "__main__":
    root = tk.Tk()
    app = MegaWordle(root)
    root.mainloop()
