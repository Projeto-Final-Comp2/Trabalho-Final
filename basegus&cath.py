# ======================================================= #
# DOUCMENTAÇÃO DO ARQUIVO
# ------------------------------------------------------- #
# OBS: Alterar somente 'Turma' e 'Grupo'
# ======================================================= #
__doc__ = '''
---------------------------------------------------------
Trabalho Final - Computação II
---------------------------------------------------------
Professor: Natanael Quintino
---------------------------------------------------------
Projeto        : Calculadora
Data da entrega: 22/10 (valendo 100% da nota)
                 29/10 (valendo  80% da nota)
---------------------------------------------------------
Turma: EB? (4: Tarde, 5: Manha)
Grupo: 1.
       2.
       3.
Nota :
---------------------------------------------------------
'''

# ======================================================= #
# INÍCIO DA CLASSE BASE
# ======================================================= #

# Importando TODO conteúdo do módulo de interfaces
# gráficas 'tkinter'
from math import *
from tkinter import *
from tkinter import messagebox

class JanelaBase():
    'Classe geradora da janela gráfica'

    # Importando um pacote interno do python
    import sys

    # Listando todos os atributos e método públicos
    __all__ = [
        'expressao', 'conteudoCaixa', 'rodandoJanela'
    ]

    # Método Privado
    def __configurarJanela(
        self       : object,
        comprimento: [int,float],
        altura     : [int,float],
        titulo     : str,
        corFundo   : str,
        ):
        'Configurando alguns parâmetros da janela'

        # Definindo a cor de fundo da janela gráfica
        self.janela.configure(background=corFundo)

        # Definindo o título da janela gráfica
        self.janela.title(titulo)

        # Definindo o tamanho da janela gráfica
        self.janela.geometry(f'{comprimento}x{altura}')

        return None

    # Método Privado
    def __configurarBotao(
        self       : object,
        corTexto   : str,
        corFundo   : str,
        altura     : [int,float],
        comprimento: [int,float]
        ):
        'Configurando alguns parâmetros dos botoes'

        # Criando atributos privados com os parametros
        self.__corBotaoTexto    = corTexto
        self.__corBotaoBg       = corFundo
        self.__alturaBotao      = altura
        self.__comprimentoBotao = comprimento

        return None

    # Método Privado
    def __criarAtributos(
        self: object
        ):
        'Criando os atributos necessários'

        # Criando o atributo 'expressao' para armazenar
        # o conteúdo a ser resolvido pelo python
        self.expressao = ''

        # Criando um atributo com uma variável de janela
        # gráfica, do tipo str, para armazenar o conteúdo
        # a ser digitado/exibido na caixa de textoCaixa = StringVar()
        self.conteudoCaixa = StringVar()

        return None

    # Método Privado
    def __criarWidgets(
        self: object
        ):
 #trecos
        'Criando e posicionando os widgets na janela'
        # Criando caixa para digitação de textos na janela
        # gráfica e direcionando seu conteúdo ao atributo
        # 'equação'
        self.caixaDaEquacao = Entry(
            self.janela, textvariable=self.conteudoCaixa,
            borderwidth=2
        )

        # Posicionando a caixa de texto considerando a
        # mescalgem de 3 colunas de espaço, tendo 10 px
        # de distância entre a borda desse espaço e a caixa
        self.caixaDaEquacao.grid(columnspan=3, ipadx=10)

        # Definindo um valor inicial/padrão para a caixa
        # de texto
        self.conteudoCaixa.set('O que vamos calcular?')

        # Criando um botão funcional com o texto '1'
        self.botao1 = Button(
            self.janela,                 # Onde será colocado o botão
            text='1',                    # Texto a ser exibido no botão
            fg=self.__corBotaoTexto,        # Cor do texto
            bg=self.__corBotaoBg,          # Cor de fundo do botão
            height=self.__alturaBotao,     # Altura do botão
            width=self.__comprimentoBotao, # Comprimento do botão
            command=lambda:self.__adicionaValor(1),
#funçao ĺambda: n preciso dar nome
            # Função a ser executada ao clicar no botão
        )

        # Criando um botão funcional com o texto '2'
        self.botao2 = Button(
            self.janela,
            text='2',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(2)
        )

        # Criando um botão funcional com o texto '3'
        self.botao3 = Button(
            self.janela,
            text='3',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(3)
        )

        # Criando um botão funcional com o texto '4'
        self.botao4 = Button(
            self.janela,
            text='4',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(4)
        )

        # Criando um botão funcional com o texto '5'
        self.botao5 = Button(
            self.janela,
            text='5',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(5)
        )

        # Criando um botão funcional com o texto '6'
        self.botao6 = Button(
            self.janela,
            text='6',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(6)
        )

        # Criando um botão funcional com o texto '7'
        self.botao7 = Button(
            self.janela,
            text='7',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(7)
        )

        # Criando um botão funcional com o texto '8'
        self.botao8 = Button(
            self.janela,
            text='8',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(8)
        )

        # Criando um botão funcional com o texto '9'
        self.botao9 = Button(
            self.janela,
            text='9',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(9)
        )

        # Criando um botão funcional com o texto '0'
        self.botao0 = Button(
            self.janela,
            text='0',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(0)
        )

        # Criando um botão funcional com o texto '+'
        self.botaoPlus = Button(
            self.janela,
            text='+',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('+')
        )

        # Criando um botão funcional com o texto '-'
        self.botaoMinus = Button(
            self.janela,
            text='-',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('-')
        )

        # Criando um botão funcional com o texto '*'
        self.botaoMultiply = Button(
            self.janela,
            text='x',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('x')
        )

        # Criando um botão funcional com o texto '/'
        self.botaoDivide = Button(
            self.janela,
            text='÷',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('÷')
        )

        # Criando um botão funcional com o texto '.'
        self.botaoDecimal= Button(
            self.janela,
            text='.',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('.')
        )

        # Criando um botão funcional com o texto '='
        self.botaoEqual = Button(
            self.janela,
            text='=',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__resolveExpressao
        )

        # Criando um botão funcional com o texto 'C'
        self.botaoClear = Button(
            self.janela,
            text='C',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__limpar
        )

        #self.botaoShift = Button(
            #self.janela,                 
            #text='Shift',                    
            #fg=self.__corBotaoTexto,        
            #bg=self.__corBotaoBg,          
            #height=self.__alturaBotao,     
            #width=self.__comprimentoBotao, 
            #command=self.__,
        #)

        # Criando um botão funcional com o texto 'π'
        self.botaoPi = Button(
            self.janela,
            text='π',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('π')
        )

        # Criando um botão funcional com o texto 'e'
        self.botaoEulerNumber = Button(
            self.janela,
            text='e',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('e')
        )

        # Criando um botão funcional com o texto 'n!'
        self.botaoFatorial = Button(
            self.janela,
            text='n!',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__fatorial
        )

        # Criando um botão funcional com o texto 'Ln' 
        self.botaoLn = Button(
            self.janela,
            text='Ln',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__log
        )

        # Criando um botão funcional com o texto 'Rad' 
        self.botaoConverteRadianos = Button(
            self.janela,
            text='Rad',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__rad
        )
        # Criando um botão funcional com o texto 'Graus'  
        self.botaoConverteGraus = Button(
            self.janela,
            text='Graus',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__deg
        )
        # Criando um botão funcional com o texto '('  
        self.botaoParenteses1 = Button(
            self.janela,
            text='(',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('(')
        )

        # Criando um botão funcional com o texto ')'
        self.botaoParenteses2 = Button(
            self.janela,
            text=')',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(')')
        )

        # Criando um botão funcional com o texto 'Sin'
        self.botaoSin = Button(
            self.janela,
            text='Sin',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__sin
        )

        # Criando um botão funcional com o texto 'Cos'
        self.botaoCos = Button(
            self.janela,
            text='Cos',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__cos
        )

        # Criando um botão funcional com o texto 'Tan'
        self.botaoTan = Button(
            self.janela,
            text='Tan',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__tan
        )

        # Criando um botão funcional com o texto 'xʸ'
        self.botaoElevado = Button(
            self.janela,
            text='xʸ',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('**') 
        )

        # Criando um botão funcional com o texto 'Del'
        self.botaoApagar = Button(
            self.janela,
            text='Del',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__apagar
        )

        # Criando um botão funcional com o texto '?'
        self.botaoManual = Button(
            self.janela,
            text='?',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__manual
        )

        # Criando um botão funcional com o texto 'Med'
        self.botaoMedia = Button(
            self.janela,
            text='Med',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__media
        )

        # Criando um botão funcional com o texto 'X/Y'
        self.botaoFracao = Button(
            self.janela,
            text='X/Y',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__fracao
        )

        # Criando um botão funcional com o texto 'Rom'
        self.botaoRomanos = Button(
            self.janela,
            text='Rom',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__romanos
        )

        # Criando um botão funcional com o texto '~='
        self.arredondar = Button(
            self.janela,
            text='~=',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__arredondar
        )
    
        # Posicionando os botões considerando um grid
        # com 6 linhas e 4 colunas
        self.botao1               .grid(row=4, column=0)
        self.botao2               .grid(row=4, column=1)
        self.botao3               .grid(row=4, column=2)
        self.botao4               .grid(row=3, column=0)
        self.botao5               .grid(row=3, column=1)
        self.botao6               .grid(row=3, column=2)
        self.botao7               .grid(row=2, column=0)
        self.botao8               .grid(row=2, column=1)
        self.botao9               .grid(row=2, column=2)
        self.botao0               .grid(row=5, column=1)
        self.botaoPlus            .grid(row=2, column=3)
        self.botaoMinus           .grid(row=3, column=3)
        self.botaoMultiply        .grid(row=4, column=3)
        self.botaoDivide          .grid(row=5, column=3)
        self.botaoEqual           .grid(row=5, column=2)
        self.botaoClear           .grid(row=6, column=3)
        self.botaoDecimal         .grid(row=5, column=0)
        self.botaoParenteses1     .grid(row=6, column=0)
        self.botaoParenteses2     .grid(row=6, column=1)
        self.botaoSin             .grid(row=2, column=4)
        self.botaoCos             .grid(row=3, column=4)
        self.botaoTan             .grid(row=4, column=4)
        self.botaoElevado         .grid(row=6, column=2)
        self.botaoApagar          .grid(row=6, column=4)
        self.botaoManual          .grid(row=8, column=3)
        self.botaoPi              .grid(row=7, column=2)
        self.botaoEulerNumber     .grid(row=7, column=3)
        self.botaoFatorial        .grid(row=7, column=0)
        self.botaoLn              .grid(row=7, column=1)
        self.botaoConverteRadianos.grid(row=7, column=4)
        self.botaoConverteGraus   .grid(row=8, column=4)
        self.botaoMedia           .grid(row=5, column=4)
        self.botaoFracao          .grid(row=8, column=0)
        self.botaoRomanos         .grid(row=8, column=1)
        self.arredondar           .grid(row=8, column=2)
        return None

    # Método Privado
    def __adicionaValor(
        self : object,
        valor: [int,str]
        ):
        'Adicionando valor à expressão'

        # Adicionando o valor à expressao
        self.expressao += str(valor)

        # Atualizando expressão na caixa
        self.conteudoCaixa.set(self.expressao)

        return None

    # Método Privado
    def __fecharJanela(
        self: object
        ):
        'Fechando janela'

        # Excutando fechamento
        self.janela.destroy()

        return None

    # Método Privado
    def __limpar(
        self : object,
        event: 'Event' = None
        ):
        "Limpando entrada de texto e variavel 'expressao'"

        # Limpando expressao
        self.expressao = ''

        # Limpando caixa de texto
        self.conteudoCaixa.set('')

        return None

    def __apagar(
        self : object,
        event: 'Event' = None
        ):
        "Apagar apenas o ultimo caractere pra eu nao ter que digitar de novo a funçao inteira a cada erro"

        self.expressao = self.conteudoCaixa.get()
        for i in self.expressao:
            self.conteudoCaixa.set(self.expressao[:-1])

        return None
    
    # Método Privado
    def __perguntarPraSair(
        self : object,
        event: 'Event' = None
        ):
        'Exibe uma janela perguntando se deseja fechar a janela'

        # Abrindo janela com o diálogo
        decisao = messagebox.askyesno(
            'Fechar calculadora',
            'Acabaram os cálculos por hoje?'
        )

        # Verificando decisão
        if decisao == True:
            # Fechando a janela
            self.__fecharJanela()

        else:
            # Faça nada
            pass

        return None

    # Método Privado
    def __manual(
        self : object,
        event: 'Event' = None
        ):
        'Exibe uma janela perguntando se deseja fechar a janela'

        # Abrindo janela com o diálogo
        decisao = messagebox.showinfo(
            'Manual',
            'Olá! Dúvidas? Veja se isso ajuda:\n\nLog: Por a base e o logaritmando\n'
        )
        return None

    # Método Privado
    def __media(
        self : object,
        event: 'Event' = None
        ):
        'Faz media da soma de numeros'
        nova=[]
        listaemstr = str(self.expressao).split('+')
        for i in listaemstr:
            nova.append(int(i))
        self.conteudoCaixa.set(sum(nova)/len(nova)) 
        return None

    # Método Privado
    def __fracao(
        self : object,
        event: 'Event' = None
        ):
        'Faz o resultado de uma divisão aparecer no formato de fração, apenas simplificado'
        nova=[]
        listaemstr = str(self.expressao).split('÷')
        for i in listaemstr:
            nova.append(int(i))
        divisor=gcd(nova[0],nova[1])
        fracao=int(nova[0]/divisor),'/',int(nova[1]/divisor)
        self.conteudoCaixa.set(fracao)
        return None

    # Método Privado
    def __romanos(
        self : object,
        event: 'Event' = None
        ):
        'Transforma os numeros em numeros romanos'
        num = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        rom = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        resultado = []
        self.expressao=int(self.expressao)
        if 0 < self.expressao < 4000:
            for i in range(len(num)):
                numero = int(self.expressao) / num[i]
                resultado.append(rom[i] * int(numero))
                self.expressao -= num[i] * int(numero)
            final = ''.join(resultado)
            self.conteudoCaixa.set(final)
        else:
            self.conteudoCaixa.set('O número precisa ser <4000')
        return None

    # Método Privado
    def __sin(
        self : object,
        event: 'Event' = None
        ):
        'transforma o grau dado em radianos e devolve o sin'
        self.expressao=int(self.expressao)
        nova=radians(self.expressao)
        seno=sin(nova)
        string=str(seno)
        self.conteudoCaixa.set(string)
        return None

    # Método Privado
    def __cos(
        self : object,
        event: 'Event' = None
        ):
        'transforma o grau dado em radianos e devolve o cos'
        self.expressao=int(self.expressao)
        nova=radians(self.expressao)
        cose=cos(nova)
        string=str(cose)
        self.conteudoCaixa.set(string)
        return None

    # Método Privado
    def __tan(
        self : object,
        event: 'Event' = None
        ):
        'transforma o grau dado em radianos e devolve o tan'
        self.expressao=int(self.expressao)
        nova=radians(self.expressao)
        tang=tan(nova)
        string=str(tang)
        self.conteudoCaixa.set(string)
        return None

    # Método Privado
    def __arredondar(
        self : object,
        event: 'Event' = None
        ):
        'arredonda o valor'
        string = self.conteudoCaixa.get()
        self.expressao=float(string)
        self.conteudoCaixa.set(round(self.expressao,1))
        return None

    # Método Privado
    def __fatorial(
        self : object,
        event: 'Event' = None
        ):
        'devolve o fatorial do numero'
        self.conteudoCaixa.set(factorial(int(self.expressao)))
        return None

    # Método Privado
    def __log(
        self : object,
        event: 'Event' = None
        ):
        'devolve o log do numero'
        self.conteudoCaixa.set(log(int(self.expressao)))
        return None

    # Método Privado
    def __rad(
        self : object,
        event: 'Event' = None
        ):
        'transforma o grau dado em radianos'
        self.conteudoCaixa.set(radians(int(self.expressao)))
        return None

    # Método Privado
    def __deg(
        self : object,
        event: 'Event' = None
        ):
        'transforma o radianos dado em graus'
        self.conteudoCaixa.set(round(degrees(float(self.expressao))))
        return None
    
    # Método Privado
    def __resolveExpressao(
        self : object,
        event: 'Event' = None
        ):
        'Avaliando a expressao e exibindo seu resultado'

        # Definindo uma variavel para verificar
        # se houve erro ou nao
        houveErro = True

        # Tratando possíveis erros
        try:
            # Ajustando os simbolos de multiplicação e divisão
            expressao = self.expressao.replace('x','*').replace('÷','/').replace('π','pi')

            # Avaliando a expressão
            resultado = eval(expressao)

            # Redefinindo a expressão pelo resultado
            self.expressao = str(resultado)

            # Exibindo resultado na caixa
            self.conteudoCaixa.set(str(resultado))

            # Informando que houve erro
            houveErro = False

        except SyntaxError as erroInfo:
            # Reportando erro no shell
            print(f'\nErroDeSintaxe: {erroInfo}\n', file=sys.stderr)

        except NameError as erroInfo:
            # Reportando erro no shell
            print(f'\nErroDeNome: {erroInfo}\n', file=sys.stderr)

        except:
            # Reportando erro no shell
            print(f'\nDeuRuim: Problema desconhecido\n', file=sys.stderr)

        finally:
            # Verificando se houve erro
            if houveErro:
                # Limpando a expressao na memória
                self.expressao = ''

                # Informando erro na caixa
                self.conteudoCaixa.set('Vish, deu erro... Tenta de novo!')

            else:
 #nem precisava pq ele iria em frente
                # Faça nada
                pass


        return None

    def __definirAcoesTeclado(
        self: object
        ):
        'Definindo as ações de teclado'

        # Habilitando ENTER para resolver a equação
        self.janela.bind('<Return>', self.__resolveExpressao)

        # Habilitando ESC para fechar a janela
        self.janela.bind('<Escape>', self.__perguntarPraSair)

        # Habilitando BACKSPACE para limpar caixa de texto
        self.janela.bind('<BackSpace>', self.__limpar)


        return None

    # Método Público    
    def rodandoJanela(
        comprimento     : [int,float] = 310,
        altura          : [int,float] = 230,
        titulo          : str         = 'Calculadora',
        corFundo        : str         = 'pink',
        corFundoBotao   : str         = 'pink',
        corTextoBotao   : str         = 'black',
        alturaBotao     : [int,float] = 1,
        comprimentoBotao: [int,float] = 4,
        myFile          : 'file'      = sys.stderr # sys.stderr: Texto no Shell Vermelho
                                                   # sys.stdout: Texto no Shell Azul
                                                   # yourFile  : Texto no Arquivo '.txt' dado
        ):
        'Executando janela e sua funções'

        #self.botao1 = Button(
            #self.janela,                 # Onde será colocado o botão
            #text='1',                    # Texto a ser exibido no botão
            #fg=self.__corBotaoTexto,        # Cor do texto
            #bg=self.__corBotaoBg,          # Cor de fundo do botão
            #height=self.__alturaBotao,     # Altura do botão
            #width=self.__comprimentoBotao, # Comprimento do botão
            #command=lambda:self.__adicionaValor(1

        # Criando uma instancia da janela base
        print('\n> Instanciando uma janela base', end='... ', file=myFile)
        self = JanelaBase()
        print('OK',file=myFile)

        # Instanciando uma janela do Tkinter
        print('\n> Instanciando uma janela do Tkinter', end='... ', file=myFile)
        self.janela = Tk()
        print('OK',file=myFile)

        # Definindo as configurações da janela gráfica
        print('\n> Configurado janela', end='... ', file=myFile)
        self.__configurarJanela(
            comprimento, altura, titulo, corFundo
        )
        print('OK',file=myFile)

        # Definindo as configurações dos botões
        print('\n> Configurando botões',end='... ', file=myFile)
        self.__configurarBotao(
            corTextoBotao, corFundoBotao, alturaBotao,
            comprimentoBotao
        )
        print('OK',file=myFile)

        # Criando os atributos necessários
        print('\n> Criando Atributos',end='... ', file=myFile)
        self.__criarAtributos()
        print('OK',file=myFile)

        # Criando e posicionando os widgets na janela
        print('\n> Criando Widgets',end='... ', file=myFile)
        self.__criarWidgets()
        print('OK',file=myFile)

        # Definindo ações de teclado
        print('\n> Definindo as ações de teclado',end='... ', file=myFile)
        self.__definirAcoesTeclado()
        print('OK',file=myFile)

        # Rodando aplicação
        print('\n> Janela pronta para execução! ;D', file=myFile)
        self.janela.mainloop()

        # Fechando arquivo caso de '.txt'
        if 'idlelib' not in str(type(myFile)):
            myFile.close()

        return None

# ======================================================= #
# FIM DA CLASSE BASE
# ======================================================= #

# Como executar a janela
if __name__ == "__main__":

    # Informando início do programa
    print('\nPrograma iniciado\n')

    # Executando janela
    JanelaBase.rodandoJanela(
        myFile=open('log.txt','w')
    )

    # Informando fim do programa
    print('\n\nPrograma encerrado\n')
