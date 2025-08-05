import tkinter as tk
from tkinter import simpledialog, messagebox, colorchooser, font

# Hauptfenster erstellen

class MolyoMaps:
    def __init__(self, root):
        self.root = root
        self.root.title("Molyo Maps")




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

        self.cities = {
        "Norum": {
        "place": (405, 537) 
        },
        "Havensta": {
        "place": (406, 543) 
        },
        "Nordo Norum": {
        "place": (393, 508) 
        },
        "Neosta": {
        "place": (397, 591) 
        },
        "Nova Norum": {
        "place": (384, 633) 
        },
        "Vulcanos": {
        "place": (418, 622) 
        },
        "Watino": {
        "place": (393, 709) 
        },
        "Vocca Nord": {
        "place": (418, 760) 
        },
        "Alexandros": {
        "place": (481, 755) 
        },
        "Lapitschu": {
        "place": (482, 646) 
        },
        "Lagopitschu": {
        "place": (478, 630) 
        },
        "Asinovidum": {
        "place": (522, 384) 
        },
        "Onol": {
        "place": (522, 472) 
        },
        "Lono": {
        "place": (517, 528) 
        },
        "Kleinrom": {
        "place": (545, 600) 
        },
        "Omikron": {
        "place": (556, 579) 
        },
        "Miorago": {
        "place": (661, 382) 
        },
        "Porta_de_Nolo": {
        "place": (693, 369) 
        },
        "Porta_de_Memalo": {
        "place": (767, 365) 
        },
        "Orgrimmar": {
        "place": (788, 407) 
        },
        "Krestonum_Hareo": {
        "place": (714, 407) 
        },
        "Garabesk": {
        "place": (727, 449) 
        },
        "Elvadorey": {
        "place": (733, 510) 
        },
        "Gabio": {
        "place": (762, 554) 
        },
        "Zora_Hareo": {
        "place": (764, 578) 
        },
        "Zora": {
        "place": (758, 591) 
        },
        "Mitkro": {
        "place": (713, 623) 
        },
        "Verbindo": {
        "place": (646, 612) 
        },
        "Canalos": {
        "place": (598, 773) 
        },
        "Suedos": {
        "place": (597, 786) 
        },
        "Vocca Süd": {
        "place": (421, 780) 
        },
        "Ali": {
        "place": (460, 823) 
        },
        "Alikanasum": {
        "place": (493, 851) 
        },
        "Ka": {
        "place": (583, 903) 
        },
        "Na": {
        "place": (636, 864) 
        },
        "Sum": {
        "place": (690, 895) 
        },
        "Itochame": {
        "place": (895, 906) 
        },
        "Voda": {
        "place": (839, 790) 
        },
        "Molia": {
        "place": (730, 759) 
        },
        "Talos": {
        "place": (788, 691) 
        },
        "Aro": {
        "place": (772, 683) 
        },
        "Aroino": {
        "place": (849, 699) 
        },
        "Aroinaronoaro": {
        "place": (893, 803) 
        },
        "Tiso": {
        "place": (696, 649) 
        },
        "Völö": {
        "place": (651, 660) 
        },
        "Voeloe": {
        "place": (670, 697) 
        },
        "Radio": {
        "place": (627, 725) 
        },
        "Ritora_Forta": {
        "place": (834, 507) 
        },
        "Titana": {
        "place": (865, 298) 
        },
        "Ivora": {
        "place": (799, 291) 
        },
        "Tiza_Exodaria": {
        "place": (684, 301) 
        },
        "Amphalo": {
        "place": (627, 331) 
        },
        "Aryptikos": {
        "place": (568, 335) 
        },
        "Retoro": {
        "place": (596, 313) 
        },
        "Larissima": {
        "place": (538, 214) 
        },
        "Gommasi": {
        "place": (613, 175) 
        },
        "Orkonum": {
        "place": (616, 138) 
        },
        "Troston_Banala_iv_Maima": {
        "place": (535, 75) 
        },
        "Sol_Noverima": {
        "place": (397, 120) 
        },
        "Fero": {
        "place": (481, 147) 
        },
        "Hika": {
        "place": (478, 154) 
        },
        "Nova": {
        "place": (496, 170) 
        },
        "Kazamari": {
        "place": (487, 192) 
        },
        "Crocodilandia": {
        "place": (495, 232) 
        },
        "Darnassus": {
        "place": (482, 258) 
        },
        "Fellwell": {
        "place": (505, 303) 
        },
        "Durnhallo": {
        "place": (473, 330) 
        },
        "Shattrah": {
        "place": (633, 257) 
        },
        "Lordeon": {
        "place": (754, 240) 
        },
        "Tantalona": {
        "place": (789, 231) 
        },
        "Salve_de_Mis": {
        "place": (836, 213) 
        },
        "Storma_Vinda": {
        "place": (838, 138) 
        },
        "Bamberg": {
        "place": (878, 110) 
        },
        "Prudmora": {
        "place": (778, 170) 
        },
        "Minera": {
        "place": (732, 148) 
        },
        "Dazaran": {
        "place": (747, 203) 
        },}

        self.states = {
            "Norum": {
            "points": [414, 585, 405, 546, 409, 530, 411, 513, 390, 499, 383, 518, 383, 539, 365, 542, 362, 552, 368, 561, 370, 553, 364, 543, 382, 538, 382, 558, 381, 582, 381, 593, 397, 593, 414, 583],
            "color": "#800040"
        },


        "Watino": {
            "points": [416, 583, 398, 593, 379, 593, 378, 620, 380, 634, 382, 656, 385, 678, 389, 711, 400, 727, 416, 755, 425, 759, 437, 759, 447, 755, 471, 755, 485, 756, 478, 733, 464, 704, 455, 668, 446, 629, 440, 590, 419, 591, 416, 583],
            "color": "#ffff00"
        },


        "Lapitschu": {
            "points": [486, 755, 518, 759, 546, 763, 586, 762, 603, 759, 599, 735, 588, 705, 581, 674, 589, 654, 582, 600, 553, 598, 550, 589, 544, 586, 540, 596, 530, 590, 493, 612, 489, 597, 481, 593, 476, 599, 450, 583, 440, 590, 446, 630, 454, 667, 462, 703, 476, 730, 485, 753],
            "color": "#008040"
        },


        "Suedos": {
            "points": [547, 761, 586, 760, 604, 757, 602, 773, 596, 791, 582, 805, 570, 819, 550, 827, 526, 830, 509, 817, 501, 805, 501, 793, 510, 797, 529, 796, 545, 781, 545, 762],
            "color": "#00ffff"
        },


        "Verbindo": {
            "points": [590, 653, 581, 599, 613, 593, 626, 590, 646, 595, 677, 594, 721, 582, 727, 625, 718, 618, 715, 638, 704, 633, 670, 629, 637, 631, 605, 641, 589, 656],
            "color": "#808000"
        },


        "Voeloe": {
            "points": [701, 646, 703, 665, 693, 662, 686, 667, 681, 679, 681, 694, 675, 701, 648, 704, 638, 715, 628, 724, 621, 722, 631, 708, 617, 704, 611, 684, 619, 665, 633, 673, 653, 676, 669, 661, 683, 657, 691, 653, 685, 643, 700, 646],
            "color": "#0000ff"
        },


        "Völö": {
            "points": [669, 659, 653, 675, 633, 674, 617, 664, 626, 661, 642, 661, 668, 657],
            "color": "#00ff80"
        },


        "Aro": {
            "points": [721, 581, 742, 575, 757, 577, 769, 582, 802, 587, 830, 587, 844, 609, 850, 632, 824, 644, 798, 646, 800, 657, 798, 646, 788, 640, 773, 647, 773, 665, 774, 682, 783, 688, 791, 688, 790, 693, 783, 688, 773, 681, 773, 699, 769, 713, 763, 732, 740, 735, 696, 730, 702, 708, 716, 676, 717, 648, 716, 639, 717, 618, 727, 624, 720, 581],
            "color": "#00ffff"
        },


        "Molia": {
            "points": [764, 732, 739, 732, 696, 729, 692, 745, 694, 766, 711, 776, 735, 783, 764, 782, 790, 781, 814, 783, 821, 784, 832, 780, 847, 785, 832, 778, 821, 783, 816, 759, 795, 733, 787, 742, 771, 742, 764, 730],
            "color": "#8080c0"
        },


        "Aroino": {
            "points": [796, 735, 816, 757, 821, 783, 831, 778, 845, 783, 869, 791, 871, 769, 864, 735, 853, 708, 845, 670, 848, 631, 825, 642, 798, 644, 801, 657, 805, 675, 807, 706, 795, 733, 814, 754, 822, 780],
            "color": "#ffffff"
        },


        "Aroinaronoaro": {
            "points": [830, 587, 843, 608, 848, 630, 858, 635, 868, 645, 878, 668, 884, 694, 890, 720, 895, 752, 896, 776, 891, 787, 892, 800, 903, 804, 920, 786, 928, 763, 930, 730, 923, 691, 909, 644, 902, 606, 890, 592, 868, 591, 829, 586],
            "color": "#ff8000"
        },


        "Voda": {
            "points": [868, 789, 846, 782, 830, 775, 823, 778, 825, 792, 814, 814, 789, 831, 761, 843, 731, 847, 725, 865, 732, 873, 735, 893, 765, 885, 790, 880, 814, 867, 837, 859, 855, 838, 868, 827, 867, 789],
            "color": "#ff0000"
        },


        "Alikanasum": {
            "points": [730, 846, 725, 864, 733, 873, 735, 893, 704, 894, 671, 900, 625, 903, 587, 905, 554, 901, 517, 900, 482, 888, 452, 878, 438, 853, 426, 842, 411, 816, 401, 792, 413, 783, 418, 776, 433, 788, 458, 814, 478, 831, 498, 846, 521, 859, 549, 861, 581, 865, 624, 865, 639, 863, 656, 855, 678, 850, 703, 852, 730, 845],
            "color": "#ff00ff"
        },


        "Asinovidum": {
            "points": [449, 581, 474, 598, 480, 591, 488, 595, 491, 611, 529, 587, 510, 579, 502, 548, 501, 515, 502, 485, 509, 451, 508, 429, 526, 390, 520, 380, 513, 369, 501, 377, 483, 395, 470, 412, 466, 446, 465, 487, 460, 533, 456, 567, 448, 581],
            "color": "#004080"
        },


        "Onol": {
            "points": [523, 444, 514, 458, 514, 466, 520, 471, 526, 467, 525, 443],
            "color": "#00ff00"
        },


        "Lono": {
            "points": [515, 499, 511, 506, 510, 530, 519, 530, 521, 504, 516, 497],
            "color": "#00006a"
        },


        "Elvadorey": {
            "points": [700, 505, 703, 490, 712, 486, 703, 407, 708, 392, 720, 393, 725, 403, 715, 406, 704, 406, 713, 485, 726, 482, 736, 485, 747, 491, 753, 501, 738, 503, 735, 507, 739, 517, 753, 539, 769, 543, 769, 550, 737, 556, 737, 548, 752, 540, 739, 517, 734, 527, 714, 526, 699, 506],
            "color": "#fb007d"
        },


        "Itochame": {
            "points": [894, 880, 853, 908, 851, 924, 861, 932, 880, 924, 898, 907, 894, 892, 903, 882, 895, 880],
            "color": "#804000"
        },
        #=========================================================================================
        #=====Ab hier Testweise======
        #=========================================================================================

        "Aryptikos": {
            "points": [556, 581, 532, 556, 529, 491, 536, 439, 540, 396, 541, 340, 565, 322, 606, 325, 631, 318, 637, 323, 628, 337, 619, 371, 616, 421, 607, 473, 593, 523, 578, 566, 567, 579, 557, 579],
            "color": "#ff0080"
        },


        "Durnhallo": {
            "points": [565, 321, 543, 280, 530, 241, 526, 200, 491, 199, 475, 203, 479, 233, 476, 250, 462, 266, 446, 274, 444, 281, 451, 291, 442, 305, 460, 312, 449, 323, 469, 320, 471, 326, 475, 334, 503, 327, 528, 325, 541, 338, 564, 320],
            "color": "#ffc6ff"
        },


        "Troston": {
            "points": [476, 201, 464, 192, 446, 190, 431, 157, 428, 121, 411, 113, 402, 123, 387, 124, 390, 108, 402, 107, 400, 99, 387, 99, 387, 92, 401, 93, 413, 102, 410, 112, 427, 119, 436, 104, 453, 88, 473, 73, 500, 63, 527, 64, 544, 79, 543, 101, 524, 118, 506, 135, 498, 149, 503, 163, 525, 169, 527, 199, 493, 200, 476, 201],
            "color": "#fd5200"
        },


        "Orkonum": {
            "points": [526, 172, 526, 197, 558, 200, 593, 214, 644, 212, 687, 192, 740, 181, 753, 139, 726, 147, 691, 153, 653, 153, 636, 127, 617, 120, 593, 136, 575, 162, 545, 173, 526, 169, 527, 197],
            "color": "#5c2e2e"
        },


        "Shattrah": {
            "points": [638, 322, 672, 311, 700, 304, 748, 303, 753, 257, 783, 219, 743, 209, 740, 181, 688, 191, 643, 212, 595, 213, 527, 198, 530, 239, 543, 279, 566, 319, 605, 322],
            "color": "#ae5eff"
        },


        "Tantalone": {
            "points": [783, 264, 752, 256, 785, 218, 742, 208, 742, 180, 752, 137, 786, 124, 796, 153, 808, 186, 814, 206, 798, 219, 801, 239, 783, 263],
            "color": "#6f006f"
        },


        "Titana": {
            "points": [748, 302, 753, 254, 785, 261, 827, 265, 868, 274, 877, 286, 879, 319, 878, 356, 872, 397, 863, 432, 853, 462, 844, 494, 835, 508, 824, 508, 816, 491, 821, 453, 828, 419, 831, 387, 830, 349, 821, 322, 795, 313, 747, 300, 753, 254],
            "color": "#0dff86"
        },


        "Bamberg": {
            "points": [878, 287, 876, 226, 868, 199, 866, 167, 877, 131, 885, 108, 878, 104, 849, 119, 818, 119, 786, 124, 795, 153, 806, 185, 814, 204, 798, 217, 802, 236, 786, 258, 826, 264, 866, 272, 877, 286],
            "color": "#808040"
        },


        "Krestonum": {
            "points": [700, 406, 677, 407, 662, 395, 660, 374, 675, 359, 697, 366, 720, 363, 741, 356, 762, 351, 777, 365, 777, 383, 786, 395, 794, 394, 806, 400, 807, 406, 802, 411, 785, 409, 738, 446, 722, 449, 718, 446, 731, 441, 737, 446, 785, 408, 783, 401, 785, 395, 777, 383, 765, 396, 741, 402, 730, 405, 720, 391, 710, 395, 701, 405],
            "color": "#730e8c"
        },




        }
        tk.Button(self.root, text="Parteien erstellen", command=self.parties).pack()
        self.List = []

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw()
    def on_click(self, event):
        items = self.canvas.find_withtag("current")
        if items:
            tags = self.canvas.gettags(items[0])
            if tags:
                state_name = tags[0]
                state_name = state_name.replace("_", " ")
                messagebox.showinfo("Staat", f"Du hast auf '{state_name}' geklickt.")

    def draw(self):
        capitals = ["Norum", "Orkonum"]
        state_capitals = ["Watino", "Lapitschu", "Asinovidum", "Onol", "Lono", "Verbindo", "Aro", "Aroino", "Aroinaronoaro", "Voda", "Itochame", "Ka", "Suedos", "Tiso", "Völö", "Molia", "Elvadorey", "Aryptikos", "Durnhallo", "Troston_Banala_iv_Maima", "Shattrah", "Salve_de_Mis", "Bamberg", "Titana", "Porta_de_Nolo"]
        capitalfont = font.Font(weight="bold", family="Arial", size=11, underline=True)
        for part in state_capitals and capitals:
            part.replace(" ", "_")
        for name, state in self.states.items():
            name_with_space = name.replace("_", " ")
            points = state["points"]
            color = state["color"]

            self.canvas.create_polygon(points, fill=color, outline="black", width=2, tags=name)
        for name, city in self.cities.items():
            name_with_space = name.replace("_", " ")
            place = city["place"]
            self.canvas.create_oval(place[0], place[1], place[0] + 2, place[1] + 2, fill="red", outline="black", tags=name)
            if name.replace(" ", "_") in capitals:
                self.canvas.create_text(place[0]-15, place[1], text=name_with_space, anchor=tk.E, font=capitalfont, tags=name)
            elif name.replace(" ", "_") in state_capitals:
                self.canvas.create_text(place[0]-15, place[1], text=name_with_space, anchor=tk.E, font=("Arial", 10, "bold"), tags=name)
            else:
                self.canvas.create_text(place[0]-15, place[1], text=name_with_space, anchor=tk.E, tags=name)
    

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
