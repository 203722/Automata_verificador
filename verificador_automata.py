from ensurepip import version
from select import select
import tkinter as tk
from automata.fa.dfa import DFA
import psycopg2

def nick_gui():

    def obtener_nick():
        print(nick.get())
        dfa = DFA(
            allow_partial=True,
            states={'q0', 'q1', 'q2','q3','q4','q5','q6','q7','q8','q9','q10','q11', 'q12','q13','q14','q15','q16','q17','q18','q19','q20','q21', 'q22','q23','q24','q25','q26','q26','q27','q28','q29','q30','q31','q32','q33','q34','q35','q36','q37','q38','q39','q40','q41','q42','q43','q44','q45','q46','q47','q48','q49','q50','q51','q52','q53','q54','q55','q56','q57','q58','q59','q60','q61','q62','q63','q64','q65','q66','q67','q68','q69','q70','q71','q72','q73','q74','q75','q76','q77','q78','q79','q80','q81','q82'},
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
                'q14':{' ':'q23',' ':'q41',' ':'q49',' ':'q54',' ':'q60',' ':'q15','.':'q14','_': 'q14','1': 'q14','2': 'q14','3': 'q14','4': 'q14','5': 'q14','6': 'q14','7': 'q14','8': 'q14','9': 'q14','0': 'q14', 'a': 'q14','b': 'q14','c': 'q14','d': 'q14','e': 'q14','f': 'q14','g': 'q14','h': 'q14','i': 'q14','j': 'q14','k': 'q14','l': 'q14','m': 'q14','n': 'q14','ñ': 'q14','o': 'q14','p': 'q14','q': 'q14','r': 'q14','s': 'q14','t': 'q14','u': 'q14','v': 'q14','w': 'q14','x': 'q14','y': 'q14','z': 'q14'},
                'q15':{'i':'q16'},
                'q16':{'n':'q17'},
                'q17':{'t':'q18'},
                'q18':{'e':'q19'},
                'q19':{'g':'q20'},
                'q20':{'e':'q21'},
                'q21':{'r':'q22'},
                'q22':{' ':'q68'},
                'q23':{'c':'q24'},
                'q24':{'h':'q25'},
                'q25':{'a':'q26'},
                'q26':{'r':'q27'},
                'q27':{'a':'q28'},
                'q28':{'c':'q29'},
                'q29':{'t':'q30'},
                'q30':{'e':'q31'},
                'q31':{'r':'q32'},
                'q32':{' ':'q33'},
                'q33':{'v':'q34'},
                'q34':{'a':'q35'},
                'q35':{'r':'q36'},
                'q36':{'y':'q37'},
                'q37':{'i':'q38'},
                'q38':{'n':'q39'},
                'q39':{'g':'q65'},
                #'q40':{'':'q15'},
                'q41':{'b':'q42'},
                'q42':{'o':'q43'},
                'q43':{'o':'q44'},
                'q44':{'l':'q45'},
                'q45':{'e':'q46'},
                'q46':{'a':'q47'},
                'q47':{'n':'q48'},
                'q48':{' ':'q68'},
                'q49':{'d':'q50'},
                'q50':{'a':'q51'},
                'q51':{'t':'q52'},
                'q52':{'e':'q53'},
                'q53':{' ':'q68'},
                'q54':{'m':'q55'},
                'q55':{'o':'q56'},
                'q56':{'n':'q57'},
                'q57':{'e':'q58'},
                'q58':{'y':'q59'},
                'q59':{' ':'q68'},
                'q60':{'r':'q61'},
                'q61':{'e':'q62'},
                'q62':{'a':'q63'},
                'q63':{'l':'q64'},
                'q64':{' ':'q68'},
                'q65':{'(':'q66'},
                'q66':{')':'q67','1':'q66','2':'q66','3':'q66','4':'q66','5':'q66','6':'q66','7':'q66','8':'q66','9':'q66','0':'q66'},
                'q67':{' ':'q68'},
                'q68':{'n':'q69'},
                'q69':{'o':'q70'},
                'q70':{'t':'q71'},
                'q71':{' ':'q72'},
                'q72':{'n':'q73'},
                'q73':{'u':'q74'},
                'q74':{'l':'q75'},
                'q75':{'l':'q80'},
                'q76':{'n':'q77'},
                'q77':{'u':'q78'},
                'q78':{'l':'q79'},
                'q79':{'l':'q80'},
                'q80':{')':'q81',',':'q14'},
                'q81':{';':'q82'},
                'q82':{' ':'q82'}
                
            },
            initial_state='q0',
            final_states={'q82'}
        )
        if dfa.accepts_input(nick.get()):
            con = psycopg2.connect(database="pruebas", user="postgres", password="batalla", host="localhost", port="5432")
            con.autocommit = True
            cursor=con.cursor()
            cursor.execute(nick.get())
            labelaceptado = tk.Label(frame, text="Aceptada añadiendo tabla a la base de datos pruebas")
            labelaceptado.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="n")
        else:
            print('rejected')
            labelrechazado = tk.Label(frame, text="sentencia rechazada")
            labelrechazado.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="n")

    root = tk.Tk()
    root.title("Verificador")

    nick = tk.StringVar()

    frame = tk.Frame(root)
    frame.grid(row=0, column=0, padx=5, pady=5)

    labeltexto = tk.Label(frame, text="inserte la sentencia create table siguiendo la siguiente sintaxis:")
    labeltexto.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="n")
    
    label2 = tk.Label(frame, text="create table [nombre]([nombre columna] [tipo de dato]([tamaño]) [restriccion not null]);)")
    label2.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="n")

    insert_nick = tk.Entry(frame, width=150, textvariable=nick)
    insert_nick.grid(row=2, column=0, sticky="w", padx=10, pady=10)

    boton_nick = tk.Button(frame, text="Verificar", command=obtener_nick)
    boton_nick.grid(row=2, column=1, sticky="e", padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    nick_gui()