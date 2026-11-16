import tkinter as tk

# ----- CORES DO SPOTIFY ------
VERDE = "#1DB954"
PRETO = "#121212"
CINZA = "#282828"

# ===== JANELA PRINCIPAL ======
janela = tk.Tk()
janela.title("Spotify")
janela.geometry("350x450")
janela.config(bg=PRETO)

# ==== DADOS =====
musicas = ["Ompaa Lompaa", "Kia", "Gin com Suco de Laranja", "Espero que vocês Entendam"]
tocando = False

# ============= FUNÇÕES =============
def entrar():
    nome = entrada_nome.get()
    if nome == "":
        nome = "visitante"
    label_ola.config(text="Olá, " + nome + "!")
    tela1.pack_forget()
    tela2.pack(fill="both", expand=True)

def sair():
    tela2.pack_forget()
    tela1.pack(fill="both", expand=True)

def tocar_pausar():
    global tocando
    tocando = not tocando
    if tocando:
        botao_play.config(text="⏸ Pausar")
    else:
        botao_play.config(text="▶ Tocar")

def escolher_musica(evento):
    global tocando
    if lista.curselection():  # Corrigido: era curseelection()
        nome = lista.get(lista.curselection()[0])
        label_tocando.config(text="🎶 " + nome)
        tocando = True
        botao_play.config(text="⏸ Pausar")

# ============ TELA 1 LOGIN =================
tela1 = tk.Frame(janela, bg=PRETO)
tk.Label(tela1, text="Spotify", font=("Arial", 32, "bold"), bg=PRETO, fg=VERDE).pack(pady=40)
tk.Label(tela1, text="Digite seu nome:", bg=PRETO, fg="white").pack()

entrada_nome = tk.Entry(tela1, font=("Arial", 14), bg=CINZA, fg="white", insertbackground="white")
entrada_nome.pack(pady=10)

tk.Button(tela1, text="Entrar", font=("Arial", 12, "bold"), bg=VERDE, fg="black",
          width=15, command=entrar).pack(pady=20)

# ======== TELA 2 PLAYER ========
tela2 = tk.Frame(janela, bg=PRETO)

label_ola = tk.Label(tela2, text="", font=("Arial", 16, "bold"), bg=PRETO, fg="white")
label_ola.pack(pady=15)

lista = tk.Listbox(tela2, bg=CINZA, fg="white", font=("Arial", 11),
                   selectbackground=VERDE, height=6, width=30)
for musica in musicas:
    lista.insert(tk.END, musica)
lista.pack(pady=10)
lista.bind("<<ListboxSelect>>", escolher_musica)

label_tocando = tk.Label(tela2, text="Escolha uma música", bg=PRETO, fg=VERDE)
label_tocando.pack(pady=10)

# Corrigido: era commad=tocar_pausar
botao_play = tk.Button(tela2, text="▶ Tocar", bg=VERDE, width=15, command=tocar_pausar)
botao_play.pack(pady=5)

tk.Button(tela2, text="Sair", bg=CINZA, fg="white", width=15, command=sair).pack(pady=5)

# ======= INICIA O PROGRAMA ===========
tela1.pack(fill="both", expand=True)
janela.mainloop()