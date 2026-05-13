Projeto desenvolvido na Fatec Rio Claro, no curso de Inteligência Artificial, para a disciplina Estrutura de Dados.

O projeto consiste em um sistema de playlist. O sistema permite que o usuário gerencie sua biblioteca pessoal de músicas, monte filas de reprodução de acordo com humor e consulte o histórico de reprodução.

O sistema funciona da seguinte maneira:
Aparece o menu com as opções do sistema que são as seguintes:

1- Adicionar música: Permite ao usuário cadastrar uma música na biblioteca

2- Remover música: Permite ao usuário remover uma música da biblioteca pelo ID

3- Buscar música: Permite ao usuário buscar uma música na biblioteca, pode-se buscar de duas formas, pelo ID ou pelo título da música

4- Listar biblioteca: Lista todas as músicas cadastradas pelo usuário

5- Montar filas de humor: Monta as filas de humor de acordo com o BPM 
             Relaxar: 1 a 80 BPM
             Focar: 81 a 120 BPM
             Animar: 121 a 160 BPM
             Treinar: acima de 160 BPM

6- Reproduzir próxima: O usuário escolhe uma fila de humor e o sistema reproduz a música da fila escolhida pelo usuário, de acordo com a ordem do enfileiramento

7- Exibir fila de humor: O usuário escolhe uma fila de humor e o sistema exibi as músicas da fila escolhida pelo usuário

8- Exibir histórico: Mostra o histórico das músicas que foram reproduzidas

9- Estatísticas: Mostra o total de músicas cadastradas na biblioteca, o total de cada fila de humor e o total de músicas reproduzidas

10- Sair: Encerra o sistema



As estruturas de dados utilizadas no projeto foram:

Lista encadeada simples: Estrutura de dados linear que foi utilizada para gerenciar a biblioteca de músicas cadastradas

Filas: Estrutura de dados linear que foi utilizada para gerenciar as músicas de cada humor e o histórico das músicas reproduzidas


As estruturas de dados foram criadas manualmente(não foram utilizadas estruturas built-in do Python como List e Deque)


O projeto teve como objetivo entender programação orientada a objetos e aplicar as estruturas de dados criadas manualmente que foram Lista encadeada e Fila


Para rodar o projeto, clone o repositório e execute o arquivo app.py


Observação: O projeto não exige instalação de bibliotecas externas


