'''
from PIL import Image

def aumentar_resolucao(caminho_entrada, caminho_saida, fator_escala):
    # Abre a imagem original
    img = Image.open(caminho_entrada)
    
    # Calcula o novo tamanho (ex: 2x maior, 3x maior)
    largura_nova = int(img.width * fator_escala)
    altura_nova = int(img.height * fator_escala)
    
    # Redimensiona usando o filtro LANCZOS (o melhor para aumento)
    img_alta_res = img.resize((largura_nova, altura_nova), Image.Resampling.LANCZOS)
    
    # Salva a imagem garantindo que o perfil seja mantido e qualidade máxima
    img_alta_res.save(caminho_saida, "JPEG", quality=100, subsampling=0)
    print(f"Sucesso! Imagem salva em: {caminho_saida}")

# Exemplo de uso: Aumentar em 2x (se a foto tem 2MP, vai para 4MP)
aumentar_resolucao("fotos\gatinho.jpg", "gatinho_high_res.jpg", 2)
'''
'''
import os
from PIL import Image

def aumentar_resolucao(caminho_entrada, caminho_saida, fator_escala):
    # Abre a imagem original
    img = Image.open(caminho_entrada)
    
    # Calcula o novo tamanho
    largura_nova = int(img.width * fator_escala)
    altura_nova = int(img.height * fator_escala)
    
    # Redimensiona usando LANCZOS
    img_alta_res = img.resize((largura_nova, altura_nova), Image.Resampling.LANCZOS)
    
    # Salva a imagem com qualidade máxima
    img_alta_res.save(caminho_saida, "JPEG", quality=100, subsampling=0)
    print(f"Sucesso! Imagem salva em: {caminho_saida}")

# Função para aplicar em todas as imagens de uma pasta
def aumentar_todas_imagens(pasta_entrada, pasta_saida, fator_escala):
    # Cria a pasta de saída se não existir
    os.makedirs(pasta_saida, exist_ok=True)
    
    # Percorre todos os arquivos da pasta
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.lower().endswith((".jpg", ".jpeg", ".png")):  # apenas imagens
            caminho_entrada = os.path.join(pasta_entrada, arquivo)
            caminho_saida = os.path.join(pasta_saida, f"highres_{arquivo}")
            
            aumentar_resolucao(caminho_entrada, caminho_saida, fator_escala)

# Exemplo de uso: aumentar todas as imagens da pasta "fotos" em 2x
aumentar_todas_imagens("fotos", "fotos_highres", 2)
'''
'''
import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from PIL import Image

def aumentar_resolucao(caminho_entrada, caminho_saida):
    fator_escala = 2  # escala fixa
    img = Image.open(caminho_entrada)
    largura_nova = int(img.width * fator_escala)
    altura_nova = int(img.height * fator_escala)
    img_alta_res = img.resize((largura_nova, altura_nova), Image.Resampling.LANCZOS)

    formato = img.format if img.format else "JPEG"
    img_alta_res.save(caminho_saida, formato, quality=100, subsampling=0)

def aumentar_todas_imagens(pasta_entrada, pasta_saida):
    os.makedirs(pasta_saida, exist_ok=True)
    for arquivo in os.listdir(pasta_entrada):
        if arquivo.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff")):
            caminho_entrada = os.path.join(pasta_entrada, arquivo)
            nome_base, ext = os.path.splitext(arquivo)
            caminho_saida = os.path.join(pasta_saida, f"{nome_base}_highres{ext}")
            try:
                aumentar_resolucao(caminho_entrada, caminho_saida)
            except Exception as e:
                print(f"Erro ao processar {arquivo}: {e}")

    messagebox.showinfo("Concluído", f"Imagens salvas em: {pasta_saida}")

# ---------------- INTERFACE GRÁFICA ----------------
def selecionar_pasta_entrada():
    pasta = filedialog.askdirectory(title="Selecione a pasta de entrada")
    if pasta:
        entrada_var.delete(0, "end")
        entrada_var.insert(0, pasta)

def selecionar_pasta_saida():
    pasta = filedialog.askdirectory(title="Selecione a pasta de saída")
    if pasta:
        saida_var.delete(0, "end")
        saida_var.insert(0, pasta)

def executar():
    pasta_entrada = entrada_var.get()
    pasta_saida = saida_var.get()

    if not pasta_entrada or not pasta_saida:
        messagebox.showerror("Erro", "Selecione as pastas de entrada e saída.")
        return

    aumentar_todas_imagens(pasta_entrada, pasta_saida)

    # 🔹 Limpar os campos após concluir
    entrada_var.delete(0, "end")
    saida_var.delete(0, "end")

# Criar janela principal
root = Tk()
root.title("Aumentar Resolução de Imagens (Escala 2x)")

Label(root, text="Pasta de entrada:").grid(row=0, column=0, padx=5, pady=5)
entrada_var = Entry(root, width=40)
entrada_var.grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Selecionar", command=selecionar_pasta_entrada).grid(row=0, column=2, padx=5, pady=5)

Label(root, text="Pasta de saída:").grid(row=1, column=0, padx=5, pady=5)
saida_var = Entry(root, width=40)
saida_var.grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Selecionar", command=selecionar_pasta_saida).grid(row=1, column=2, padx=5, pady=5)

Button(root, text="Executar", command=executar).grid(row=2, column=1, pady=10)

root.mainloop()
'''

import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from tkinter import ttk
from PIL import Image

def aumentar_resolucao(caminho_entrada, caminho_saida):
    fator_escala = 2  # escala fixa
    img = Image.open(caminho_entrada)
    largura_nova = int(img.width * fator_escala)
    altura_nova = int(img.height * fator_escala)
    img_alta_res = img.resize((largura_nova, altura_nova), Image.Resampling.LANCZOS)

    formato = img.format if img.format else "JPEG"
    img_alta_res.save(caminho_saida, formato, quality=100, subsampling=0)

def aumentar_todas_imagens(pasta_entrada, pasta_saida, progress_bar, percent_label):
    arquivos = [f for f in os.listdir(pasta_entrada) if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tiff"))]
    total = len(arquivos)

    if total == 0:
        messagebox.showwarning("Aviso", "Nenhuma imagem encontrada na pasta de entrada.")
        return

    os.makedirs(pasta_saida, exist_ok=True)

    for i, arquivo in enumerate(arquivos, start=1):
        caminho_entrada = os.path.join(pasta_entrada, arquivo)
        nome_base, ext = os.path.splitext(arquivo)
        caminho_saida = os.path.join(pasta_saida, f"{nome_base}_highres{ext}")
        try:
            aumentar_resolucao(caminho_entrada, caminho_saida)
        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")

        # Atualizar barra de progresso e porcentagem
        progresso = (i / total) * 100
        progress_bar["value"] = progresso
        percent_label.config(text=f"{progresso:.0f}%")
        root.update_idletasks()

    messagebox.showinfo("Concluído", f"Imagens salvas em: {pasta_saida}")

# ---------------- INTERFACE GRÁFICA ----------------
def selecionar_pasta_entrada():
    pasta = filedialog.askdirectory(title="Selecione a pasta de entrada")
    if pasta:
        entrada_var.delete(0, "end")
        entrada_var.insert(0, pasta)

def selecionar_pasta_saida():
    pasta = filedialog.askdirectory(title="Selecione a pasta de saída")
    if pasta:
        saida_var.delete(0, "end")
        saida_var.insert(0, pasta)

def executar():
    pasta_entrada = entrada_var.get()
    pasta_saida = saida_var.get()

    if not pasta_entrada or not pasta_saida:
        messagebox.showerror("Erro", "Selecione as pastas de entrada e saída.")
        return

    # Resetar barra e porcentagem antes de iniciar
    progress_bar["value"] = 0
    percent_label.config(text="0%")
    aumentar_todas_imagens(pasta_entrada, pasta_saida, progress_bar, percent_label)

    # 🔹 Limpar os campos após concluir
    entrada_var.delete(0, "end")
    saida_var.delete(0, "end")

# Criar janela principal
root = Tk()
root.title("Aumentar Resolução de Imagens (Escala 2x)")

Label(root, text="Pasta de entrada:").grid(row=0, column=0, padx=5, pady=5)
entrada_var = Entry(root, width=40)
entrada_var.grid(row=0, column=1, padx=5, pady=5)
Button(root, text="Selecionar", command=selecionar_pasta_entrada).grid(row=0, column=2, padx=5, pady=5)

Label(root, text="Pasta de saída:").grid(row=1, column=0, padx=5, pady=5)
saida_var = Entry(root, width=40)
saida_var.grid(row=1, column=1, padx=5, pady=5)
Button(root, text="Selecionar", command=selecionar_pasta_saida).grid(row=1, column=2, padx=5, pady=5)

Button(root, text="Executar", command=executar).grid(row=2, column=1, pady=10)

progress_bar = ttk.Progressbar(root, length=250, mode="determinate")
progress_bar.grid(row=3, column=1, pady=10, sticky="e")

percent_label = Label(root, text="0%")
percent_label.grid(row=3, column=2, padx=5, sticky="w")

root.mainloop()