from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import random
from random import randint

root = tk.Tk()
#root.geometry('560x290') - Tamanho inicial
root.minsize(width=560, height=290) #Tamanho mínimo
root.maxsize(width=560, height=290) #Tamanho máximo
root.title("MiniLife")
root.iconbitmap('pypixel.ico')

s = ttk.Style()
s.configure('TNotebook.Tab', font=('Verdana', '12'), padding=(14, 6), foreground='#212121')
s.configure('TNotebook', background='#fafafa')
s.map('TNotebook.Tab', foreground=[('selected', '#4285F4')])

tabControl = ttk.Notebook(root) #Controle das Tabs
tabPerfil = ttk.Frame(tabControl) #Cria a tabPerfil
tabControl.add(tabPerfil, text='Cartão de aventureiro') #Adiciona a tab
tabTrabalho = ttk.Frame(tabControl) 
#
#
tabAc = ttk.Frame(tabControl)
tabControl.add(tabAc, text='Ações')
tabControl.pack(expand=1, fill='both') #Empacota as Tabs

#TabPerfil
personaNull = ImageTk.PhotoImage(Image.open('personaNull.png'))
N_Label = Label(tabPerfil, image=personaNull)
N_Label.grid(row=0, column=0, columnspan=2, rowspan=6, padx=10, pady=15)

global Char
Char = {'Lvl': 1, 'Hp':300, 'Defesa':50, 'Agilidade':50, 'Destreza':50, 'Inteligência':50, 'Força':50, 'nextXp': 500} #StatusBase
global xp
xp = 0
def atributos(Char, rc):
     global raça
     global classe
     global xp
     RC = rc
     if RC == 0:
          #+Atributos por raça
          if raça =='Humano':
               Char['Agilidade'] += 15
               Char['Inteligência'] += 15
               Char['Força'] += 15
               Char['Destreza'] += 15
          elif raça=='Elfo':
               Char['Inteligência'] += 45
               Char['Agilidade'] += 15
          elif raça =='Anão':
               Char['Destreza'] += 35
               Char['Força'] += 25
          #+Atributos por Classe
          if classe =='Mago':
               Char['Agilidade'] += 5
               Char['Destreza'] += 5
               Char['Inteligência'] += 65
          elif classe=='Arqueiro':
               Char['Destreza'] += 60
               Char['Agilidade'] += 15
          elif classe =='Guerreiro':
               Char['Defesa'] += 25
               Char['Força'] += 50
          
     frameAtributos = LabelFrame(tabPerfil, padx=15, pady=15)
     frameAtributos.config(text='Atributos')
     frameAtributos.grid(row=0, column=4, columnspan=3, rowspan=5, padx=20)
     LvlLabel = Label(frameAtributos, text='Lvl: ' + str(Char.get('Lvl')), font=('Courier New', 12)).grid(row=1, column=0)
     HpLabel = Label(frameAtributos, text='Vida: ' + str(Char.get('Hp')), font=('Courier', 12)).grid(row=2, column=0)
     DefLabel = Label(frameAtributos, text='Defesa: ' + str(Char.get('Defesa')), font=('Courier', 12)).grid(row=3, column=0)
     AgilidadeLabel = Label(frameAtributos, text='Agilidade: ' + str(Char.get('Agilidade')), font=('Courier', 12)).grid(row=4, column=0)
     DestrezaLabel = Label(frameAtributos, text='Destreza: ' + str(Char.get('Destreza')), font=('Courier', 12)).grid(row=5, column=0)
     InteligênciaLabel = Label(frameAtributos, text='Inteligência:  ' + str(Char.get('Inteligência')), font=('Courier', 12)).grid(row=6, column=0)
     ForçaLabel = Label(frameAtributos, text='Força: ' + str(Char.get('Força')), font=('Courier', 12)).grid(row=7, column=0)
     xpLabel = Label(frameAtributos, text='Xp: ' + str(xp) + '/' + str(Char.get('nextXp')), font=('Courier New', 12)).grid(row=8, column=0)
     
def LevelUp(Char, xp):
     nextXp =  Char.get('nextXp')
     if xp >= nextXp:
          Char['nextXp'] = round(Char.get('nextXp') * 2.5)
          Char['Lvl'] += 1
          Char['Hp'] += 20
          Char['Defesa'] += 5
          Char['Agilidade'] += 5
          Char['Destreza'] += 5
          Char['Inteligência'] += 5
          Char['Força'] += 5
     atributos(Char, 1)

#cadastro
guiPerfil = Toplevel()
guiPerfil.title("Criar Cartão de aventureiro ")
guiPerfil.iconbitmap('pypixel.ico')
guiPerfil.geometry('320x300')
guiPerfil.configure(bg="#4a4947")

frameF = LabelFrame(guiPerfil, padx=15, pady=15)
frameF.config(fg='white', bg="#4a4947")
frameF.pack(padx=10, pady=10)

def NomGen():
     global raça
     global classe
     nome = charNome.get()
     if nome == '':
          name = Label(tabPerfil, text='Nome: Unknown', font=('Courier', 12)).grid(row=0, column=2, padx=(5,0), pady=(10,0)) 
     else:
          name = Label(tabPerfil, text='Nome: ' + nome, font=('Courier', 12)).grid(row=0, column=2, padx=(5,0), pady=(10,0))
          
     gender = genero.get()
     if gender == "":
          genderLabel = Label(tabPerfil, text='Genêro: Unknown', font=('Courier', 12)).grid(row=1, column=2, padx=(10,0))
     else:
          genderLabel = Label(tabPerfil, text='Genêro: ' + gender, font=('Courier', 12)).grid(row=1, column=2, padx=(10,0))
     raça = Raça.get()
     if raça == "":
          raçaLabel = Label(tabPerfil, text='Raça: Unknown', font=('Courier', 12)).grid(row=2, column=2, padx=(10,0))
     else:
          raçaLabel = Label(tabPerfil, text='Raça: ' + raça, font=('Courier', 12)).grid(row=2, column=2, padx=(10,0))
          
     classe = Classe.get()
     if classe == "":
          classeLabel = Label(tabPerfil, text='Classe: Unknown', font=('Courier', 12)).grid(row=3, column=2, padx=(10,0))
     else:
          classeLabel = Label(tabPerfil, text='Classe: ' + classe, font=('Courier', 12)).grid(row=3, column=2, padx=(10,0))
     atributos(Char, 0)

def confirmarPerfil():
     global personaH
     global personaM
     global personaNull
     gender = genero.get()#passar imagem dependendo da escolha do genero
     if gender == 'Masculino':
          personaH = ImageTk.PhotoImage(Image.open("personaH.png"))
          H_Label = Label(tabPerfil, image=personaH)
          H_Label.grid(row=0, column=0, columnspan=2, rowspan=6, padx=10, pady=15)
          NomGen()
     elif gender == 'Feminino':
          personaM = ImageTk.PhotoImage(Image.open('personaM.png'))
          M_Label = Label(tabPerfil, image=personaM)
          M_Label.grid(row=0, column=0, columnspan=2, rowspan=6, padx=10, pady=15)
          NomGen()
     else:
          personaNull = ImageTk.PhotoImage(Image.open('personaNull.png'))
          N_Label = Label(tabPerfil, image=personaNull)
          N_Label.grid(row=0, column=0, columnspan=2, rowspan=6, padx=10, pady=15)
          NomGen()
     guiPerfil.destroy()

nomeLabel = Label(frameF, text='Nome:', fg='white', bg='#4a4947').grid(row=0, column=0)
charNome = Entry(frameF, width=30)
charNome.grid(row=0, column=1, columnspan=2)

genero = StringVar()
gen = Label(frameF, text="Genêro:", fg='white', bg="#4a4947").grid(row=1, column=0)
Radiobutton(frameF, text="Feminino", variable=genero, value="Feminino", fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=1)
Radiobutton(frameF, text="Masculino", variable=genero, value="Masculino", fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=2)

frameRaça = LabelFrame(frameF, padx=15, pady=15)
frameRaça.config(fg='white', text='Selecionar Raça', bg="#4a4947")
frameRaça.grid(row=2, column=0, columnspan=3)

Raça = StringVar()
Radiobutton(frameRaça, text='Humano', variable=Raça, value='Humano', fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=0)
Radiobutton(frameRaça, text='Elfo', variable=Raça, value='Elfo', fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=1)
Radiobutton(frameRaça, text='Anão', variable=Raça, value='Anão', fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=2)

frameClasse = LabelFrame(frameF, padx=15, pady=15)
frameClasse.config(fg='white', text='Selecionar Classe ', bg="#4a4947")
frameClasse.grid(row=3, column=0, columnspan=3)

Classe = StringVar()
Radiobutton(frameClasse, text='Mago', variable=Classe, value='Mago', fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=0)
Radiobutton(frameClasse, text='Arqueiro', variable=Classe, value='Arqueiro', fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=1)
Radiobutton(frameClasse, text='Guerreiro', variable=Classe, value='Guerreiro', fg='white', activeforeground='white', bg='#4a4947', activebackground="#4a4947", selectcolor='black').grid(row=1, column=2)

btnConfirm = Button(frameF, text='Confirmar', activeforeground='white', activebackground='lightgreen', command=confirmarPerfil)
btnConfirm.grid(row=8, column=1, ipadx=15, pady=10)

#TabAc
def caçar(Char):
     #(Tupla)Define os lugares onde encontrar monstros
     Lugares = ('no bosque', 'nas montanhas', 'na floresta', 'próximo à uma lagoa', 'invadindo uma vila', 'escondido no mato')
     #(Tupla)Define os monstros disponíveis para batalhar
     Monstros = ('Slime', 'Goblin', 'Lobo Selvagem', 'Ogro', 'Monstro Rochoso', 'Wyvern')
     #Dicionários informando a vida e o atk dos monstros
     Slime = { 'vida': 15, 'ataque': 5, 'xp':50}
     Goblin = { 'vida': 30, 'ataque': 10, 'xp':65}
     LoboSelvagem = { 'vida': 40, 'ataque': 15, 'xp':75}
     Ogro = { 'vida': 50, 'ataque': 25, 'xp':90}
     MonstroRochoso = { 'vida': 80, 'ataque': 30, 'xp':150}
     Wyvern = {'vida': 100, 'ataque': 40, 'xp':200}

     Caçando = Toplevel()
     Caçando.title("Batalhando  ...")
     Caçando.iconbitmap('pypixel.ico')
     Caçando.geometry('680x330')
     Caçando.configure(bg="#4a4947")
     
     frameCaça = LabelFrame(Caçando, bg="#4a4947", fg='white')
     frameCaça.grid(row=0, column=0, columnspan=3, rowspan=5)
     Tc = tk.Text(frameCaça, height=20, width=50)
     Tc.grid(row=0, column=1)
     global batalhar
     batalhar = random.choice(Monstros)
     Tc.insert(END, f'\nVocê encontrou um {batalhar} {random.choice(Lugares)}')
     global Vida
     Vida = Char.get('Hp')
     global VidaMonstro
     if batalhar == 'Slime':
          VidaMonstro = Slime.get('vida')
          Tc.insert(END, f'\n{batalhar} tem uma vida de: {VidaMonstro}\n prepare-se para a batalha.')
          Tc.insert(END, f'''\n
(\__/)
(•ㅅ•)       Sua vida máxima é de: {Vida}
/ 　 づ
''')
          
     if batalhar == 'Goblin':
          VidaMonstro = Goblin.get('vida')
          Tc.insert(END, f'\n{batalhar} tem uma vida de: {VidaMonstro}\n prepare-se para a batalha.')
          Tc.insert(END, f'''\n
(\__/)
(•ㅅ•)       Sua vida máxima é de: {Vida}
/ 　 づ
''')
     if batalhar == 'Lobo Selvagem':
          VidaMonstro = LoboSelvagem.get('vida')
          Tc.insert(END, f'\n{batalhar} tem uma vida de: {VidaMonstro}\n prepare-se para a batalha.')
          Tc.insert(END, f'''\n
(\__/)
(•ㅅ•)       Sua vida máxima é de: {Vida}
/ 　 づ
''')
          
     if batalhar == 'Ogro':
          VidaMonstro = Ogro.get('vida')
          Tc.insert(END, f'\n{batalhar} tem uma vida de: {VidaMonstro}\n prepare-se para a batalha.')
          Tc.insert(END, f'''\n
(\__/)
(•ㅅ•)       Sua vida máxima é de: {Vida}
/ 　 づ
''')
     if batalhar == 'Monstro Rochoso':
          VidaMonstro = MonstroRochoso.get('vida')
          Tc.insert(END, f'\n{batalhar} tem uma vida de: {VidaMonstro}\n prepare-se para a batalha.')
          Tc.insert(END, f'''\n
(\__/)
(•ㅅ•)       Sua vida máxima é de: {Vida}
/ 　 づ
''')
          
     if batalhar == 'Wyvern':
          VidaMonstro = Wyvern.get('vida')
          Tc.insert(END, f'\n{batalhar} tem uma vida de: {VidaMonstro}\n prepare-se para a batalha.')
          Tc.insert(END, f'''\n
(\__/)
(•ㅅ•)       Sua vida máxima é de: {Vida}
/ 　 づ
''')
     def Atacar():
          global VidaMonstro
          global Vida
          global batalhar
          global xp
          global Char
          x = round((Char.get('Força')/10) * (Char.get('Inteligência')/10))
          atk = randint(0, x)
          if atk > 1:
               Tc.delete('1.0', END)
               Tc.insert(END, f'\nVocê desferiu {atk} de dano')
               VidaMonstro -= atk
          else:
               Tc.delete('1.0', END)
               Tc.insert(END, 'Você errou !!!')
               
          if VidaMonstro <= 0:
               Tc.insert(END, f'Você derrotou {batalhar} !!!\n')
               btnAtacar = Button(Caçando, text='Atacar', font=('Courier New', 12), state=DISABLED, padx=25, pady=10, command=Atacar)
               btnAtacar.grid(row=0, column=5, padx=70, pady=(70, 0))
               btnEscapar = Button(Caçando, text='Escapar', font=('Courier New', 12), state=DISABLED, padx=20, pady=10, command=Fugir)
               btnEscapar.grid(row=1, column=5, padx=70, pady=30)
               if batalhar =='Slime':
                    xp += 50
                    Tc.insert(END, 'Você recebeu +50 de experiência')
               if batalhar =='Goblin':
                    xp += 65
                    Tc.insert(END, 'Você recebeu +65 de experiência')
               if batalhar =='Lobo Selvagem':
                    xp += 75
                    Tc.insert(END, 'Você recebeu +75 de experiência')
               if batalhar =='Ogro':
                    xp += 90
                    Tc.insert(END, 'Você recebeu +90 de experiência')
               if batalhar =='Monstro Rochoso':
                    xp += 150
                    Tc.insert(END, 'Você recebeu +150 de experiência')
               if batalhar =='Wyvern':
                    xp += 200
                    Tc.insert(END, 'Você recebeu +200 de experiência')
               LevelUp(Char, xp)
                    
          if VidaMonstro > 0:
               Tc.insert(END, f'\n{batalhar} ainda tem {VidaMonstro} de vida restantes')
               if batalhar =='Slime':
                    atkMonstro = randint(1, Slime.get('ataque'))
               if batalhar =='Goblin':
                    atkMonstro = randint(1, Goblin.get('ataque'))
               if batalhar =='Lobo Selvagem':
                    atkMonstro = randint(1, LoboSelvagem.get('ataque'))
               if batalhar =='Ogro':
                    atkMonstro = randint(1, Ogro.get('ataque'))
               if batalhar =='Monstro Rochoso':
                    atkMonstro = randint(1, MonstroRochoso.get('ataque'))
               if batalhar =='Wyvern':
                    atkMonstro = randint(1, Wyvern.get('ataque'))
               Tc.insert(END, f'\nVocê recebeu {atkMonstro} de dano neste turno.')
               Vida -= atkMonstro
               Tc.insert(END, f'''
(\__/)
(•ㅅ•)       Sua vida atual é de: {Vida}
/ 　 づ
''')
          if Vida <= 0:
               Tc.delete('1.0', END)
               Tc.insert(END, 'Você foi derrotado: Fim de jogo')
               sleep(3)
               btnAtacar = Button(Caçando, text='Atacar', font=('Courier New', 12), state=DISABLED, padx=25, pady=10, command=Atacar)
               btnAtacar.grid(row=0, column=5, padx=70, pady=(70, 0))
               btnEscapar = Button(Caçando, text='Escapar', font=('Courier New', 12), state=DISABLED, padx=20, pady=10, command=Fugir)
               btnEscapar.grid(row=1, column=5, padx=70, pady=30)
               
          
     def Fugir():
          Tc.delete('1.0', END)
          Tc.insert(END, 'Você fugiu da batalha\n')
          Tc.insert(END, '''
──▄█▀█▄──────────██
▄████████▄────▄▀█▄▄▄▄
██▀▼▼▼▼▼──▄▀──█▄▄
█████▄▲▲▲──▄▄▄▀───▀▄
██████▀▀▀▀──▀────────▀▀
''')
          btnAtacar = Button(Caçando, text='Atacar', font=('Courier New', 12), state=DISABLED, padx=25, pady=10, command=Atacar)
          btnAtacar.grid(row=0, column=5, padx=70, pady=(70, 0))
          btnEscapar = Button(Caçando, text='Escapar', font=('Courier New', 12), state=DISABLED, padx=20, pady=10, command=Fugir)
          btnEscapar.grid(row=1, column=5, padx=70, pady=30)
          
     btnAtacar = Button(Caçando, text='Atacar', font=('Courier New', 12), padx=25, pady=10, command=Atacar)
     btnAtacar.grid(row=0, column=5, padx=70, pady=(70, 0))
     btnEscapar = Button(Caçando, text='Escapar', font=('Courier New', 12), padx=20, pady=10, command=Fugir)
     btnEscapar.grid(row=1, column=5, padx=70, pady=30)

def catalogo():
     Catalogo = Toplevel()
     Catalogo.title("Catálogo")
     Catalogo.iconbitmap('pypixel.ico')
     Catalogo.geometry('970x310')
     Catalogo.configure(bg="#4a4947")
     
     frameCatl = LabelFrame(Catalogo, bg="#4a4947", fg='white')
     frameCatl.grid(row=0, column=0, columnspan=3, rowspan=5)
     Tcat = tk.Text(frameCatl, height=8, width=120)
     Tcat.grid(row=0, column=1, columnspan=6, rowspan=3)

     def slime():
          Slime = { 'vida': 15, 'ataque': 5, 'descrição': 'Uma pequena criaturinha gosmenta, muitas vezes inofenciva. \nCostumam ser encontrados perto de florestas e bosques'}
          Tcat.delete('1.0', END)
          Tcat.insert(END, 'Slime\n')
          Tcat.insert(END, f"Vida: {Slime.get('vida')}\n")
          Tcat.insert(END, f"Ataques dessa criatura variam de 1 à {Slime.get('ataque')}")
          Tcat.insert(END, f"\nDescrição: {Slime.get('descrição')}")
     def goblin():
          Goblin = { 'vida': 30, 'ataque': 10,  'descrição': 'Goblins são pequenos humanoides monstruosos que não medem muito mais que um metro. \nA cor da pele dos goblins depende do ambiente em que vivem; os tons de cor incluem verde, cinza e azul, embora goblins negros ou mesmo completamente pálidos já foram vistos.'}
          Tcat.delete('1.0', END)
          Tcat.insert(END, 'Goblin\n')
          Tcat.insert(END, f"Vida: {Goblin.get('vida')}\n")
          Tcat.insert(END, f"Ataques dessa criatura variam de 1 à {Goblin.get('ataque')}")
          Tcat.insert(END, f"\nDescrição: {Goblin.get('descrição')}")

     def lobo():
         LoboSelvagem = { 'vida': 40, 'ataque': 15, 'descrição': 'Lobo Selvagem é considerado perigoso, não apenas por ser um animal predador, mas também por geralmente ser encontrado como parte de uma alcateia.' }
         Tcat.delete('1.0', END)
         Tcat.insert(END, 'Lobo Selvagem\n')
         Tcat.insert(END, f"Vida: {LoboSelvagem.get('vida')}\n")
         Tcat.insert(END, f"Ataques dessa criatura variam de 1 à {LoboSelvagem.get('ataque')}")
         Tcat.insert(END, f"\nDescrição: {LoboSelvagem.get('descrição')}")
     def ogro():
          Ogro = { 'vida': 50, 'ataque': 25,'descrição': 'Ogros são conhecidos por ter uma grande quantidade de força.' }
          Tcat.delete('1.0', END)
          Tcat.insert(END, 'Ogro\n')
          Tcat.insert(END, f"Vida: {Ogro.get('vida')}\n")
          Tcat.insert(END, f"Ataques dessa criatura variam de 1 à {Ogro.get('ataque')}")
          Tcat.insert(END, f"\nDescrição: {Ogro.get('descrição')}")
     def monstroR():
          MonstroRochoso = { 'vida': 80, 'ataque': 30, 'descrição': 'Pouco se sabe sobre eles. Alguns dizem que são como golems, porém construídos a partir de magias mais antigas. \nCom seu propósito perdido esses monstros vagam pelo mundo sem rumo.' }
          Tcat.delete('1.0', END)
          Tcat.insert(END, 'Monstro Rochoso\n')
          Tcat.insert(END, f"Vida: {MonstroRochoso.get('vida')}\n")
          Tcat.insert(END, f"Ataques dessa criatura variam de 1 à {MonstroRochoso.get('ataque')}")
          Tcat.insert(END, f"\nDescrição: {MonstroRochoso.get('descrição')}")
     def wyvern():
          Wyvern = {'vida': 100, 'ataque': 40, 'descrição': 'Um animal mítico geralmente representado como uma criatura alada de duas pernas que se assemelha a um dragão'}
          Tcat.delete('1.0', END)
          Tcat.insert(END, 'Wyvern\n')
          Tcat.insert(END, f"Vida: {Wyvern.get('vida')}\n")
          Tcat.insert(END, f"Ataques dessa criatura variam de 1 à {Wyvern.get('ataque')}")
          Tcat.insert(END, f"\nDescrição: {Wyvern.get('descrição')}")

     btnMonster = Button(Catalogo, text='Slime', bg="#363232", fg="white", font=('Courier New', 12), command=slime).grid(row=5, column=0, padx=20, pady=30)
     btnMonster = Button(Catalogo, text='Goblin', bg="#363232", fg="white", font=('Courier New', 12), command=goblin).grid(row=5, column=1, padx=20, pady=30)
     btnMonster = Button(Catalogo, text='Lobo', bg="#363232", fg="white", font=('Courier New', 12), command=lobo).grid(row=5, column=2, padx=20, pady=30)
     btnMonster = Button(Catalogo, text='Ogro', bg="#363232", fg="white", font=('Courier New', 12), command=ogro).grid(row=6, column=0, padx=20, pady=30)
     btnMonster = Button(Catalogo, text='MonstroRochoso', bg="#363232", fg="white", font=('Courier New', 12), command=monstroR).grid(row=6, column=1, padx=20, pady=30)
     btnMonster = Button(Catalogo, text='Wyvern',bg="#363232", fg="white", font=('Courier New', 12), command=wyvern).grid(row=6, column=2, padx=20, pady=30)


     
btn_Caçar = Button(tabAc, text="Procurar por Monstros", padx=35, pady=15, bg="#363232", fg="white", font=('Courier New', 12), command=lambda: caçar(Char))
btn_Caçar.grid(row=0, column=1, columnspan=3, padx=130, pady=(45, 0), ipadx=5)
btn_Catl = Button(tabAc, text="Catálogo de Monstros", padx=35, pady=15, bg="#363232", fg="white",font=('Courier New', 12), command=catalogo)
btn_Catl.grid(row=1, column=1, columnspan=3, padx=130, pady=20, ipadx=10)

root.mainloop()
