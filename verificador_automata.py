from ast import Raise
from ensurepip import version
from re import A
from select import select
import tkinter as tk
from automata.fa.dfa import DFA
import psycopg2

def nick_gui():
    
    def obtener_nick():
        print(nick.get())
        print(base.get())
        dfa = DFA(
            allow_partial=True,
            states={'q0', 'q1', 'q2','q3','q4','q5','q6','q7','q8','q9','q10','q11', 'q12','q13','q14','q15','q16','q17','q18','q19','q20','q21', 'q22','q23','q24','q25','q26','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36','q37','q38','q39','q40','q41','q42','q43','q44','q45','q46','q47','q48','q49','q50','q51','q52','q53','q54','q55','q56','q57','q58','q59','q60','q61','q62','q63','q64','q65','q66','q67','q68','q69','q70','q71','q72'},
            input_symbols={';','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','_',' ','.','(',')',','},
            transitions={
                'q0':{'c': 'q1'},
                'q1':{'r': 'q2'},
                'q2':{'e': 'q3'},
                'q3':{'a': 'q4'},
                'q4':{'t': 'q5'},
                'q5':{'e':'q6'},
                'q6':{' ':'q7'},
                'q7':{'t':'q8'},
                'q8':{'a':'q9'},
                'q9':{'b':'q10'},
                'q10':{'l':'q11'},
                'q11':{'e':'q12'},
                'q12':{' ':'q13'},
                'q13':{'(':'q14','.':'q13','_': 'q13','1': 'q13','2': 'q13','3': 'q13','4': 'q13','5': 'q13','6': 'q13','7': 'q13','8': 'q13','9': 'q13','0': 'q13', 'a': 'q13','b': 'q13','c': 'q13','d': 'q13','e': 'q13','f': 'q13','g': 'q13','h': 'q13','i': 'q13','j': 'q13','k': 'q13','l': 'q13','m': 'q13','n': 'q13','ñ': 'q13','o': 'q13','p': 'q13','q': 'q13','r': 'q13','s': 'q13','t': 'q13','u': 'q13','v': 'q13','w': 'q13','x': 'q13','y': 'q13','z': 'q13'},
                'q14':{' ':'q15','.':'q14','_': 'q14','1': 'q14','2': 'q14','3': 'q14','4': 'q14','5': 'q14','6': 'q14','7': 'q14','8': 'q14','9': 'q14','0': 'q14', 'a': 'q14','b': 'q14','c': 'q14','d': 'q14','e': 'q14','f': 'q14','g': 'q14','h': 'q14','i': 'q14','j': 'q14','k': 'q14','l': 'q14','m': 'q14','n': 'q14','ñ': 'q14','o': 'q14','p': 'q14','q': 'q14','r': 'q14','s': 'q14','t': 'q14','u': 'q14','v': 'q14','w': 'q14','x': 'q14','y': 'q14','z': 'q14'},
                'q15':{'i':'q16','c':'q23','b':'q39','d':'q46','m':'q50','r':'q55'},
                'q16':{'n':'q17'},
                'q17':{'t':'q18'},
                'q18':{'e':'q19'},
                'q19':{'g':'q20'},
                'q20':{'e':'q21'},
                'q21':{'r':'q61'},
                'q22':{' ':'q61'},
                'q23':{'h':'q24'},
                'q24':{'a':'q25'},
                'q25':{'r':'q26'},
                'q26':{'a':'q27'},
                'q27':{'c':'q28'},
                'q28':{'t':'q29'},
                'q29':{'e':'q30'},
                'q30':{'r':'q31'},
                'q31':{' ':'q32'},
                'q32':{'v':'q33'},
                'q33':{'a':'q34'},
                'q34':{'r':'q35'},
                'q35':{'y':'q36'},
                'q36':{'i':'q37'},
                'q37':{'n':'q38'},
                'q38':{'g':'q59'},
                'q39':{'o':'q40'},
                'q40':{'o':'q41'},
                'q41':{'l':'q42'},
                'q42':{'e':'q43'},
                'q43':{'a':'q44'},
                'q44':{'n':'q61'},
                'q45':{' ':'q61'},
                'q46':{'a':'q47'},
                'q47':{'t':'q48'},
                'q48':{'e':'q49'},
                'q49':{' ':'q61'},
                'q50':{'o':'q51'},
                'q51':{'n':'q52'},
                'q52':{'e':'q53'},
                'q53':{'y':'q61'},
                'q54':{' ':'q61'},
                'q55':{'e':'q56'},
                'q56':{'a':'q57'},
                'q57':{'l':'q61'},
                'q58':{' ':'q61'},
                'q59':{'(':'q60'},
                'q60':{')':'q61','1':'q60','2':'q60','3':'q60','4':'q60','5':'q60','6':'q60','7':'q60','8':'q60','9':'q60','0':'q60'},
                'q61':{' ':'q62',')':'q71'},
                'q62':{'n':'q63'},
                'q63':{'o':'q64'},
                'q64':{'t':'q65'},
                'q65':{' ':'q66'},
                'q66':{'n':'q67'},
                'q67':{'u':'q68'},
                'q68':{'l':'q69'},
                'q69':{'l':'q70'},
                'q70':{')':'q71',',':'q14'},
                'q71':{';':'q72'},
                'q72':{' ':'q72'}
                
            },
            initial_state='q0',
            final_states={'q72'}
        )
        if dfa.accepts_input(nick.get()):
            con = psycopg2.connect(database=base.get(), user="postgres", password="batalla", host="localhost", port="5432")
            con.autocommit = True
            cursor=con.cursor()
            cursor.execute(nick.get())
            labelaceptado = tk.Label(frame, text="Aceptada añadiendo tabla a la base de datos "+base.get())
            labelaceptado.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="n")
        else:
            print('rejected')
            labelrechazado = tk.Label(frame, text="sentencia rechazada")
            labelrechazado.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="n")

    root = tk.Tk()
    root.title("Verificador")

    nick = tk.StringVar()
    base = tk.StringVar()
    
    frame = tk.Frame(root)
    frame.grid(row=1, column=0, padx=5, pady=5)
    
    base_nombre = tk.Entry(frame, width=25,textvariable=base)
    base_nombre.grid(row=3, column=0, sticky="w", padx=10, pady=10)

    label1 = tk.Label(frame, text="inserte la sentencia create table siguiendo la siguiente sintaxis:")
    label1.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="n")
    
    label13 = tk.Label(frame, text="nombre de la base de datos:")
    label13.grid(row=2, column=0, columnspan=1, padx=5, pady=5, sticky="n")
    
    label2 = tk.Label(frame, text="create table [nombre]([nombre columna] [tipo de dato]([tamaño]) [restriccion not null]);)")
    label2.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="n")

    insert_nick = tk.Entry(frame, width=150, textvariable=nick)
    insert_nick.grid(row=3, column=1, sticky="w", padx=10, pady=10)

    boton_nick = tk.Button(frame, text="Verificar", command=obtener_nick)
    boton_nick.grid(row=3, column=2, sticky="e", padx=5, pady=5)
    
    label23 = tk.Label(frame, text="Tipos de Datos:\n-integer\n-character varying([longitud])\n-boolean\n-date\n-money\n-real")
    label23.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="n")

    root.mainloop()

if __name__ == "__main__":
    nick_gui()