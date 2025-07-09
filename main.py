import tkinter as tk
import threading
import g4f

class Overlay(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("neurum")
        self.geometry("400x50+100+100") # Initial size for just the entry
        self.overrideredirect(True)
        self.attributes("-alpha", 0.7)  # Set transparency (0.0 to 1.0)
        self.attributes("-topmost", True)

        self.wm_attributes("-transparentcolor", "red") # Make 'red' pixels transparent

        self.canvas = tk.Canvas(self, bg="red", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.entry = tk.Entry(self.canvas, bd=0, bg="gray", fg="white", font=("Helvetica", 12), highlightthickness=0, relief="flat")
        self.placeholder_text = "ask"
        self.placeholder_color = "lightgray"
        self.default_fg_color = "white"

        self.entry.insert(0, self.placeholder_text)
        self.entry.config(fg=self.placeholder_color)

        self.entry_window = self.canvas.create_window(200, 25, window=self.entry, anchor="center", width=360, height=30)

        self.entry.bind("<FocusIn>", self.on_focus_in)
        self.entry.bind("<FocusOut>", self.on_focus_out)
        self.entry.bind("<Return>", self.generate_response) # Bind Enter key

        # Text widget for displaying LLM response
        self.response_text = tk.Text(self.canvas, wrap=tk.WORD, bg="gray", fg="white", font=("Helvetica", 12), height=0, bd=0, highlightthickness=0, relief="flat")
        self.response_text_window = None # Will be created when response is shown

        self.bind("<Configure>", self.on_window_configure) # Bind for resizing

        self.draw_rounded_rectangle()

        self._offset_x = 0
        self._offset_y = 0

    def draw_rounded_rectangle(self):
        self.canvas.delete("all")
        width = self.winfo_width()
        height = self.winfo_height()
        radius = 20 # Adjust for desired roundness
        self.canvas.create_oval(0, 0, radius*2, radius*2, fill="gray", outline="gray")
        self.canvas.create_oval(width-radius*2, 0, width, radius*2, fill="gray", outline="gray")
        self.canvas.create_oval(0, height-radius*2, radius*2, height, fill="gray", outline="gray")
        self.canvas.create_oval(width-radius*2, height-radius*2, width, height, fill="gray", outline="gray")
        self.canvas.create_rectangle(radius, 0, width-radius, height, fill="gray", outline="gray")
        self.canvas.create_rectangle(0, radius, width, height-radius, fill="gray", outline="gray")

        # Re-position widgets on the canvas
        self.canvas.coords(self.entry_window, width / 2, 25)
        if self.response_text_window:
            self.canvas.coords(self.response_text_window, width / 2, 25 + self.entry.winfo_height() + 10 + self.response_text.winfo_height() / 2)


    def on_window_configure(self, event):
        self.draw_rounded_rectangle()

    def on_focus_in(self, event):
        if self.entry.get() == self.placeholder_text:
            self.entry.delete(0, tk.END)
            self.entry.config(fg=self.default_fg_color)

    def on_focus_out(self, event):
        if not self.entry.get():
            self.entry.insert(0, self.placeholder_text)
            self.entry.config(fg=self.placeholder_color)

    def generate_response(self, event=None):
        prompt = self.entry.get()
        if prompt == self.placeholder_text or not prompt.strip():
            return

        self.entry.config(state=tk.DISABLED) # Disable entry during generation
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, "Generating response...")
        self.response_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.update_idletasks() # Update window to show "Generating response..."

        # Adjust window size to accommodate response_text
        current_width = self.winfo_width()
        current_height = self.winfo_height()
        self.geometry(f"{current_width}x{current_height + 150}") # Increase height by 150 for response

        threading.Thread(target=self._get_llm_response, args=(prompt,)).start()

    def _get_llm_response(self, prompt):
        try:
            response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4o_mini,
                messages=[{"role": "user", "content": prompt}],
                stream=False,
            )
            self.after(0, self.update_response_text, response)
        except Exception as e:
            self.after(0, self.update_response_text, f"Error: {e}")

    def update_response_text(self, response):
        self.response_text.delete(1.0, tk.END)
        self.response_text.insert(tk.END, response)
        self.entry.config(state=tk.NORMAL) # Re-enable entry
        self.entry.delete(0, tk.END)
        self.on_focus_out(None) # Reset placeholder

if __name__ == "__main__":
    app = Overlay()
    app.mainloop()
