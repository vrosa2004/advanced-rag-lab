# 🐘 Dia 3: Persistência Vetorial com PostgreSQL e pgvector

Este diretório contém o laboratório prático do terceiro dia. O objetivo principal deste exercício é tirar o cálculo matemático da memória RAM do computador (como fizemos nos dias 1 e 2) e delegá-lo para um **Banco de Dados Vetorial** real utilizando PostgreSQL (Supabase) com a extensão `pgvector`.

## 🎯 Resumo do Aprendizado

Nesta etapa, evoluímos a arquitetura do nosso RAG ao introduzir um banco de dados e aplicar boas práticas de Engenharia de Software:

1. **Persistência com `pgvector`:** Aprendemos a habilitar e utilizar o tipo nativo `vector(384)` no PostgreSQL. Ele é projetado especificamente para armazenar e indexar matrizes numéricas complexas geradas por IA.
2. **Padrão Repository (Separação de Responsabilidades):** Estruturamos o projeto para não criar "código espaguete":
   * `database.py`: Cuida exclusivamente de conectar e configurar a infraestrutura.
   * `repository.py`: Centraliza todos os comandos e lógicas SQL (Criar tabela, Inserir, Buscar).
   * `main.py`: Funciona como o orquestrador, unindo o modelo de Inteligência Artificial e as operações do banco.
3. **Idempotência (Prevenção de Duplicatas):** Implementamos uma rotina de checagem prévia (`select_document`) antes da inserção para garantir que o mesmo documento não seja vetorizado e salvo duas vezes, economizando armazenamento e poder de processamento.
4. **Cálculo de Distância no Banco (Operador `<=>`):** Na busca vetorial (`search_similar`), utilizamos o operador `<=>` do pgvector, que calcula a **Distância do Cosseno**. Para transformar a distância em "Score de Similaridade", executamos `1 - (distância)`. Os menores valores de distância representam a maior similaridade.

## 🗂️ Estrutura de Arquivos

```text
dia3/
├── .env              # Variáveis de ambiente contendo as credenciais do banco
├── database.py       # Fábrica de conexão com Supabase e registro da extensão pgvector
├── repository.py     # Padrão Repository contendo todas as querys SQL
└── main.py           # Script principal que orquestra os embeddings e a busca semântica
```

## 🚀 Como Executar

Certifique-se de estar no ambiente virtual do projeto e instale os pacotes de banco de dados e IA:

```bash
pip install numpy sentence-transformers psycopg2-binary python-dotenv pgvector
```

### Configuração do Banco de Dados
Antes de rodar, crie um arquivo chamado `.env` na pasta `dia3/` e insira a string de conexão do seu projeto Supabase:

```env
DATABASE_URL=postgresql://postgres.seuusurio:suasenha@aws-0-suaregiao.pooler.supabase.com:6543/postgres
```

### Rodando a Aplicação
Com o `.env` configurado, basta executar o orquestrador:

```bash
python main.py
```

### 💡 O que observar na saída do terminal:
Na primeira execução, o banco criará a tabela e inserirá todos os textos, convertendo-os em vetores. Nas execuções subsequentes, o código irá detectar que os textos já existem, pular a inserção de forma inteligente e ir direto para o ranqueamento (Retrieval) da sua pergunta!