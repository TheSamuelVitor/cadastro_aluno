from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview
from turtle import position

import psycopg2

# ------------------
#  CONEXÃO COM O BD
# ------------------
con = psycopg2.connect(
        host = "localhost",
        database = "cadastro",
        user = "postgres",
        password = "sysadmin"
    )

cur = con.cursor()

# ------------------
#    DEFINIÇÃO
# ------------------
app = Tk()
app.title('Cadastro de alunos')
app.resizable(height=False, width=False)
app.geometry('760x250+400+300')



# ------------------
#    FUNÇÕES
# ------------------
def apagar():
    
    entrada_nome.delete(0, END)
    entrada_rg.delete(0, END)
    entrada_cpf.delete(0, END)
    entrada_cep.delete(0, END)
    entrada_numero.delete(0, END)


def cadastrar():

    box_cadastrar = messagebox.askyesno('Cadastro', 'Tem certeza que deseja cadastrar? ')

    if box_cadastrar == TRUE:
        
        sql_cadastro = f"insert into tb_alunos(nome, rg, cpf, cep, numero_casa) values ('{entrada_nome.get()}', '{entrada_rg.get()}', '{entrada_cpf.get()}', '{entrada_cep.get()}', '{entrada_numero.get()}')"
        
        cur.execute(sql_cadastro)
        cur.execute('commit')

        messagebox.showinfo('Mensagem', 'Cadastro realizado com sucesso')

    apagar()


def janela():

    janela = Tk()
    janela.title('LISTA DE ALUNOS')

    tv = Treeview(janela, columns= ('ID', 'NOME', 'RG', 'CPF', 'CEP', 'N°'), show='headings')

    tv.column('ID', minwidth= 20, width= 50)
    tv.column('NOME', minwidth= 100, width=300)
    tv.column('RG', minwidth= 50, width= 100)
    tv.column('CPF', minwidth= 50, width= 100)
    tv.column('CEP', minwidth= 50, width= 100)
    tv.column('N°', minwidth= 50, width= 100)

    tv.heading('ID', text = 'ID')
    tv.heading('NOME', text = 'NOME')
    tv.heading('RG', text = 'RG')
    tv.heading('CPF', text = 'CPF')
    tv.heading('CEP', text = 'CEP')
    tv.heading('N°', text = 'N°')

    cur.execute('select * from tb_alunos')

    linhas = cur.fetchall()

    for id, nome, rg, cpf, cep, n in linhas:
        tv.insert('', 'end', values= (id, nome, rg, cpf, cep, n))

    tv.pack()

    janela.mainloop()


def limpar():

    box_limpar = messagebox.askyesno('Limpar', 'Tem certeza que deseja limpar a tabela? \nIsso apagará todos os dados')

    if box_limpar == TRUE:
        
        cur.execute('truncate table tb_alunos')

        messagebox.showinfo('Aviso', 'Tabela limpa com sucesso')
    
    apagar()


#------------------
#    COMPONENTES
#------------------
label_titulo = Label(text= 'ALUNOS', font= 'Verdana 18 bold')

label_nome = Label(app, text= 'Nome:', font= 'Verdana 12 bold', justify= LEFT)
label_rg = Label(app, text= 'RG:', font= 'Verdana 12 bold', justify= LEFT)
label_cpf = Label(app, text= 'CPF:', font= 'Verdana 12 bold', justify= LEFT)
label_cep = Label(app, text= 'CEP:', font= 'Verdana 12 bold', justify= LEFT)
label_numero = Label(app, text= 'N° da casa:', font= 'Verdana 12 bold', justify= LEFT)

entrada_nome = Entry(app, font= 'Verdana 12', width= 50, justify= LEFT)
entrada_rg = Entry(app, font= 'Verdana 12', justify= LEFT)
entrada_cpf = Entry(app, font= 'Verdana 12', justify= LEFT)
entrada_cep = Entry(app, font= 'Verdana 12', justify= LEFT)
entrada_numero = Entry(app, font= 'Verdana 12', justify= LEFT)

botao_cadastrar = Button(app, text= 'Cadastrar', font= 'Verdana 12', width= 10, command= lambda: cadastrar())
botao_listar = Button(app, text= 'Listar', font= 'Verdana 12', width= 10, command= lambda: janela())
botao_limpar = Button(app, text= 'Limpar', font= 'Verdana 12', width= 10, command= lambda: limpar())

#------------------
#    POSIÇÕES
#------------------
label_titulo.grid(row= 0, column= 0, columnspan= 3, padx= 5, pady=5)

label_nome.grid(row= 1, column= 0, padx= 5, pady=5)
label_rg.grid(row= 2, column= 0, padx= 5, pady=5)
label_cpf.grid(row= 3, column= 0, padx= 5, pady=5)
label_cep.grid(row= 4, column= 0, padx= 5, pady=5)
label_numero.grid(row= 5, column= 0, padx= 5, pady=5)

entrada_nome.grid(row= 1, column= 1, padx= 5, pady=5)
entrada_rg.grid(row= 2, column= 1, padx= 5, pady=5)
entrada_cpf.grid(row= 3, column= 1, padx= 5, pady=5)
entrada_cep.grid(row= 4, column= 1, padx= 5, pady=5)
entrada_numero.grid(row= 5, column= 1, padx= 5, pady=5)

botao_cadastrar.grid(row= 1, column= 2, padx= 5, pady=5)
botao_listar.grid(row= 2, column= 2, padx= 5, pady=5)
botao_limpar.grid(row= 3, column= 2, padx= 5, pady=5)


app.mainloop()