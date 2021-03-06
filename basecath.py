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
        ): #trecos
        'Criando e posicionando os widgets na janela'
        # Criando caixa para digitação de textos na janela
        # gráfica e direcionando seu conteúdo ao atributo
        # 'equação'
        self.caixaDaEquacao = Entry(
            self.janela, textvariable=self.conteudoCaixa,
            borderwidth=2
        )

        # Posicionando a caixa de texto considerando a
        # mescalgem de 4 colunas de espaço, tendo 70 px
        # de distância entre a borda desse espaço e a caixa
        self.caixaDaEquacao.grid(columnspan=4, ipadx=0)

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
            command=lambda:self.__adicionaValor(1),#funçao ĺambda: n preciso dar nome
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

        self.botaoParenteses1 = Button(
            self.janela,
            text='(',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('(')
        )

        self.botaoParenteses2 = Button(
            self.janela,
            text=')',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor(')')
        )

        self.botaoSin = Button(
            self.janela,
            text='Sin',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('sin(grau)')
        )

        self.botaoCos = Button(
            self.janela,
            text='Cos',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('cos(radians(')
        )

        self.botaoTan = Button(
            self.janela,
            text='Tan',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('tan(radians(')
        )
        self.botaoElevado = Button(
            self.janela,
            text='X²',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=lambda:self.__adicionaValor('**') 
        )

        self.botaoApagar = Button(
            self.janela,
            text='Del',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__limpar
        )

        self.botaoManual = Button(
            self.janela,
            text='?',
            fg=self.__corBotaoTexto,
            bg=self.__corBotaoBg,
            height=self.__alturaBotao,
            width=self.__comprimentoBotao,
            command=self.__manual
        )


        # Posicionando os botões considerando um grid
        # com 6 linhas e 4 colunas
        self.botao1           .grid(row=4, column=0)
        self.botao2           .grid(row=4, column=1)
        self.botao3           .grid(row=4, column=2)
        self.botao4           .grid(row=3, column=0)
        self.botao5           .grid(row=3, column=1)
        self.botao6           .grid(row=3, column=2)
        self.botao7           .grid(row=2, column=0)
        self.botao8           .grid(row=2, column=1)
        self.botao9           .grid(row=2, column=2)
        self.botao0           .grid(row=5, column=0)
        self.botaoPlus        .grid(row=2, column=3)
        self.botaoMinus       .grid(row=3, column=3)
        self.botaoMultiply    .grid(row=4, column=3)
        self.botaoDivide      .grid(row=5, column=3)
        self.botaoEqual       .grid(row=5, column=2)
        self.botaoClear       .grid(row=6, column=3)
        self.botaoDecimal     .grid(row=5, column=1)
        self.botaoParenteses1 .grid(row=6, column=0)
        self.botaoParenteses2 .grid(row=6, column=1)
        self.botaoSin         .grid(row=2, column=4)
        self.botaoCos         .grid(row=3, column=4)
        self.botaoTan         .grid(row=4, column=4)
        self.botaoElevado     .grid(row=6, column=2)
        self.botaoApagar      .grid(row=5, column=4)
        self.botaoManual      .grid(row=6, column=4)
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
    
    def __manual(
        self : object,
        event: 'Event' = None
        ):
        'Exibe uma janela perguntando se deseja fechar a janela'

        # Abrindo janela com o diálogo
        decisao = messagebox.showinfo(
            'Manual',
            'Olá! Dúvidas? Veja se isso ajuda:\n\nIsso: Assim\nAquilo: Assado\nFulano: De tal'
        )
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
            expressao = self.expressao.replace('x','*').replace('÷','/')
            expressao = self.expressao.replace('sin','sin(radians)')

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

            else: #nem precisava pq ele iria em frente
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
        comprimento     : [int,float] = 220,
        altura          : [int,float] = 180,
        titulo          : str         = 'Calculadora',
        corFundo        : str         = 'light blue',
        corFundoBotao   : str         = 'pink',
        corTextoBotao   : str         = 'black',
        alturaBotao     : [int,float] = 1,
        comprimentoBotao: [int,float] = 1,
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
