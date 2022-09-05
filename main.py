from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from tkinter import *


conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='marcelo',
    database='db_petshop',
)
cursor = conexao.cursor()

# CRUD

# CREATE


# nome = "blade"
# idade = 8
# dt_cadastro = "14/02/2014"
# dt_adocao = ""
#
#
# comando = f'INSERT INTO tbDados (nome, idade, dt_cadastro, dt_adocao) VALUES ("{nome}", {idade}, "{dt_cadastro}", "{dt_adocao}")'
#
# cursor.execute(comando)
#
# conexao.commit() # edita o banco de dados



# READ
def cadastrados():
    tv.delete(*tv.get_children())
    comando = f'SELECT * FROM tbDados'

    cursor.execute(comando)

    resultado = cursor.fetchall() # ler o banco de dados
    for i in resultado:
        tv.insert("","end", values=i)


#Adotados READ

def adotados():
    tv.delete(*tv.get_children())
    comando = f'SELECT * FROM tbDados WHERE dt_adocao != ""'

    cursor.execute(comando)

    resultado = cursor.fetchall() # ler o banco de dados

    for i in resultado:
        tv.insert("","end", values=i)

# UPDATE

# nome_produto = "todynho"

# valor = 6

# comando = f'UPDATE tbDados SET nome = "{nome}" WHERE nome = "{nome}"'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados



# DELETE

# nome_produto = "todynho"

# comando = f'DELETE FROM tbDados WHERE nome = "{nome}"'

# cursor.execute(comando)

# conexao.commit() # edita o banco de dados


janela = Tk()

janela.title("PETSHOP")
janela.geometry("700x500")

quadroGrid=LabelFrame(janela,text="Sistema", bg="#5C5B5B",fg = "#FFFFFF", font=("Arial", 13))
quadroGrid.pack(fill="both", expand="yes",padx=10,pady=10)

tv= ttk.Treeview(quadroGrid,columns=('codigo','nome', 'idade','dt_cadastro','dt_adocao'), show='headings')
tv.column('codigo', minwidth=0,width=53)
tv.column('nome', minwidth=0,width=150)
tv.column('idade', minwidth=0,width=50)
tv.column('dt_cadastro', minwidth=0,width=100)
tv.column('dt_adocao', minwidth=0,width=100)
tv.heading('codigo',text='CODIGO')
tv.heading('nome',text='NOME')
tv.heading('idade',text='IDADE')
tv.heading('dt_cadastro',text='DT_CADASTRO')
tv.heading('dt_adocao',text='ADOÇÃO')
tv.pack()
cadastrados()

texto = Label(quadroGrid, text="Escolha um botão para ver os animais adotados ou cadastrados.", bg = "#5C5B5B",fg = "#FFFFFF", font=("Arial", 13))
texto.pack(side="top",pady=10)

botao = Button(quadroGrid, text="Animais cadastrados", bg = "#939292",fg = "#FFFFFF",font=("Arial", 10),command=cadastrados)
botao.pack(side="top", padx=10, pady=10)

botao = Button(quadroGrid, text="Animais Adotados", bg = "#939292",fg = "#FFFFFF",font=("Arial", 10) ,command=adotados)
botao.pack(side="top", padx=10)

janela.mainloop()

cursor.close()
conexao.close()