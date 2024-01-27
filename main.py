import tkinter as tk
import wc


# Calcul
def calcule ():
    
    entries_non_vide = [entry for entry in entries if entry[0].get() != ""]

    if var_methode.get() == 0:
        max_wc, min_wc, it_wc = wc.calcul_wc(entries_non_vide)
        print(f"L'intervalle de tolérance est de : {it_wc}")
        print(f"Le maximum est de : {max_wc}")
        print(f"Le minimum est de : {min_wc}")

# Ajout ligne
def ajouter_ligne():
    global next_row


    label_cote = tk.Label(root, text=next_row)
    label_cote.grid(row=next_row, column=0, sticky='ns', padx=10, pady=5)

    entry_nom_cote = tk.Entry(root)
    entry_nom_cote.grid(row=next_row, column=1, sticky='w', padx=10, pady=5)
    entry_nom_cote.config(width=15)

    entry_cote = tk.Entry(root)
    entry_cote.grid(row=next_row, column=2, sticky='w', padx=10, pady=5)
    entry_cote.config(width=10)

    entry_upper = tk.Entry(root)
    entry_upper.grid(row=next_row, column=3, sticky='w', padx=10, pady=5)
    entry_upper.config(width=10)

    entry_lower = tk.Entry(root)
    entry_lower.grid(row=next_row, column=4, sticky='w', padx=10, pady=5)
    entry_lower.config(width=10)

    liste_sens = ["+", "-"]
    var_sens = tk.StringVar(root)
    option_menu_sens = tk.OptionMenu(root, var_sens, *liste_sens)
    option_menu_sens.grid(row=next_row, column=5, sticky='e', padx=10, pady=5)


    entries.append([entry_cote, entry_upper, entry_lower, var_sens])
    noms.append([entry_nom_cote])


    next_row += 1
    bouton_ajout.grid(row=next_row, column=0, columnspan=5, pady=10)

        
# Création de la fenêtre principale
root = tk.Tk()
root.title("Application de calcul de chaîne de cotes 1D.")

# Création des entêtes de tableau d'entrée
label_nb_cote = tk.Label(root, text="#")
label_nb_cote.grid(row=0, column=0, sticky='ns', padx=10, pady=5)

label_nom_cote = tk.Label(root, text="Désignation")
label_nom_cote.grid(row=0, column=1, sticky='ns', padx=10, pady=5)

label_cote = tk.Label(root, text="Cotes")
label_cote.grid(row=0, column=2, sticky='ns', padx=10, pady=5)

label_upper = tk.Label(root, text="Tol +")
label_upper.grid(row=0, column=3, sticky='ns', padx=10, pady=5)

label_lower = tk.Label(root, text="Tol -")
label_lower.grid(row=0, column=4, sticky='ns', padx=10, pady=5)

label_sens = tk.Label(root, text="Sens")
label_sens.grid(row=0, column=5, sticky='ns', padx=10, pady=5)

# Paramètres
next_row = 1
entries = []
noms =[]

# Donnés d'entrées
label_cote_1 = tk.Label(root, text="1")
label_cote_1.grid(row=1, column=0, sticky='ns', padx=10, pady=5)

entry_nom_cote_1 = tk.Entry(root)
entry_nom_cote_1.grid(row=1, column=1, sticky='w', padx=10, pady=5)
entry_nom_cote_1.config(width=15)

entry_cote_1 = tk.Entry(root)
entry_cote_1.grid(row=1, column=2, sticky='w', padx=10, pady=5)
entry_cote_1.config(width=10)

entry_upper_1 = tk.Entry(root)
entry_upper_1.grid(row=1, column=3, sticky='w', padx=10, pady=5)
entry_upper_1.config(width=10)

entry_lower_1 = tk.Entry(root)
entry_lower_1.grid(row=1, column=4, sticky='w', padx=10, pady=5)
entry_lower_1.config(width=10)

liste_sens = ["+", "-"]
var_sens = tk.StringVar(root)
option_menu_sens = tk.OptionMenu(root, var_sens, *liste_sens)
option_menu_sens.grid(row=1, column=5, sticky='ns', padx=10, pady=5)

entries.append([entry_cote_1, entry_upper_1, entry_lower_1, var_sens])


# Bouton pour ajouter une nouvelle ligne
bouton_ajout = tk.Button(root, text="Ajouter une ligne", command=ajouter_ligne)
bouton_ajout.grid(row=next_row, column=0, columnspan=5, pady=10)

# Choix de la méthode 
label_choix = tk.Label(root,text="Choissisez la méthode :")
label_choix.grid(row=0, column=6, sticky='ns', padx=10, pady=5)

var_methode = tk.IntVar()
radio_wc = tk.Radiobutton(root, text="WC", variable=var_methode, value=0)
radio_wc.grid(row = 1, column = 6, padx=10, pady=5)

# Bouton calcul
calculate_button = tk.Button(root, text="Calculer", command=calcule)
calculate_button.grid(row=2, column=6, padx=10, pady=5)


root.mainloop()