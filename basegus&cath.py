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
Turma: EB5 (4: Tarde, 5: Manha)
Grupo: 1. Gustavo Darmont
       2. Maria Catharina Bueno
Nota :
---------------------------------------------------------
'''

# ======================================================= #
# INÍCIO DA CLASSE BASE
# ======================================================= #

# Importando TODO conteúdo do módulo de interfaces
# gráficas 'tkinter'
from math import *
from statistics import *
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
        altura     : [int,float],
        comprimento: [int,float]
        ):
        'Configurando alguns parâmetros dos botoes'

        # Criando atributos privados com os parametros
        self.__corBotaoTexto    = corTexto
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
        
        'Criando e posicionando os widgets na janela'
        # Criando caixa para digitação de textos na janela
        #definindo a largura
        # gráfica e direcionando seu conteúdo ao atributo
        # 'equação'
        self.caixaDaEquacao = Entry(
            self.janela, textvariable=self.conteudoCaixa,
            width=30, borderwidth=1,
        )
        #self.caixaDaEquacao.width('1')
        
        # Posicionando a caixa de texto considerando a
        # mescalgem de 3 colunas de espaço, tendo 10 px
        # de distância entre a borda desse espaço e a caixa
        self.caixaDaEquacao.grid(columnspan=4, ipadx=4)
        self.caixaDaEquacao.icursor(len(self.caixaDaEquacao.get()))

        # Definindo um valor inicial/padrão para a caixa
        # de texto
        self.conteudoCaixa.set('O que vamos calcular?')

        # Criando um botão funcional com o texto '1'
        self.botao1 = Button(
            self.janela,                   # Onde será colocado o botão
            text='1',                      # Texto a ser exibido no botão
            fg=self.__corBotaoTexto,       # Cor do texto
            bg='hot pink',                 # Cor de fundo do botão
            height=self.__alturaBotao,     # Altura do botão
            width=self.__comprimentoBotao, # Comprimento do botão
            command=lambda:self.__adicionaValor(1)
            # Função a ser executada ao clicar no botão
        )

        # Criando um botão funcional com o texto '2'
        self.botao2 = Button(
            self.janela,
            text='2',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(2)
        )

        # Criando um botão funcional com o texto '3'
        self.botao3 = Button(
            self.janela,
            text='3',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(3)
        )

        # Criando um botão funcional com o texto '4'
        self.botao4 = Button(
            self.janela,
            text='4',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(4)
        )

        # Criando um botão funcional com o texto '5'
        self.botao5 = Button(
            self.janela,
            text='5',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(5)
        )

        # Criando um botão funcional com o texto '6'
        self.botao6 = Button(
            self.janela,
            text='6',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(6)
        )

        # Criando um botão funcional com o texto '7'
        self.botao7 = Button(
            self.janela,
            text='7',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(7)
        )

        # Criando um botão funcional com o texto '8'
        self.botao8 = Button(
            self.janela,
            text='8',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(8)
        )

        # Criando um botão funcional com o texto '9'
        self.botao9 = Button(
            self.janela,
            text='9',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(9)
        )

        # Criando um botão funcional com o texto '0'
        self.botao0 = Button(
            self.janela,
            text='0',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(0)
        )

        # Criando um botão funcional com o texto '+'
        self.botaoMais = Button(
            self.janela,
            text='+',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('+')
        )

        # Criando um botão funcional com o texto '-'
        self.botaoMenos = Button(
            self.janela,
            text='-',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('-')
        )

        # Criando um botão funcional com o texto '*'
        self.botaoVezes = Button(
            self.janela,
            text='x',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('x')
        )

        # Criando um botão funcional com o texto '/'
        self.botaoDivisao = Button(
            self.janela,
            text='÷',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('÷')
        )

        # Criando um botão funcional com o texto '.'
        self.botaoPonto= Button(
            self.janela,
            text='.',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('.')
        )

        # Criando um botão funcional com o texto '='
        self.botaoIgual = Button(
            self.janela,
            text='=',
            fg=self.__corBotaoTexto,
            bg='hot pink',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__resolveExpressao
        )

        # Criando um botão funcional com o texto '('  
        self.botaoParenteses1 = Button(
            self.janela,
            text='(',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('(')
        )

        # Criando um botão funcional com o texto ')'
        self.botaoParenteses2 = Button(
            self.janela,
            text=')',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(')')
        )

        # Criando um botão funcional com o texto 'xʸ'
        self.botaoElevado = Button(
            self.janela,
            text='xʸ',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('^') 
        )
        
        # Criando um botão funcional com o texto 'C'
        self.botaoLimpar = Button(
            self.janela,
            text='C',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__limpar
        )

        # Criando um botão funcional com o texto 'n!'
        self.botaoFatorial = Button(
            self.janela,
            text='n!',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__fatorial
        )

        # Criando um botão funcional com o texto 'Ln' 
        self.botaoLn = Button(
            self.janela,
            text='Ln',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__log
        )

        # Criando um botão funcional com o texto 'π'
        self.botaoPi = Button(
            self.janela,
            text='π',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('π')
        )

        # Criando um botão funcional com o texto 'e'
        self.botaoEulerNumber = Button(
            self.janela,
            text='e',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('e')
        )

        # Criando um botão funcional com o texto 'X/Y'
        self.botaoFracao = Button(
            self.janela,
            text='X/Y',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__fracao
        )

        # Criando um botão funcional com o texto '√'
        self.botaoRaiz = Button(
            self.janela,
            text='√',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('^(1/')
        )

        # Criando um botão funcional com o texto '≅'
        self.botaoArredondar = Button(
            self.janela,
            text='≅',
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__arredondar
        )

        # Criando um botão funcional com o texto 'xʸ''
        self.botaoDeriv = Button(
            self.janela,
            text="xʸ'",
            fg=self.__corBotaoTexto,
            bg='light coral',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__deriv
        )

        # Criando um botão funcional com o texto '?'
        self.botaoManual = Button(
            self.janela,
            text='?',
            fg=self.__corBotaoTexto,
            bg='DeepPink2',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__manual
        )

        # Criando um botão funcional com o texto 'Sin'
        self.botaoSin = Button(
            self.janela,
            text='Sin',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__sin
        )

        # Criando um botão funcional com o texto 'Cos'
        self.botaoCos = Button(
            self.janela,
            text='Cos',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__cos
        )

        # Criando um botão funcional com o texto 'Tan'
        self.botaoTan = Button(
            self.janela,
            text='Tan',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__tan
        )

        # Criando um botão funcional com o texto 'Rad' 
        self.botaoConverteRadianos = Button(
            self.janela,
            text='Rad',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__rad
        )

        # Criando um botão funcional com o texto 'Graus'  
        self.botaoConverteGraus = Button(
            self.janela,
            text='Graus',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__deg
        )

        # Criando um botão funcional com o texto 'Del'
        self.botaoDel = Button(
            self.janela,
            text='Del',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__del
        )

        # Criando um botão funcional com o texto 'Med'
        self.botaoMedia = Button(
            self.janela,
            text='Med',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__media
        )

        # Criando um botão funcional com o texto 'DP'
        self.botaoDesvioPadrao = Button(
            self.janela,
            text='Desvio P',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__desviopadrao
        )

        # Criando um botão funcional com o texto 'CDLXII'
        self.botaoRomanos = Button(
            self.janela,
            text='CLXVII',
            fg=self.__corBotaoTexto,
            bg='pale violet red',
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__romanos
        )
        
        # Posicionando os botões considerando um grid
        # com 9 linhas e 5 colunas
        # Seguindo a mesma ordem em que os botoẽs foram definidos
        # e condizendo com a proximidade entre eles no layout

        #Números
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
        self.botaoMais            .grid(row=2, column=3)
        self.botaoMenos           .grid(row=3, column=3)
        self.botaoVezes           .grid(row=4, column=3)
        self.botaoDivisao         .grid(row=5, column=3)
        self.botaoPonto           .grid(row=5, column=0)
        self.botaoIgual           .grid(row=5, column=2)
        self.botaoParenteses1     .grid(row=6, column=0)
        self.botaoParenteses2     .grid(row=6, column=1)
        self.botaoElevado         .grid(row=6, column=2)
        self.botaoLimpar          .grid(row=6, column=3)
        self.botaoFatorial        .grid(row=7, column=0)
        self.botaoLn              .grid(row=7, column=1)
        self.botaoPi              .grid(row=7, column=2)
        self.botaoEulerNumber     .grid(row=7, column=3)
        self.botaoFracao          .grid(row=8, column=0)
        self.botaoRaiz            .grid(row=8, column=1)
        self.botaoArredondar      .grid(row=8, column=2)
        self.botaoDeriv           .grid(row=8, column=3)
        self.botaoManual          .grid(row=0, column=4)
        self.botaoSin             .grid(row=2, column=4)
        self.botaoCos             .grid(row=3, column=4)
        self.botaoTan             .grid(row=4, column=4)
        self.botaoConverteRadianos.grid(row=5, column=4)
        self.botaoConverteGraus   .grid(row=6, column=4)
        self.botaoDel             .grid(row=7, column=4)
        self.botaoMedia           .grid(row=8, column=4)
        self.botaoDesvioPadrao    .grid(row=9, column=4)
        self.botaoRomanos         .grid(row=9, column=3)
            
        return None

    # Definição dos métodos dos botões, como as funções de cada um vão funcionar
    # Seguindo a mesma ordem em que os botoẽs foram definidos, condizendo com a
    # proximidade entre eles no layout e a ordem em que ficou anotado o posicionamento
    # considerando um grid com 9 linhas e 5 colunas

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
            expressao = self.expressao.replace('x','*').replace('÷','/').replace('π','pi').replace('^', '**')

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
            # Criando arquivo que registra a cada linha o historico de cálculo, com a conta
            # e o resultado toda vez que uma conta for feita
            histórico = open('histórico.txt','a')
            histórico.write(expressao)
            histórico.write('=')
            histórico.write(f'{self.conteudoCaixa.get()}\n')
            histórico.close()
            
            # Verificando se houve erro
            if houveErro:
                # Limpando a expressao na memória
                self.expressao = ''

                # Informando erro na caixa
                self.conteudoCaixa.set('Vish, deu ruim... Tenta de novo!')
            else:
                # Faça nada
                pass

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

    # Método Privado
    def __fatorial(
        self : object,
        event: 'Event' = None
        ):
        'Devolve o fatorial do numero'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        self.conteudoCaixa.set(factorial(float(self.expressao)))
        self.expressao=str(factorial(float(self.expressao)))
        return None
    
    # Método Privado
    def __log(
        self : object,
        event: 'Event' = None
        ):
        'Devolve o log do numero'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        self.conteudoCaixa.set(log(float(self.expressao)))
        self.expressao=str(log(float(self.expressao)))
        return None

    # Método Privado
    def __fracao(
        self : object,
        event: 'Event' = None
        ):
        '''Faz o resultado de uma divisão aparecer no formato de fração,
        apenas simplifica usando o maior denominador em comum'''
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        nova=[]
        listaemstr = str(self.expressao).split('÷')
        for i in listaemstr:
            nova.append(float(i))
        divisor=gcd(nova[0],nova[1])
        fracao=float(nova[0]/divisor),'/',float(nova[1]/divisor)
        self.conteudoCaixa.set(fracao)
        return None
 
    # Método Privado
    def __arredondar(
        self : object,
        event: 'Event' = None
        ):
        'Arredonda o valor'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        
        # Condiçao para caso o usuario queira arredondar o resultado decimal de uma
        # transformacao de grau pra radiano, uma vez que essa funçao fornece 2 resultados
        if 'ou' in self.conteudoCaixa.get():
            string = self.conteudoCaixa.get()
            partida=string.split(' ')
            numero=partida[0]
            final=numero[1:-1]
            self.expressao=float(final)
            arredondado=round(self.expressao,1)
            self.expressao=str(arredondado)
            self.conteudoCaixa.set(self.expressao)
        # Qualquer outro arredondamento
        else:
            string = self.conteudoCaixa.get()
            self.expressao=float(string)
            arredondado=round(self.expressao,1)
            self.expressao=str(arredondado)
            self.conteudoCaixa.set(self.expressao)
        return None

    def __deriv(
        self : object,
        event: 'Event' = None
        ):
        'Retorna a derivada exponencial, sem mostrar alguma icognita '
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        string=self.expressao.split('^')
        numero1=float(string[0])
        numero2=float(string[2])
        resultado=str(numero1*numero2)
        potenciafinal=str(numero2-1)
        self.conteudoCaixa.set(resultado+'^'+potenciafinal)
        
        return None

    # Método Privado
    def __manual(
        self : object,
        event: 'Event' = None
        ):
        'Exibe uma janela explicando as funções da calculadora'

        # Abrindo janela com o diálogo
        decisao = messagebox.showinfo(
            'Manual',
            '''Olá! Dúvidas? Veja se isso ajuda:\n\nDica -> Para todas as funções,
você pode seguir calculando com o resultado, contanto que sejam cálculos simples (sem usar outras
funções)\n\nSin, Cos e Tan: É só digitar o número e clicar no botão, eu te dou o resultado\n
Rad: Posso te dar o radiano do grau digitado na forma decimal ou em função de π, você escolhe\n
Graus: Transformo de radiano para grau, é só clicar, pode escrever em decimal ou como π/x que eu vou
entender\n\nMed: Digite assim '1+2+3+...+n' e clique, que eu faço a média pra você\n
CLXVII: Transformo o número em algaritmo romano\n\n√ e xʸ: Eu só preciso que você
escreva antes o número você quer tirar a raiz ou elevar, depois a potência da raiz ou o expoente e
feche os parenteses\n\nX/Y: Simplifico frações\n\nxʸ': Dou a derivada exponencial, é
só usar o botão xʸ, e clicar''')
        return None
    # Método Privado
    def __sin(
        self : object,
        event: 'Event' = None
        ):
        'Transforma o grau dado em radianos e devolve o sin'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        self.expressao=float(self.expressao)
        nova=radians(self.expressao)
        seno=sin(radians(self.expressao))
        self.expressao=str(seno)
        self.conteudoCaixa.set(self.expressao)
        
        return None

    # Método Privado
    def __cos(
        self : object,
        event: 'Event' = None
        ):
        'Transforma o grau dado em radianos e devolve o cos'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        self.expressao=float(self.expressao)
        nova=radians(self.expressao)
        cose=cos(nova)
        self.expressao=str(cose)
        self.conteudoCaixa.set(self.expressao)
        
        return None

    # Método Privado
    def __tan(
        self : object,
        event: 'Event' = None
        ):
        'Transforma o grau dado em radianos e devolve a tan'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        self.expressao=float(self.expressao)
        nova=radians(self.expressao)
        tang=tan(nova)
        self.expressao=str(tang)
        self.conteudoCaixa.set(self.expressao)
        return None

    # Método Privado
    def __rad(
        self : object,
        event: 'Event' = None
        ):
        'Transforma o grau dado em radianos'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        radianosemdecimal=(radians(float(self.expressao)))
        # Para a funçao gcd nao pode ser float
        divisor=gcd(int(self.expressao),180)
        numeradorradianos=int(int(self.expressao)/divisor)
        radianos=str(numeradorradianos)
        final=radianosemdecimal,'ou',radianos+'π','/',int(180/divisor)
        self.conteudoCaixa.set(final)
        # Definindo que a expressao que vai continuar ali pro usuario seguir fazendo contas
        # direto, seja o resultado do radiano em decimais, pois é o que pode ser usado para
        # continuar a conta, tendo em vista que o valor é o mesmo
        self.expressao=str(radianosemdecimal)
        return None

    # Método Privado
    def __deg(
        self : object,
        event: 'Event' = None
        ):
        'Transforma o radianos dado em graus'
        # Usando float para transformar em números, pois float funciona para int
        # mas int não funciona se o usuário decidir mexer com float
        
        # Definindo uma maneira de resolver para caso o usuário digite
        # o radiano direto na forma mais comum: 'π/x'
        if 'π' in self.expressao:
            resultado=pi/float(self.expressao[2])
            self.conteudoCaixa.set(round(degrees(float(resultado))))
            self.expressao=str(degrees(float(resultado)))
        # Caso o usuário já saiba a forma decimal do radiano
        else:
            self.conteudoCaixa.set(round(degrees(float(self.expressao))))
            self.expressao=str(degrees(float(self.expressao)))
        return None

    # Método Privado
    def __del(
        self : object,
        event: 'Event' = None
        ):
        '''Apagar apenas o último caractere para não
        ter que apagar a função inteira a cada erro'''

        self.expressao = self.conteudoCaixa.get()
        for i in self.expressao:
            self.conteudoCaixa.set(self.expressao[:-1])
        self.expressao=self.expressao[:-1]
            
        return None

    # Método Privado
    def __media(
        self : object,
        event: 'Event' = None
        ):
        'Faz media da soma de numeros'
        #Usando float para transformar em números, pois float funciona para int
        #mas int não funciona se o usuário decidir mexer com float
        nova=[]
        listaemstr = str(self.expressao).split('+')
        for i in listaemstr:
            nova.append(float(i))
        self.conteudoCaixa.set(sum(nova)/len(nova)) 
        return None

    # Método Privado
    def __desviopadrao(
        self : object,
        event: 'Event' = None
        ):
        'Calcula o desvio padrão de uma lista dos números dados'
        #Usando float para transformar em números, pois float funciona para int
        #mas int não funciona se o usuário decidir mexer com float
        nova=[]
        listaemstr = str(self.expressao).split('+')
        for i in listaemstr:
            nova.append(float(i))
        self.conteudoCaixa.set(pstdev(nova)) 
        return None

    # Método Privado
    def __romanos(
        self : object,
        event: 'Event' = None
        ):
        'Transforma os numeros em numeros romanos'
        # Usando apenas int, pois a função de números romanos nao irá trabalhar com float
        num = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
        rom = ('M', 'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        resultado = []
        # Caso o usuário queira transformar um float
        if '.' in self.expressao:
            self.conteudoCaixa.set('Não esqueça de usar um número inteiro')
        elif 0 < int(self.expressao) < 4000:
            for i in range(len(num)):
                numero = int(self.expressao) / num[i]
                resultado.append(rom[i] * int(numero))
                self.expressao=int(self.expressao)
                self.expressao -= num[i] * int(numero)
            final = ''.join(resultado)
            self.conteudoCaixa.set(final)
            self.expressao=str(final)    
        else:
            self.conteudoCaixa.set('Aí não, né! Só posso com número <4000')
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
    def __definirAcoesTeclado(
        self: object
        ):
        'Definindo as ações de teclado'

        # Habilitando ENTER para resolver a equação
        self.janela.bind('<Return>', self.__resolveExpressao)

        # Habilitando ESC para fechar a janela
        self.janela.bind('<Escape>', self.__perguntarPraSair)

        # Habilitando BACKSPACE para limpar caixa de texto
        self.janela.bind('<BackSpace>', self.__del)


        return None

    # Método Público    
    def rodandoJanela(
        comprimento     : [int,float] = 320,
        altura          : [int,float] = 265,
        titulo          : str         = 'Calculadora',
        corFundo        : str         = 'pink',
        corTextoBotao   : str         = 'black',
        alturaBotao     : [int,float] = 1,
        comprimentoBotao: [int,float] = 4,
        myFile          : 'file'      = sys.stderr # sys.stderr: Texto no Shell Vermelho
                                                   # sys.stdout: Texto no Shell Azul
                                                   # yourFile  : Texto no Arquivo '.txt' dado
        ):
        'Executando janela e sua funções'

        # Criando uma instancia da janela base
        print('\n> Instanciando uma janela base', end='... ', file=myFile)
        self = JanelaBase()
        print('Funcionando',file=myFile)

        # Instanciando uma janela do Tkinter
        print('\n> Instanciando uma janela do Tkinter', end='... ', file=myFile)
        self.janela = Tk()
        print('Funcionando',file=myFile)

        # Definindo as configurações da janela gráfica
        print('\n> Configurado janela', end='... ', file=myFile)
        self.__configurarJanela(
            comprimento, altura, titulo, corFundo
        )
        print('Funcionando',file=myFile)

        # Definindo as configurações dos botões
        print('\n> Configurando botões',end='... ', file=myFile)
        self.__configurarBotao(
            corTextoBotao, alturaBotao, comprimentoBotao
        )
        print('Funcionando',file=myFile)

        # Criando os atributos necessários
        print('\n> Criando Atributos',end='... ', file=myFile)
        self.__criarAtributos()
        print('Funcionando',file=myFile)

        # Criando e posicionando os widgets na janela
        print('\n> Criando Widgets',end='... ', file=myFile)
        self.__criarWidgets()
        print('Funcionando',file=myFile)

        # Definindo ações de teclado
        print('\n> Definindo as ações de teclado',end='... ', file=myFile)
        self.__definirAcoesTeclado()
        print('Funcionando',file=myFile)

        # Rodando aplicação
        print('\n> Tudo rodando conforme o esperado, hora de calcular ;P', file=myFile)
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
    print('\nA calculadora está pronta para ser usada!\n')

    # Executando janela
    JanelaBase.rodandoJanela(
        myFile=open('log.txt','w')
    )

    # Informando fim do programa
    print('\n\nPrograma finalizado, até a próxima!\n')
