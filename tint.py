import tkinter as tk

# Map moods to subtle tint colors and their hex values
MOOD_COLORS = {
    "positive": "#00FF00",  # green
    "negative": "#FF0000",  # red
    "neutral":  "#0000FF",  # blue
}

def show_tint(mood, duration_ms=5000):
    """Display a subtle full-screen color tint based on mood."""
    color = MOOD_COLORS.get(mood, "#0000FF")

    root = tk.Tk()
    root.attributes("-fullscreen", True)    # fill the screen
    root.attributes("-alpha", 0.15)         # very transparent (0.0 to 1.0)
    root.attributes("-topmost", True)       # stay on top of other windows
    root.configure(bg=color)

    # Make it click-through by lifting and not grabbing focus
    root.overrideredirect(True)             # no title bar or borders

    # Label showing the mood in the corner
    label = tk.Label(root, text=f"News mood: {mood}", bg=color,
                     fg="white", font=("Arial", 14))
    label.place(x=10, y=10)

    # Auto-close after duration_ms milliseconds
    root.after(duration_ms, root.destroy)
    root.mainloop()

if __name__ == "__main__":
    show_tint("positive")