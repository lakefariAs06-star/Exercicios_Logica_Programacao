import tkinter as tk
from tkinter import ttk, messagebox

# Dados iniciais organizados por categoria
catalogo = {
    "Maquiagem": [
        {"nome": "Batom Matte Vermelho", "preco": "45.90"},
        {"nome": "Base Líquida", "preco": "59.90"}
    ],
    "Skincare": [
        {"nome": "Hidratante Facial CeraVe", "preco": "89.90"},
        {"nome": "Protetor Solar FPS 50", "preco": "65.00"}
    ],
    "Perfumaria": [
        {"nome": "Perfume La Vie Est Belle", "preco": "299.00"}
    ]
}

def atualizar_categorias():
    """Atualiza as opções do menu suspenso de categorias."""
    categorias = list(catalogo.keys())
    combo_categoria["values"] = categorias
    combo_add_categoria["values"] = categorias
    if categorias:
        combo_categoria.current(0)
        combo_add_categoria.current(0)
        atualizar_tabela()

def atualizar_tabela(event=None):
    """Exibe os produtos da categoria selecionada na tabela."""
    for row in tabela.get_children():
        tabela.delete(row)
    
    cat_selecionada = combo_categoria.get()
    if cat_selecionada in catalogo:
        for p in catalogo[cat_selecionada]:
            tabela.insert("", tk.END, values=(p["nome"], f"R$ {p['preco']}"))

def adicionar_produto():
    """Cadastra um novo produto na categoria escolhida."""
    cat = combo_add_categoria.get().strip()
    nome = entry_nome.get().strip()
    preco = entry_preco.get().strip()

    if not cat or not nome or not preco:
        messagebox.showwarning("Aviso", "Por favor, preencha todos os campos!")
        return

    if cat not in catalogo:
        catalogo[cat] = []

    catalogo[cat].append({"nome": nome, "preco": preco})
    
    atualizar_categorias()
    combo_categoria.set(cat)
    atualizar_tabela()

    entry_nome.delete(0, tk.END)
    entry_preco.delete(0, tk.END)
    messagebox.showinfo("Sucesso", f"'{nome}' cadastrado com sucesso na categoria '{cat}'!")

# --- Configuração da Janela Principal ---
root = tk.Tk()
root.title("Catálogo de Produtos de Beleza")
root.geometry("550x500")
root.configure(bg="#f5f5f5")

# Estilo visual
style = ttk.Style()
style.theme_use("clam")

# --- Seção 1: Visualização por Categoria ---
frame_view = ttk.LabelFrame(root, text=" Consultar Catálogo ", padding=10)
frame_view.pack(fill="x", padx=15, pady=10)

ttk.Label(frame_view, text="Selecione a Categoria:").pack(side="left", padx=5)
combo_categoria = ttk.Combobox(frame_view, state="readonly")
combo_categoria.pack(side="left", padx=5)
combo_categoria.bind("<<ComboboxSelected>>", atualizar_tabela)

# Tabela para listar os produtos
tabela = ttk.Treeview(root, columns=("Nome", "Preço"), show="headings", height=6)
tabela.heading("Nome", text="Nome do Produto")
tabela.heading("Preço", text="Preço")
tabela.column("Nome", width=300)
tabela.column("Preço", width=100, anchor="center")
tabela.pack(fill="x", padx=15, pady=5)

# --- Seção 2: Cadastro de Novo Produto ---
frame_add = ttk.LabelFrame(root, text=" Adicionar Novo Produto ", padding=10)
frame_add.pack(fill="x", padx=15, pady=10)

ttk.Label(frame_add, text="Categoria:").grid(row=0, column=0, sticky="w", pady=3)
combo_add_categoria = ttk.Combobox(frame_add)
combo_add_categoria.grid(row=0, column=1, sticky="ew", pady=3)  # Corrigido: sticky="ew" em vez de fill="x"

ttk.Label(frame_add, text="Nome do Produto:").grid(row=1, column=0, sticky="w", pady=3)
entry_nome = ttk.Entry(frame_add)
entry_nome.grid(row=1, column=1, sticky="ew", pady=3)  # Corrigido: sticky="ew"

ttk.Label(frame_add, text="Preço (R$):").grid(row=2, column=0, sticky="w", pady=3)
entry_preco = ttk.Entry(frame_add)
entry_preco.grid(row=2, column=1, sticky="ew", pady=3)  # Corrigido: sticky="ew"

frame_add.columnconfigure(1, weight=1)

btn_salvar = ttk.Button(frame_add, text="Cadastrar Produto", command=adicionar_produto)
btn_salvar.grid(row=3, column=0, columnspan=2, pady=10)

# Inicializar os dados na janela
atualizar_categorias()

# Executar a janela
root.mainloop()