from tkinter import *
from tkinter import ttk
from random import choice
from funcoes_jogo import conferir_resultado

# Funções
def jogar():
    radio_pedra.place_forget()
    radio_papel.place_forget()
    radio_tesoura.place_forget()
    label_escolha_pc['text'] = 'O PC está escolhendo...'
    img_path = dados_opcoes[str(usuario.get())]
    sortear_escolha_pc()
    
def sortear_escolha_pc(count=0):
    if count < 30:
        escolha_pc = choice(['pedra','papel','tesoura'])
        label_pc.config(image=dados_opcoes[escolha_pc])
        label_pc.after(120, lambda: sortear_escolha_pc(count + 1))
    else:
        escolha_pc = choice(['pedra','papel','tesoura'])
        label_pc.config(image=dados_opcoes[escolha_pc])
        label_escolha_pc['text'] = 'O PC escolheu:'
        resultado, cor = conferir_resultado(usuario.get(), escolha_pc, label_resultado)
        label_resultado.after(2000, edita_cor_text_label(label_resultado, resultado, cor))

def edita_cor_text_label(label, resultado, cor):
    label.config(text=resultado, fg=cor)


def configura_radiobutton(radio_button, valor, imagem):
    radio_button.config(variable=usuario, value=valor, image=imagem, compound='left', indicatoron=False, bg=bg_color, borderwidth=0, highlightthickness=0, selectcolor='orange')

# Configurações
root = Tk()
root.minsize(500, 800)
bg_color = '#FFFF88'

# Imagens
path_pedra_img = './imgs/rock_100.png'
path_papel_img = './imgs/paper_100.png'
path_tesoura_img = './imgs/scissor_100.png'

imagem_pedra = PhotoImage(file=path_pedra_img)
imagem_papel = PhotoImage(file=path_papel_img)
imagem_tesoura = PhotoImage(file=path_tesoura_img)

dados_opcoes = {
    'pedra': imagem_pedra,
    'papel': imagem_papel,
    'tesoura': imagem_tesoura,
}

style = ttk.Style()
style.configure("TSeparator", background="lightgrey")

# Variáveis
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'

# Widgets
root.config(bg=bg_color)
font_button = ('Open Sans', 12, 'bold')
font_pc_escolha = ('Open Sans', 16)
separator_antes = ttk.Separator(root, orient='horizontal')
separator_dps = ttk.Separator(root, orient='horizontal')

usuario = StringVar()

radio_pedra = Radiobutton(root, image=imagem_pedra)
radio_papel = Radiobutton(root, image=imagem_papel)
radio_tesoura = Radiobutton(root, image=imagem_tesoura)

configura_radiobutton(radio_pedra, pedra, imagem_pedra)
configura_radiobutton(radio_papel, papel, imagem_papel)
configura_radiobutton(radio_tesoura, tesoura, imagem_tesoura)

label_vs = Label(root, text='VS', font=('Open Sans', 18, 'bold'), bg=bg_color)

button_instruction = Button(root, text='Instruções', font=font_button, width=59, height=3, bg='orange', fg='white')
button_jogar = Button(root, text='Jogar', font=font_button, bg='orange', command=jogar)

label_escolha_pc = Label(root, text='Escolha uma opção para continuar', bg=bg_color, font=font_pc_escolha)
label_jogador = Label(root, image=imagem_pedra, bg=bg_color)
label_pc = Label(root, image=imagem_pedra, bg=bg_color)
label_resultado = Label(root, font=('Open Sans', 18, 'bold'), bg=bg_color)

# Posicionamento
button_jogar.place(x=0, y=0)
radio_pedra.place(x=60, y=400)
radio_papel.place(x=210, y=400)
radio_tesoura.place(x=360, y=400)
button_instruction.place(x=0, y=735)
label_escolha_pc.place(x=60, y=200)
label_jogador.place(x=50, y=250)
label_pc.place(x=340, y=250)
label_resultado.place(x=190, y=400)
separator_dps.place(x=290, y=300, width=40, height=10)
separator_antes.place(x=170, y=300, width=40, height=10)
label_vs.place(x=230, y=290)
separator_dps.place(x=290, y=300, width=40, height=10)

root.mainloop()
