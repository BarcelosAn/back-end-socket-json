
# Servidor HTTP com Socket e JSON em Python

Este projeto implementa um servidor HTTP simples usando sockets em Python, que responde com dados em formato JSON para diferentes rotas.

## 📁 Estrutura do Projeto

- `socket_json.py`: Implementa o servidor socket que escuta requisições HTTP e responde com dados JSON baseados na rota solicitada.
- `routes_json.py`: Define as rotas disponíveis e os dados associados a cada uma.


## 🚀 Como Executar

1. **Clone o repositório** ou copie os arquivos para seu ambiente local.
2. Certifique-se de estar na mesma rede do IP definido (ou ajuste o IP para `localhost` ou `127.0.0.1` se quiser testar localmente).
3. Execute o servidor:

```bash
python socket_json.py
```

4. Acesse as rotas usando um navegador ou ferramenta como `curl` ou `Postman`, com uma requisição do tipo **GET**.


## 🌐 Rotas Disponíveis

### `GET /`
- **Descrição:** Página inicial com uma mensagem de orientação.
- **Resposta:**
```json
"Escolha uma página"
```

### `GET /home`
- **Descrição:** Página principal.
- **Resposta:**
```json
{"Bem vindo a tela principal!"}
```

### `GET /users`
- **Descrição:** Lista de usuários.
- **Resposta:**
```json
{
  "Bruno": {
    "Sobrenome": "Barcelos",
    "Idade": 25
  },
  "Matheus": {
    "Sobrenome": "Lopes",
    "Idade": 23
  }
}
```

### `GET /carrinho`
- **Descrição:** Dados de um carrinho de compras.
- **Resposta:**
```json
{
  "carrinho": {
    "Banana": {
      "categoria": "Fruta",
      "valor": 10
    },
    "Açucar": {
      "categoria": "Cereal",
      "valor": 10
    },
    "Batata": {
      "categoria": "Verdura",
      "valor": "5"
    }
  }
}
```

### `GET /saudacao`
- **Descrição:** Mensagem de saudação.
- **Resposta:**
```json
"Olá Brasil!"
```

## ❌ Tratamento de Erros

Se uma rota não for reconhecida, o servidor responde com:

- **Status:** `404`
- **Corpo:**
```json
"Página não encontrada"
```


## 🔧 Detalhes Técnicos

- **IP/Porta padrão:** `127.0.0.1` (edite no `socket_json.py` se necessário).
- **Protocolo:** HTTP 1.1
- **Tipo de conteúdo:** `application/json`
- **Permissões CORS:** Origem `*` permitida.

## 🛠 Requisitos

- Python 3.x

Não há bibliotecas externas obrigatórias além das padrões (`socket`, `json`).


## 📌 Observações

- O servidor aceita uma conexão por vez (threading pode ser adicionado para múltiplas conexões simultâneas).
- Para testes locais, pode-se alterar `host = '127.0.0.1'`.


## 📄 Licença

Este projeto é open-source e pode ser utilizado livremente para fins educacionais.
```

Se quiser, posso gerar esse `README.md` como um arquivo para você baixar ou complementar com prints ou diagramas. Deseja isso?
