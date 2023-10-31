import csv
import customtkinter as ctk
from login import *
from tkinter import messagebox
from __main__ import *

class AppLogin(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.config_janela_principal()
        self.janela_principal()

    def config_janela_principal(self):
        self.geometry("1000x700")
        self.title("Sistema de Cadastros")
        self.resizable(True,True)

    def janela_principal(self):
        #Frame
        self.frame_login = ctk.CTkFrame(self)
        self.frame_login.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Texto
        self.title = ctk.CTkLabel(self.frame_login, text="Login de Sistema", font=("Century Gothic", 20))
        self.title.grid(row=0, column=0, padx=10, pady=10)
        #Widget login - Usuário
        self.usuario_login = ctk.CTkEntry(self.frame_login, width=325, placeholder_text="Nome de Usuário", font=("Century Gothic", 16), corner_radius=0)
        self.usuario_login.grid(row=1, column=0, padx=10, pady=10)
        #Widget login - Senha
        self.senha_login = ctk.CTkEntry(self.frame_login, width=325, placeholder_text="Senha", font=("Century Gothic", 16), corner_radius=0, show="*")
        self.senha_login.grid(row=2, column=0, padx=10, pady=10)
        #Mostrar senha
        self.ver_senha = ctk.CTkCheckBox(self.frame_login, text="Clique para mostrar a senha", font=("Century Gothic", 13), command=self.mostrar_senhal)
        self.ver_senha.grid(row=3, column=0, padx=10, pady=10)
        #Botão login
        self.btn_login = ctk.CTkButton(self.frame_login, width=300, text="LOGIN", font=("Century Gothic", 16), corner_radius=0, command=self.entrar)
        self.btn_login.grid(row=4, column=0, padx=10, pady=10)
        #Botão cadastro
        self.btn_cadastro = ctk.CTkButton(self.frame_login, width=300, text="CADASTRE-SE", font=("Century Gothic", 16), corner_radius=0, command=self.janela_cadastro)
        self.btn_cadastro.grid(row=5, column=0, padx=10, pady=10)

    def mostrar_senhal(self):
        if self.senha_login.cget('show') == '*':
            self.senha_login.configure(show='')
        else:
            self.senha_login.configure(show='*')

    def janela_cadastro(self):
        self.frame_login.place_forget()
        #Frame
        self.frame_cadastro = ctk.CTkFrame(self)
        self.frame_cadastro.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Título
        self.title = ctk.CTkLabel(self.frame_cadastro, text="Cadastro de Sistema", font=("Century Gothic", 20))
        self.title.grid(row=0, column=0, padx=10, pady=10)
        #Widget login - Usuário
        self.usuario_cadastro = ctk.CTkEntry(self.frame_cadastro, width=325, placeholder_text="Nome de Usuário", font=("Century Gothic", 16), corner_radius=0)
        self.usuario_cadastro.grid(row=1, column=0, padx=10, pady=10)
        #Widget cadastro - Senhas
        self.senha_cadastro = ctk.CTkEntry(self.frame_cadastro, width=325, placeholder_text="Senha", font=("Century Gothic", 16), corner_radius=0, show="*")
        self.senha_cadastro.grid(row=2, column=0, padx=10, pady=10)
        self.senha_cadastro2 = ctk.CTkEntry(self.frame_cadastro, width=325, placeholder_text="Repita a senha", font=("Century Gothic", 16), corner_radius=0, show="*")
        self.senha_cadastro2.grid(row=3, column=0, padx=10, pady=10)
        #Mostrar senha
        self.ver_senha = ctk.CTkCheckBox(self.frame_cadastro, text="Clique para mostrar a senha", font=("Century Gothic", 13), command=self.mostrar_senhac)
        self.ver_senha.grid(row=4, column=0, padx=10, pady=10)
        #Botão cadastro
        self.btn_cadastrar = ctk.CTkButton(self.frame_cadastro, width=300, text="CADASTRAR", font=("Century Gothic", 16), corner_radius=0, command=self.registrar)
        self.btn_cadastrar.grid(row=5, column=0, padx=10, pady=10)
        #Botão voltar
        self.btn_voltar = ctk.CTkButton(self.frame_cadastro, width=300, text="VOLTAR", font=("Century Gothic", 16), corner_radius=0, command=self.mudar_janela)
        self.btn_voltar.grid(row=6, column=0, padx=10, pady=10)

    def mostrar_senhac(self):
        if self.senha_cadastro.cget('show') == '*' or self.senha_cadastro2.cget('show') == '*':
            self.senha_cadastro.configure(show='')
            self.senha_cadastro2.configure(show='')
        else:
            self.senha_cadastro.configure(show='*')
            self.senha_cadastro2.configure(show='*')

    def mudar_janela(self):
        self.frame_cadastro.destroy()
        self.janela_principal()
            
    def registrar(self):
        with open ("login.csv", mode="r") as f:
            leitor = csv.DictReader(f, delimiter=";")
            nome = self.usuario_cadastro.get()
            senha = self.senha_cadastro.get()
            senha2 = self.senha_cadastro2.get()

            if nome == "" or senha == "" or senha2 == "":
                messagebox.showerror("Erro", "Por favor preencher todos os campos.")
            elif any(linha['Nome'] == nome for linha in leitor):
                messagebox.showerror("Erro", "Usuário já cadastrado no sistema.")
            else:
                with open("login.csv", mode="a", newline="") as f:
                    escrita = csv.writer(f,delimiter=";")
                    if senha == senha2:
                        escrita.writerow([nome,senha,"1"])
                        messagebox.showinfo("Sucesso", "Usuário cadastrado.")
                        self.limpa_cadastro()
                    else:
                        messagebox.showerror("Erro", "Senhas não correspondem.")

    def entrar(self):
        with open("login.csv", mode="r") as f:
            leitor = csv.reader(f, delimiter=";")
            nome = self.usuario_login.get()
            senha = self.senha_login.get()
            var = 0

            if nome == "" or senha == "":
                messagebox.showerror("Erro", "Preencha todos os campos.")
            else:
                for linha in leitor:
                    if linha == [nome, senha,"0"]:
                        messagebox.showinfo("Successo","Logado como Administrador.")
                        var = 0
                        self.limpa_login()
                        self.mudar_admin()
                        break
                    elif linha == [nome, senha,"1"]:
                        messagebox.showinfo("Successo","Logado como Usuário.")
                        var = 0
                        self.limpa_login()
                        self.mudar_usuario()
                        break
                    else:
                        var =+ 1
                if var != 0:
                    messagebox.showerror("Erro", "Usuário ou senha incorreta.")
                    var = 0
    


    def limpa_cadastro(self):
        self.usuario_cadastro.delete(0, END)
        self.senha_cadastro.delete(0, END)
        self.senha_cadastro2.delete(0, END)

    def limpa_login(self):
        self.usuario_login.delete(0, END)
        self.senha_login.delete(0, END)

    def mudar_admin(self):
        self.frame_login.destroy()
        self.janela_admin()

    def janela_admin(self):
        #Frame
        self.frame_admin = ctk.CTkFrame(self)
        self.frame_admin.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Título
        self.title = ctk.CTkLabel(self.frame_admin, text="Logado em nível de Administrador", font=("Century Gothic", 20))
        self.title.grid(row=0, column=0, padx=10, pady=10)

    def mudar_usuario(self):
        self.frame_login.destroy()
        self.janela_usuario()

    def janela_usuario(self):
        #Frame
        self.frame_usuario = ctk.CTkFrame(self)
        self.frame_usuario.place(relx=0.5, rely=0.5, anchor=CENTER)
        #Título
        self.title = ctk.CTkLabel(self.frame_usuario, text="Logado em nível de Usuário", font=("Century Gothic", 20))
        self.title.grid(row=0, column=0, padx=10, pady=10)
