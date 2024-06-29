import tkinter as tk
import sys
import random

vesalice = ['kompjuter', 'monitor', 'tastatura', 'mis', 'procesor', 'graficka', 'memorija', 'hard', 'disk', 'ssd',
            'napajanje', 'kuciste', 'mreza', 'internet', 'kamera', 'skener', 'stampac', 'zvucnici', 'slusalice',
            'mikrofon', 'tastatura']

broj_pokusaja = 7


def zatvori_prozorce():
    prozor.destroy()
    sys.exit()

def kada_kliknem_na_play():
    global broj_pokusaja
    prvi_tekst.grid_forget()
    play.grid_forget()
    Quit.grid_forget()
    opis.grid_forget()

    global rec
    rec = random.choice(vesalice)
    global otkrivena_slova
    otkrivena_slova = ["_" for _ in rec]

    VESALICA = tk.Label(text="DOBRODOŠAO U IGRU VESALICA", font=("Helvetica", 20), bg="peach puff", fg="black")
    VESALICA.grid(row=0, column=0, columnspan=2, pady=20)

    pogodi_slovo = tk.Label(text="Pogodi slovo", font=("Helvetica", 15), bg="peach puff", fg="black")
    pogodi_slovo.grid(row=1, column=0, padx=10, pady=10)

    global unos_slova, unos_slova_entry
    unos_slova = tk.StringVar()  
    unos_slova_entry = tk.Entry(prozor, textvariable=unos_slova, font=("Helvetica", 14))  
    unos_slova_entry.grid(row=1, column=1, padx=10, pady=10)

    def slovca():
        global broj_pokusaja
        slovo = unos_slova.get().lower()
        if len(slovo) > 1:
            greska.config(text="Ne možeš da uneseš više od jednog slova", font=("Helvetica", 14), bg="peach puff", fg="black")
        else:
            if slovo in rec:
                for i in range(len(rec)):
                    if rec[i] == slovo:
                        otkrivena_slova[i] = slovo
                prikazi_otkrivena_slova()
                if "_" not in otkrivena_slova:
                    rip.config(text="Čestitamo, pobijedili ste!")
            else:
                broj_pokusaja -= 1
                if broj_pokusaja == 6:
                    coveculjak1.grid_forget()
                    coveculjak1.grid(row=4, column=0, columnspan=2, sticky="e")
                elif broj_pokusaja == 5:
                    coveculjak2.grid_forget()
                    coveculjak2.grid(row=4, column=0, columnspan=2, sticky="e")
                elif broj_pokusaja == 4:
                    coveculjak3.grid_forget()
                    coveculjak3.grid(row=4, column=0, columnspan=2, sticky="e")
                elif broj_pokusaja == 3:
                    coveculjak4.grid_forget()
                    coveculjak4.grid(row=4, column=0, columnspan=2, sticky="e")
                elif broj_pokusaja == 2:
                    coveculjak5.grid_forget()
                    coveculjak5.grid(row=4, column=0, columnspan=2, sticky="e")
                elif broj_pokusaja == 1:
                    coveculjak6.grid_forget()
                    coveculjak6.grid(row=4, column=0, columnspan=2, sticky="e")
                elif broj_pokusaja == 0:
                    rip.config(text="GAME OVER")

    ok = tk.Button(text="OK", command=slovca, font=("Helvetica", 14), bg="peach puff", fg="black")
    ok.grid(row=2, column=0, columnspan=2, pady=10)
    
    greska.grid(row=5, column=0, columnspan=2, pady=10)

    global coveculjak1, coveculjak2, coveculjak3, coveculjak4, coveculjak5, coveculjak6, rip
    coveculjak1 = tk.Label(prozor, font=("Courier", 10), text="""
           -----
           |   |
               |
               |
               |
               |
        """)
    coveculjak1.grid(row=4, column=0, columnspan=2, sticky="e")
    coveculjak2 = tk.Label(prozor, font=("Courier", 10), text="""
           -----
           |   |
           O   |
               |
               |
               |
        """)
    coveculjak3 = tk.Label(prozor, font=("Courier", 10), text="""
           -----
           |   |
           O   |
           |   |
               |
               |
        """)
    coveculjak4 = tk.Label(prozor, font=("Courier", 10), text="""
           -----
           |   |
           O   |
          /|   |
               |
               |
        """)
    coveculjak5 = tk.Label(prozor, font=("Courier", 10), text="""
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        """)
    coveculjak6 = tk.Label(prozor, font=("Courier", 10), text="""
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        """)
    rip = tk.Label(prozor, font=("Courier", 14))

def prikazi_otkrivena_slova():
    tekst = " ".join(otkrivena_slova)
    otkrivena_slova_label.config(text=tekst)

prozor = tk.Tk()

prozor.config(bg="peach puff")  
prozor.title("Vesalica") 

prvi_tekst = tk.Label(prozor, text="VESALICA", font=("Helvetica", 30), bg="peach puff", fg="black") 
prvi_tekst.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

play = tk.Button(prozor, text="PLAY", font=("Helvetica", 20), bg="peach puff", fg="black", command=kada_kliknem_na_play)
play.grid(row=1, column=0, padx=10, pady=10)

Quit = tk.Button(prozor, text="QUIT", font=("Helvetica", 20), bg="peach puff", fg="black", command=zatvori_prozorce)
Quit.grid(row=1, column=1, padx=10, pady=10)

opis = tk.Label(prozor, text="Najjača igra napravljena od strane Andrije Stosica", font=("Helvetica", 5), bg="peach puff", fg="black")
opis.grid(row=2, column=0, columnspan=2, pady=10)

greska = tk.Label(prozor, text="", font=("Helvetica", 14), bg="peach puff", fg="black")

otkrivena_slova_label = tk.Label(prozor, font=("Helvetica", 14), bg="peach puff", fg="black")
otkrivena_slova_label.grid(row=3, column=0, columnspan=2, pady=10)

prozor.mainloop()
