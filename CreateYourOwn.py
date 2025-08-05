import tkinter as tk
from tkinter import filedialog, simpledialog
from PIL import Image, ImageTk

class PolygonTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Generate it")

        # Größeres Canvas
        self.canvas_width = 1280
        self.canvas_height = 960
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()
        
        
        

        self.points = []
        self.original_image = None
        self.display_image = None
        self.tk_image = None
        self.image_offset = (0, 0)
        self.scale = 1

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Bild laden", command=self.load_image).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Zurücksetzen", command=self.reset).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Befehl ausgeben", command=self.export_command).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx = 5)

        self.output = tk.Text(root, height=4, font=("Courier", 10))
        self.output.pack(fill=tk.X)

        self.canvas.bind("<Button-1>", self.add_point)
        self.canvas.bind("<Button-3>", self.saycoordinates)
    def load_image(self):
        filepath = filedialog.askopenfilename(filetypes=[("Bilder", "*.png;*.jpg;*.jpeg;*.gif")])
        if not filepath:
            return

        # Bild laden
        self.original_image = Image.open(filepath)
        img_w, img_h = self.original_image.size

        # Berechne Skalierung zum Einpassen ohne Verzerrung
        scale_w = self.canvas_width / img_w
        scale_h = self.canvas_height / img_h
        self.scale = min(scale_w, scale_h)

        # Neue Größe mit Skalierung
        new_w = int(img_w * self.scale)
        new_h = int(img_h * self.scale)
        self.display_image = self.original_image.resize((new_w, new_h), Image.ANTIALIAS)
        self.tk_image = ImageTk.PhotoImage(self.display_image)

        # Offset berechnen (um Bild zu zentrieren)
        offset_x = (self.canvas_width - new_w) // 2
        offset_y = (self.canvas_height - new_h) // 2
        self.image_offset = (offset_x, offset_y)

        self.reset(clear_image=False)
        self.canvas.create_image(offset_x, offset_y, anchor=tk.NW, image=self.tk_image)

        # <-- HIER: Zustände zeichnen, wenn das Bild geladen ist
        self.draw_states()

    


    def clear(self):
        self.points = []
    def saycoordinates(self, event):
        x_canvas, y_canvas = event.x, event.y
        ox, oy = self.image_offset

        x_real = int((x_canvas - ox) / self.scale)
        y_real = int((y_canvas - oy) / self.scale)
        name = simpledialog.askstring("Name", "Was soll der Name sein?")
        
        # Punkt auf Canvas zeichnen (kleiner roter Kreis)
        self.canvas.create_oval(x_canvas-3, y_canvas-3, x_canvas+3, y_canvas+3, fill="red")

        # Ausgabe ins Textfeld
        self.output.insert(tk.END, f'\n"{name}": {{\n "place": ({x_real}, {y_real}) \n}},')


    def add_point(self, event):
        x_canvas, y_canvas = event.x, event.y
        ox, oy = self.image_offset

        
        

        # Reale Bildkoordinaten berechnen (rückskalieren)
        x_real = int((x_canvas - ox) / self.scale)
        y_real = int((y_canvas - oy) / self.scale)

        self.points.append((x_real, y_real))

        # Markierung auf Canvas zeichnen
        self.canvas.create_oval(x_canvas-3, y_canvas-3, x_canvas+3, y_canvas+3, fill="red")
        if len(self.points) > 1:
            x1, y1 = self.points[-2]
            x2, y2 = self.points[-1]

            # Wieder auf Canvas-Koordinaten skalieren
            cx1, cy1 = x1 * self.scale + ox, y1 * self.scale + oy
            cx2, cy2 = x2 * self.scale + ox, y2 * self.scale + oy

            self.canvas.create_line(cx1, cy1, cx2, cy2, fill="blue", width=2)

    def reset(self, clear_image=True):
        self.points = []
        self.canvas.delete("all")
        if self.tk_image and not clear_image:
            self.canvas.create_image(*self.image_offset, anchor=tk.NW, image=self.tk_image)
        self.output.delete("1.0", tk.END)

    def export_command(self):
        import tkinter.simpledialog as simpledialog
        import tkinter.colorchooser as colorchooser

        if not self.points:
            self.output.insert(tk.END, "Keine Punkte gesetzt.\n")
            return

        # Name abfragen
        name = simpledialog.askstring("Name eingeben", "Name des neuen Gebiets:")
        if not name:
            self.output.insert(tk.END, "Kein Name eingegeben – abgebrochen.\n")
            return

        # Farbe wählen
        color = colorchooser.askcolor(title="Farbe für das Gebiet wählen")[1]
        if not color:
            self.output.insert(tk.END, "Keine Farbe gewählt – abgebrochen.\n")
            return

        # Punkte auflisten (flache Liste)
        flat_points = [coord for point in self.points for coord in point]

        # Eintrag als Dictionary-Zeile im Stil von `states = {...}`
        entry = f'"{name}": {{\n    "points": {flat_points},\n    "color": "{color}"\n}},\n'

        # Ausgabe ins Textfeld
        self.output.insert(tk.END, f"\n{entry}\n")

        # Punkte löschen
        self.clear()

# Start the App
if __name__ == "__main__":
    root = tk.Tk()
    app = PolygonTool(root)
    root.mainloop()
