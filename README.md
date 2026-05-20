readme_content = """# Sistema de Gerenciamento de Biblioteca 📚

Este projeto foi desenvolvido com o objetivo de resolver o problema de organização de uma biblioteca municipal, controlando de forma eficiente o ciclo de vida dos empréstimos de livros. A aplicação integra **Python** com o banco de dados **MySQL** para gerenciar transições de estado, manipulação de dados e cálculos complexos envolvendo datas.

---

## 📋 Cenário e Objetivo

A biblioteca enfrentava problemas de controle: livros sumindo, devoluções atrasadas sem registro e falta de visibilidade sobre o acervo. 

O sistema resolve isso gerenciando as seguintes etapas:
1. **Saída do livro:** Altera o status para `Emprestado` (indisponível).
2. **Decurso do prazo:** Monitora as datas de empréstimo e devolução prevista.
3. **Retorno do livro:** Altera o status de volta para `Disponivel`.
4. **Cálculo de pendências:** Identifica devoluções em atraso através de funções de data nativas do SQL.

---

## 🗄️ Modelo Relacional (Banco de Dados)

O banco de dados `biblioteca_db` é composto por 4 tabelas estruturadas da seguinte forma:

* **Autores:** `id_autor` (INT), `nome` (VARCHAR), `nacionalidade` (VARCHAR)
* **Livros:** `id_livro` (INT), `titulo` (VARCHAR), `genero` (VARCHAR), `id_autor` (INT), `status` (ENUM: 'Disponivel', 'Emprestado')
* **Membros:** `id_membro` (INT), `nome` (VARCHAR), `data_cadastro` (DATE)
* **Emprestimos:** `id_emprestimo` (INT), `id_membro` (INT), `id_livro` (INT), `data_emprestimo` (DATE), `data_devolucao_prevista` (DATE), `data_devolucao_real` (DATE, aceita valores `NULL`)

---

## 🚀 Funcionalidades Implementadas

O script Python executa consultas e análises estratégicas utilizando recursos avançados de SQL:

* **Relatório de Disponibilidade:** Lista todos os livros do acervo e seus respectivos status atuais.
* **Histórico Completo de Empréstimos:** Cruza dados das tabelas de Empréstimos, Membros e Livros utilizando `INNER JOIN` para exibir quem pegou qual livro e quando devolveu.
* **O Detetive (Análise de Acervo):** Identifica livros que nunca foram emprestados utilizando `LEFT JOIN` e filtrando onde a relação de empréstimo é `IS NULL`.
* **O Cobrador (Controle de Atrasos):** Utiliza a função `DATEDIFF` do MySQL para extrair a diferença exata de dias entre a devolução prevista e a devolução real, permitindo futuras lógicas de cálculo de multa.

---

## 🛠️ Tecnologias e Infraestrutura

* **Linguagem:** Python 3.x
* **Banco de Dados:** MySQL Server
* **Biblioteca Python:** `mysql-connector-python`