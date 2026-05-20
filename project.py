import mysql.connector as mysql
from datetime import date

connect = mysql.connect(
    host='localhost',
    user='root',
    password='',
    database='biblioteca_db')

cursor = connect.cursor()

#Relatório de disponibilidade, elenca os livros e se estão disponíves ou não
cursor.execute("SELECT titulo, status FROM Livros")
disponibilidade = cursor.fetchall()

for linha in disponibilidade:
    print(f"Livro: {linha[0]} - Status: {linha[1]}")

#Histórico de empréstimos
cursor.execute("SELECT Membros.nome, Livros.titulo, Emprestimos.data_emprestimo, Emprestimos.data_devolucao_real, Emprestimos.data_devolucao_prevista FROM"
               " Emprestimos"
               " INNER JOIN Membros ON Membros.id_membro = Emprestimos.id_membro"
               " INNER JOIN Livros ON Livros.id_livro = Emprestimos.id_livro"
               )
Historico = cursor.fetchall()
for i in range(len(Historico)):
    if Historico[i][3] == None:
        print(f"O membro {Historico[i][0]} pegou o livro '{Historico[i][1]}' na data {(Historico[i][2])} e deveria ter devolvido na data {Historico[i][4]}")
    else: print(f"O membro {Historico[i][0]} pegou o livro '{Historico[i][1]}' na data {(Historico[i][2])} e devolveu em {(Historico[i][3])}")

#Livros que não foram listados
cursor.execute("SELECT Livros.titulo FROM"
               " Livros"
               " LEFT JOIN Emprestimos ON Livros.id_livro = Emprestimos.id_livro"
               " WHERE Emprestimos.id_livro IS NULL")
nao_listado = cursor.fetchall()
for i in range(len(nao_listado)):
    print(f"O livro {nao_listado[i][0]} não foi emprestado")

#Emprestimos devolvidos com atraso
cursor.execute("SELECT Membros.nome," 
               " DATEDIFF(Emprestimos.data_devolucao_prevista, Emprestimos.data_devolucao_real) FROM"
               " Emprestimos"
               " INNER JOIN Membros ON Membros.id_membro = Emprestimos.id_membro"
               " WHERE Emprestimos.data_devolucao_real IS NULL")
emprestimos_em_atraso = cursor.fetchall()

for i in range(len(emprestimos_em_atraso)):
    if emprestimos_em_atraso[i][1] is not bool and int(emprestimos_em_atraso[i][1]) < 0:
        print(f"O membro {emprestimos_em_atraso[i][0]} está atrasado {-1 * int(emprestimos_em_atraso[i][1])} dias para a entrega do livro")
    elif int(emprestimos_em_atraso[i][1]) > 0:
        print(f"O membro {emprestimos_em_atraso[i][0]} devolveu o livro no tempo correto")
    else: print(f"O membro {emprestimos_em_atraso[i][0]} ainda não devolveu o livro")


cursor.close()
connect.close()