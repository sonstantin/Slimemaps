import tkinter as tk
from tkinter import simpledialog, messagebox, colorchooser, font, filedialog
import json
from PIL import Image, ImageDraw, ImageFont

# Hauptfenster erstellen

class MolyoMaps:
    def __init__(self, root):
        self.root = root
        self.root.title("Molyo Maps")


        self.imagewidth = 1000
        self.imageheight = 1000
        self.image = Image.new("RGB", (self.imagewidth, self.imageheight), "white")
        self.drawImage = ImageDraw.Draw(self.image)

        # Scrollbare Frame-Struktur
        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True)

        # Scrollbars erstellen
        h_scroll = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)

        v_scroll = tk.Scrollbar(frame, orient=tk.VERTICAL)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)

        # Canvas mit Scrollregion
        self.canvas = tk.Canvas(frame, width=800, height=600, bg="white",
                        xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set,
                        scrollregion=(0, 0, 4000, 4000))
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        h_scroll.config(command=self.canvas.xview)
        v_scroll.config(command=self.canvas.yview)

        # Polygon zeichnen
        self.selected = ""
        self.capitals = []
        self.state_capitals = []
        self.cities = {}

        self.states = {}
        tk.Button(self.root, text="Parteien erstellen", command=self.parties).pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="Laden", command=self.prepare_load).pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="Karte als PNG exportieren", command=self.export).pack(side=tk.LEFT, padx=5)
        self.List = []

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw()

    def export(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG-Datei", "*.png")],
            title="Wähle den Ort zum speichern des Bildes"
        )
        if path:  # Falls nicht abgebrochen
            self.image.save(path)


    def load_countries(self):
        path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON-Dateien", "*.json")], title="Wähle deine Länderdatei")
        with open(path, mode="r", encoding="utf-8") as f:
            self.states = json.load(f)
        self.draw()
    def load_cities(self):
        path = filedialog.askopenfilename(defaultextension=".json", filetypes=[("JSON-Dateien", "*.json")], title="Wähle deine Städtedatei")
        with open(path, mode="r", encoding="utf-8") as f:
            data = json.load(f)
        
        self.cities = data[2]
        self.capitals = data[0]
        self.state_capitals = data[1]
        self.draw()
    def prepare_load(self):
        window = tk.Toplevel(self.root)
        window.title("Willst du Städte oder Länder laden?")
        tk.Button(window, text="Länder laden", command=self.load_countries).pack()
        tk.Button(window, text="Städte laden", command=self.load_cities).pack()
    def on_click(self, event):
        items = self.canvas.find_withtag("current")
        if items:
            tags = self.canvas.gettags(items[0])
            if tags:
                state_name = tags[0]
                state_name = state_name.replace("_", " ")
                messagebox.showinfo("Staat", f"Du hast auf '{state_name}' geklickt.")

    def draw(self):
        
        capitalimagefont = ImageFont.truetype("arialbd.ttf", 11)
        normalimagefont = ImageFont.truetype("arial.ttf", 10)
        boldimagefont = ImageFont.truetype("arialbd.ttf", 10)
        
        capitalfont = font.Font(weight="bold", family="Arial", size=11, underline=True)
        boldfont = ("Arial", 10, "bold")
        normalfont = ("Arial", 10)
        
        
        for name, state in self.states.items():
            points = state["points"]
            color = state["color"]
            self.canvas.create_polygon(points, fill=color, outline="black", width=2, tags=name)
            self.drawImage.polygon(points, fill=color, outline="black", width=2)

        
        for name, city in self.cities.items():
            name_with_space = name.replace("_", " ")
            place = city["place"]
            
            self.canvas.create_oval(place[0], place[1], place[0] + 2, place[1] + 2, fill="red", outline="black", tags=name)
            self.drawImage.ellipse((place[0], place[1], place[0] + 2, place[1] + 2), fill="red", outline="black")

            
            if name.replace(" ", "_") in self.capitals:
                self.canvas.create_text(place[0]-15, place[1], text=name_with_space, anchor=tk.E, font=capitalfont, tags=name)
                
                self.drawImage.text((place[0] - 15, place[1]), text=name_with_space, fill="black", font=capitalimagefont)
                
                
                bbox = self.drawImage.textbbox((place[0] - 15, place[1]), name_with_space, font=capitalimagefont)
                width = bbox[2] - bbox[0]
                height = bbox[3] - bbox[1]

                
                start = (place[0] - 15, place[1] + height + 2)
                end = (place[0] - 15 + width, place[1] + height + 2)
                self.drawImage.line([start, end], fill="black", width=1)

            elif name.replace(" ", "_") in self.state_capitals:
                self.canvas.create_text(place[0]-15, place[1], text=name_with_space, anchor=tk.E, font=boldfont, tags=name)
                self.drawImage.text((place[0] - 15, place[1]), text=name_with_space, fill="black", font=boldimagefont)
            else:
                self.canvas.create_text(place[0]-15, place[1], text=name_with_space, anchor=tk.E, font=normalfont, tags=name)
                self.drawImage.text((place[0] - 15, place[1]), text=name_with_space, fill="black", font=normalimagefont)

    

    def setparty(self, state):
        self.window = tk.Toplevel(self.root)
        self.window.title("Wähle die Partei für " + state)
        self.window.grab_set()  # macht das Fenster modal

        tk.Label(self.window, text=state, font=("Helvetica", 20)).pack()

        self.choose = tk.Listbox(self.window, font=("Helvetica", 14))
        self.choose.pack()

        for party in self.parteien:
            self.choose.insert(tk.END, party["name"])

        self.selected_index = None

        def confirm():
            selection = self.choose.curselection()
            if selection:
                self.selected_index = selection[0]
                self.window.destroy()

        tk.Button(self.window, text="Bestätigen", command=confirm).pack()
        self.window.bind("<Return>", lambda e: confirm())  # Enter-Taste

        self.window.wait_window()  # BLOCKT, bis Fenster geschlossen ist
        return self.selected_index

    def on_select(self):
        selection = self.choose.curselection()
        if selection:
            self.selected_index.append(selection[0])
        self.window.destroy()

        

        # Rückgabe
        return self.selected_index[0] if self.selected_index else None


            
    def parties(self):
        for part in self.List:
            part.destroy()
        no = []
        often = simpledialog.askinteger("Wie viele", "Wie viele Parteien soll es geben")
        if not often:
            return

        self.parteien = []
        for index in range(often):
            name = simpledialog.askstring("Name", "Was soll der Name der Partei sein?")
            color = colorchooser.askcolor()[1]
            if not name or not color:
                return
            self.parteien.append({"name": name, "color": color, "members": []})

        print(self.parteien)

        for state in self.states:
            if state not in no:
                index = self.setparty(state)
                if index is not None:
                    self.states[state]["color"] = self.parteien[index]["color"]
                    no.append(state)

        self.draw()
        self.List = []
        for party in self.parteien:
            new = tk.Label(self.root, text=f'{party["name"]}', bg=party["color"])
            self.List.append(new)
            for part in self.List:
                part.pack()

        

        
    def run(self):
        # Hauptschleife starten
        self.root.mainloop()
if __name__ == "__main__":
    root = tk.Tk()
    molyomaps = MolyoMaps(root)
    molyomaps.run()
