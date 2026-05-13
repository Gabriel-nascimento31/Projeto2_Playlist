class Musica: 
    def __init__(self, id_musica, titulo, artista, genero, bpm): 
        self.id = id_musica
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.bpm = bpm

    def exibir(self):
        print(f"""
ID: {self.id}
Título: {self.titulo}
Artista: {self.artista}
Gênero: {self.genero}
BPM: {self.bpm}
""")



class NodoLista: 
    def __init__(self, musica):
        self.musica = musica 
        self.proximo = None 



class Biblioteca: 
    def __init__(self):
        self.inicio = None 

    
    def adicionar(self, musica): 
        novo = NodoLista(musica)

        if self.inicio is None:
            self.inicio = novo
            return

        atual = self.inicio

        while atual.proximo:
            atual = atual.proximo

        atual.proximo = novo

    
    def remover(self, id_musica): 
        atual = self.inicio
        anterior = None

        while atual:
            if atual.musica.id == id_musica:

                
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                return True

            anterior = atual
            atual = atual.proximo

        return False

    
    def buscar_por_id(self, id_musica): 
        atual = self.inicio

        while atual:
            if atual.musica.id == id_musica:
                return atual.musica

            atual = atual.proximo

        return None

    
    def buscar_por_titulo(self, titulo): 
        atual = self.inicio

        while atual:
            if atual.musica.titulo.lower() == titulo.lower():
                return atual.musica

            atual = atual.proximo

        return None

    
    def listar(self): 
        if self.inicio is None:
            print("\nBiblioteca vazia.")
            return

        atual = self.inicio

        while atual:
            atual.musica.exibir()
            atual = atual.proximo

    
    def tamanho(self): 
        contador = 0
        atual = self.inicio

        while atual:
            contador += 1
            atual = atual.proximo

        return contador



class NodoFila: 
    def __init__(self, musica):
        self.musica = musica
        self.proximo = None



class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    
    def enqueue(self, musica):
        novo = NodoFila(musica)

        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo

        self.quantidade += 1

    
    def dequeue(self):
        if self.inicio is None:
            return None

        removido = self.inicio
        self.inicio = self.inicio.proximo

        if self.inicio is None:
            self.fim = None

        self.quantidade -= 1

        return removido.musica

    
    def exibir(self):
        if self.inicio is None:
            print("\nFila vazia.")
            return

        atual = self.inicio

        while atual:
            atual.musica.exibir()
            atual = atual.proximo

    
    def limpar(self):
        self.inicio = None
        self.fim = None
        self.quantidade = 0

    
    def tamanho(self):
        return self.quantidade




biblioteca = Biblioteca()

fila_relaxar = Fila()
fila_focar = Fila()
fila_animar = Fila()
fila_treinar = Fila()

historico = Fila()

proximo_id = 1



def montar_filas():
    fila_relaxar.limpar()
    fila_focar.limpar()
    fila_animar.limpar()
    fila_treinar.limpar()

    atual = biblioteca.inicio

    while atual:
        musica = atual.musica

        if musica.bpm <= 80:
            fila_relaxar.enqueue(musica)

        elif 81 <= musica.bpm <= 120:
            fila_focar.enqueue(musica)

        elif 121 <= musica.bpm <= 160:
            fila_animar.enqueue(musica)

        else:
            fila_treinar.enqueue(musica)

        atual = atual.proximo

    print("\nFilas de humor montadas com sucesso!")

def escolher_fila():
    print("""
1 - Relaxar
2 - Focar
3 - Animar
4 - Treinar
""")

    opcao = input("Escolha a fila: ")

    if opcao == "1":
        return fila_relaxar, "Relaxar"

    elif opcao == "2":
        return fila_focar, "Focar"

    elif opcao == "3":
        return fila_animar, "Animar"

    elif opcao == "4":
        return fila_treinar, "Treinar"

    else:
        return None, None


while True:

    print("""
==================================
 Playlist de Músicas
==================================

1 - Adicionar música
2 - Remover música
3 - Buscar música
4 - Listar biblioteca
5 - Montar filas de humor
6 - Reproduzir próxima
7 - Exibir fila de humor
8 - Exibir histórico
9 - Estatísticas
10 - Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        titulo = input("Título: ")
        artista = input("Artista: ")
        genero = input("Gênero: ")

        
        bpm = int(input("BPM: "))

        if bpm <= 0:
            print("BPM Inválido. BPM deve ser maior que zero")
            continue

        
            
        musica = Musica(
        proximo_id,
        titulo,
        artista,
        genero,
        bpm
        )

        biblioteca.adicionar(musica)

        print("\nMúsica adicionada com sucesso!")

        proximo_id += 1

    
    elif opcao == "2":

        try:
            id_musica = int(input("Digite o ID da música: "))
            
        except ValueError:
            print("ID inválido.")
            continue

        removido = biblioteca.remover(id_musica)

        if removido:
            print("Música removida com sucesso!")
        else:
            print("Música não encontrada.")

    
    elif opcao == "3":

        print("""
1 - Buscar por ID
2 - Buscar por título
""")

        tipo = input("Escolha: ")

        if tipo == "1":

            try:
                id_musica = int(input("ID: "))

            except ValueError:
                print("ID inválido.")
                continue

            musica = biblioteca.buscar_por_id(id_musica)

        elif tipo == "2":

            titulo = input("Título: ")

            musica = biblioteca.buscar_por_titulo(titulo)

        else:
            print("Opção inválida.")
            continue

        if musica:
            musica.exibir()
        else:
            print("Música não encontrada.")

    
    elif opcao == "4":
        biblioteca.listar()

    
    elif opcao == "5":
        montar_filas()

    
    elif opcao == "6":

        fila, nome = escolher_fila()

        if fila is None:
            print("Fila inválida.")
            continue

        musica = fila.dequeue()

        if musica is None:
            print("\nFila vazia.")
        else:
            print(f"\nReproduzindo da fila {nome}:")
            musica.exibir()

            historico.enqueue(musica)

    
    elif opcao == "7":

        fila, nome = escolher_fila()

        if fila is None:
            print("Fila inválida.")
            continue

        print(f"\nFila {nome}:")
        fila.exibir()

    
    elif opcao == "8":

        print("\nHistórico de reproduções:")
        historico.exibir()

    
    elif opcao == "9":

        print(f"""
======== ESTATÍSTICAS ========

Total na biblioteca: {biblioteca.tamanho()}

Fila Relaxar: {fila_relaxar.tamanho()}
Fila Focar: {fila_focar.tamanho()}
Fila Animar: {fila_animar.tamanho()}
Fila Treinar: {fila_treinar.tamanho()}

Total reproduzidas: {historico.tamanho()}
""")

    
    elif opcao == "10":

        print("\nEncerrando sistema...")
        break

    else:
        print("Opção inválida.")