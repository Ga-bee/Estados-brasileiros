import turtle
import pandas as pd


#######  Configurar tela

screen = turtle.Screen()

# Título da tela
screen.title("Estados e capitais")

# Imagem que será o fundo
imagem = './mapaBrasil.gif'
screen.addshape(imagem)
turtle.shape(imagem)

# Função que retorna posição do mouse para serem adicionadas no CSV
def coordenadas_do_mouse(x,y):
    print(x,y)

screen.onscreenclick(coordenadas_do_mouse)
# screen.mainloop()

# Lendo o CSV dos estados
estados = pd.read_csv('./estados.txt')

# Lista de acertos
corretos = []

#Estados que faltam ser adivinhados
todos_os_estados = estados["Estado"]

# print(todos_os_estados)

# o jogo roda equanto os acertos forem menores que a quantidade de estados
while len(corretos) < 27:

    # Caixa de pergunta dos nomes dos estados
    resposta = screen.textinput(title=f"{len(corretos)}/27 Acertos", prompt= "Insira o nome de um estado").title()
    
    # filtragem do df para conferir a resposta
    filtered = estados[estados["Estado"] == resposta]

    # Ao tentar sair
    if resposta == "Exit":

        # Estados faltantes passam par umm csv
        faltam = todos_os_estados.to_csv()

        # Cria-se um arquivo .txt escevendo o csv com os estados faltantes
        with open('Estados_faltantes', mode = 'w' ) as w:
            w.write(faltam)
        break


    # Se o coiso for encontrado
    if len(estados[estados["Estado"] == resposta])> 0:

        # A resposta enviada é removida da lista de todos os estados
        todos_os_estados.tolist().remove(resposta)

        # O nome do estado digitado é escrito na tela no ponto do mapa
        st = turtle.Turtle()
        st.penup()
        st.hideturtle()
        st.setpos(int(filtered.x),int(filtered.y))
        st.write(resposta)

        # Verifica se a resposta está na lista de corretos, se sim não faz nada e se não, adiciona a resposta na lista
        if resposta in corretos:
            pass
        else:
            corretos.append(resposta)
        if len(resposta) == 27:
            print('')


screen.exitonclick()






