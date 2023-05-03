from tkinter import messagebox
import customtkinter
import tkinter as tk
from tkinter import ttk
from functools import partial
from ttkthemes import ThemedTk, ThemedStyle
from connect import mycursor, mydb
from datetime import datetime
from tkinter import *

mycursor.execute("CREATE TABLE IF NOT EXISTS login (username VARCHAR(255), password VARCHAR(255), email VARCHAR(255))")

# Crie a interface de login
def login():
    # Obtenha as informações de login fornecidas pelo usuário
    username = entry_username.get()
    password = entry_password.get()

    # Verifique se as informações de login estão corretas
    mycursor.execute("SELECT * FROM login WHERE username = %s AND password = %s", (username, password))
    result = mycursor.fetchone()
    if result:
        # Redirecione o usuário para a página inicial
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        tree = menu_informacoes()
    else:
        # Exiba uma mensagem de erro e solicite que o usuário tente novamente
        print("Nome de usuário ou senha incorretos. Tente novamente.")


def logout():
    info_window.destroy()
    root.deiconify()

def atualizar_treeview(tree):

    for i in tree.get_children():
        tree.delete(i)

    mycursor.execute("SELECT * FROM vendas_produtos")
    vendas = mycursor.fetchall()
    for venda in vendas:
        data_venda = venda[3].strftime('%d/%m/%Y')
        tree.insert('', 'end', values=(venda[0], venda[1], venda[2], data_venda))



def adicionar_venda(tree):
    def salvar_venda():
        nome_produto = entry_nome_produto.get()
        valor = entry_valor.get()

        if nome_produto and valor:
            try:
                mycursor.execute("INSERT INTO vendas_produtos (nome_produto, valor) VALUES (%s, %s)", (nome_produto, float(valor)))
                mydb.commit()
                messagebox.showinfo("Sucesso", "Venda adicionada com sucesso!")
                add_venda_window.destroy()
                atualizar_treeview(tree)
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao adicionar a venda: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")

    add_venda_window = tk.Toplevel()
    add_venda_window.title("Adicionar Venda")

    label_nome_produto = ttk.Label(add_venda_window, text="Nome do Produto")
    label_nome_produto.pack()
    entry_nome_produto = ttk.Entry(add_venda_window)
    entry_nome_produto.pack()

    label_valor = ttk.Label(add_venda_window, text="Valor")
    label_valor.pack()
    entry_valor = ttk.Entry(add_venda_window)
    entry_valor.pack()

    button_salvar = tk.Button(add_venda_window, text="Salvar", command=salvar_venda)
    button_salvar.pack()

def atualizar_venda(tree):
    def salvar_atualizacao():
        id_venda = entry_id_venda.get()
        nome_produto = entry_nome_produto.get()
        valor = entry_valor.get()

        if id_venda and nome_produto and valor:
            try:
                mycursor.execute("UPDATE vendas_produtos SET nome_produto=%s, valor=%s WHERE id=%s", (nome_produto, float(valor), int(id_venda)))
                mydb.commit()
                messagebox.showinfo("Sucesso", "Venda atualizada com sucesso!")
                update_venda_window.destroy()
                atualizar_treeview(tree)
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao atualizar a venda: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")


    update_venda_window = tk.Toplevel()
    update_venda_window.title("Atualizar Venda")

    label_id_venda = ttk.Label(update_venda_window, text="ID da Venda")
    label_id_venda.pack()
    entry_id_venda = tk.Entry(update_venda_window)
    entry_id_venda.pack()

    label_nome_produto = ttk.Label(update_venda_window, text="Nome do Produto")
    label_nome_produto.pack()
    entry_nome_produto = tk.Entry(update_venda_window)
    entry_nome_produto.pack()

    label_valor = ttk.Label(update_venda_window, text="Valor")
    label_valor.pack()
    entry_valor = tk.Entry(update_venda_window)
    entry_valor.pack()

    button_salvar = ttk.Button(update_venda_window, text="Salvar", command=lambda: salvar_atualizacao())
    button_salvar.pack()

def excluir_venda(tree):
    def confirmar_exclusao():
        id_venda = entry_id_venda.get()

        if id_venda:
            try:
                mycursor.execute("DELETE FROM vendas_produtos WHERE id=%s", (int(id_venda),))
                mydb.commit()
                messagebox.showinfo("Sucesso", "Venda excluída com sucesso!")
                delete_venda_window.destroy()
                atualizar_treeview(tree)
            except Exception as e:
                messagebox.showerror("Erro", f"Ocorreu um erro ao excluir a venda: {e}")
        else:
            messagebox.showerror("Erro", "Por favor, preencha o campo do ID da venda.")

    delete_venda_window = tk.Toplevel()
    delete_venda_window.title("Excluir Venda")

    label_id_venda = ttk.Label(delete_venda_window, text="ID da Venda")
    label_id_venda.pack()
    entry_id_venda = ttk.Entry(delete_venda_window)
    entry_id_venda.pack()

    button_confirmar = tk.Button(delete_venda_window, text="Confirmar", command=confirmar_exclusao)
    button_confirmar.pack()



def menu_informacoes():
    global info_window


    root.withdraw()

    info_window = tk.Toplevel(root)

    style = ThemedStyle(info_window)
    style.set_theme("equilux")

    #info_window = ttk.Toplevel()

    info_window.title("Menu de Informações")

    # Crie o widget Notebook (abas)

    notebook = ttk.Notebook(info_window)
    notebook.pack(expand=True, fill=tk.BOTH)

   
    vendas_tab = ttk.Frame(notebook)
    notebook.add(vendas_tab, text="Vendas")

    label_vendas = ttk.Label(vendas_tab, text="Informações de vendas", font=("Helvetica", 16))
    label_vendas.pack(pady=20)
    

    # Crie e configure o Treeview
    colunas = ('#1', '#2', '#3', '#4')
    tree = ttk.Treeview(vendas_tab, columns=colunas, show='headings')
    tree.heading('#1', text='ID da Venda')
    tree.heading('#2', text='Nome do Produto')
    tree.heading('#3', text='Quantidade')
    tree.heading('#4', text='Data venda')


    # Adicione aqui o código para preencher o Treeview com os dados das vendas

    tree.pack(pady=(10, 0))

    # ...

    # Crie os botões CRUD
    frame_botoes = ttk.Frame(vendas_tab)
    frame_botoes.pack(pady=10)

    btn_adicionar = ttk.Button(frame_botoes, text="Adicionar", command=partial(adicionar_venda, tree), width=10)
    btn_adicionar.grid(row=0, column=0, padx=10)

    btn_atualizar = ttk.Button(frame_botoes, text="Atualizar", command=partial(atualizar_venda, tree), width=10)
    btn_atualizar.grid(row=0, column=1, padx=10)

    btn_excluir = ttk.Button(frame_botoes, text="Excluir", command=partial(excluir_venda, tree), width=10)
    btn_excluir.grid(row=0, column=2, padx=10)

    # ...

    btn_logout = ttk.Button(info_window, text="Logout", command=logout, width=10)
    btn_logout.pack(pady=(20, 0))


    # Adicione aqui os widgets para exibir e gerenciar informações de estoque


    atualizar_treeview(tree)

    return tree  # Adicione esta linha para retornar a variável 'tree'


# Crie a interface gráfica de usuário

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("550x234")


root.title("Login")

label_username = customtkinter.CTkLabel(root, text="Nome de usuário")
label_username.pack()
entry_username = customtkinter.CTkEntry(root)
entry_username.pack()

label_password = customtkinter.CTkLabel(root, text="Senha")
label_password.pack()
entry_password = customtkinter.CTkEntry(root, show="*")
entry_password.pack()

button_login = customtkinter.CTkButton(root, text="Entrar", command=login)
button_login.pack()

# ...

def on_enter_key(event):
    login()

root.bind('<Return>', on_enter_key)

root.mainloop()