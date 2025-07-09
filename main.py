
import tkinter as tk

class Overlay(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Overlay")
        self.geometry("200x100+100+100")
        self.overrideredirect(True)
        self.attributes("-alpha", 0.5)  # Set transparency (0.0 to 1.0)
        self.attributes("-topmost", True)

        self.grip = tk.Label(self, text="Drag me", bg="gray")
        self.grip.pack(fill=tk.BOTH, expand=True)

        self.grip.bind("<ButtonPress-1>", self.start_move)
        self.grip.bind("<ButtonRelease-1>", self.stop_move)
        self.grip.bind("<B1-Motion>", self.do_move)

        self._offset_x = 0
        self._offset_y = 0

    def start_move(self, event):
        self._offset_x = event.x
        self._offset_y = event.y

    def stop_move(self, event):
        self._offset_x = None
        self._offset_y = None

    def do_move(self, event):
        x = self.winfo_pointerx() - self._offset_x
        y = self.winfo_pointery() - self._offset_y
        self.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    app = Overlay()
    app.mainloop()
