# WebSocket com Sessão - Fabio Thomaz

Este projeto é um exemplo prático de comunicação via WebSocket, onde o cliente pode se registrar com um ID de sessão e, em seguida, enviar e receber mensagens usando WebSockets. O servidor HTTP permite registrar um ID de sessão, e o WebSocket permite comunicação em tempo real.

## Funcionalidade

- **Servidor HTTP**: Permite registrar um ID de sessão através de uma requisição GET.
- **Servidor WebSocket**: Cada cliente se conecta a um WebSocket utilizando seu ID de sessão registrado. A comunicação é bidirecional — o cliente envia mensagens ao servidor, e o servidor retorna as mensagens com o ID da sessão para identificação.
- **Frontend (HTML/JS)**: A interface de cliente permite que o usuário registre uma sessão, se conecte via WebSocket e envie mensagens em tempo real.

---

## Arquitetura

### Servidor

O servidor é dividido em duas partes:

1. **HTTP Server (aiohttp)**: 
   - Rota `/stream?id=ID` que permite o registro do ID de sessão.
   - O servidor mantém um conjunto de IDs válidos de sessões, garantindo que somente os clientes com IDs registrados possam se conectar via WebSocket.
   
2. **WebSocket Server (websockets)**: 
   - O servidor WebSocket aceita conexões nas URLs `ws://localhost:8765/ws/{ID}`, onde `{ID}` é o ID de sessão registrado.
   - As mensagens enviadas pelo cliente são recebidas e enviadas de volta, precedidas pelo ID da sessão para garantir a identificação.

### Cliente

O cliente é uma página HTML com JavaScript que permite:

- Registrar um ID de sessão através do HTTP.
- Conectar-se ao servidor WebSocket com o ID de sessão.
- Enviar e receber mensagens em tempo real.

A interface utiliza o framework **Bootstrap 5** para um design responsivo e estilizado.

---

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `aiohttp`
  - `websockets`

### Instalação

1. **Instalar dependências:**

   Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

   Instale as dependências:

   ```bash
   pip install aiohttp websockets
   ```

2. **Executar o servidor:**

   Inicie o servidor rodando o script Python `server.py`:

   ```bash
   python server.py
   ```

   O servidor estará escutando na porta `8080` para HTTP (registro de sessão) e na porta `8765` para WebSockets (comunicação em tempo real).

---

## Estrutura de Arquivos

```
├── server.py              # Servidor WebSocket + HTTP
├── index.html             # Interface HTML do cliente
└── README.md              # Este arquivo
```

---

## Como Usar

1. **Iniciar o Servidor:**

   Certifique-se de que o servidor está rodando:

   ```bash
   python server.py
   ```

2. **Registrar Sessão:**

   Abra o arquivo `index.html` no navegador. No campo "ID da Sessão", insira um ID exclusivo (exemplo: `0101`), e clique em **Registrar Sessão**. O servidor irá registrar o ID.

3. **Conectar ao WebSocket:**

   Após registrar o ID da sessão, clique em **Conectar WebSocket**. O cliente se conectará ao servidor WebSocket usando o ID registrado. Quando conectado, você poderá enviar mensagens.

4. **Enviar Mensagens:**

   Digite uma mensagem no campo "Mensagem" e clique em **Enviar**. A mensagem será enviada para o servidor e, em seguida, o servidor retornará a mensagem com o ID da sessão, permitindo que o cliente veja as mensagens recebidas.

5. **Status:**

   O status de conexão e de envio/recebimento de mensagens será exibido abaixo do campo de mensagens.

---

## Detalhamento do Código

### `server.py`

Este é o servidor principal, que contém dois componentes:

1. **HTTP Server (aiohttp)**:
   - A função `register_session` recebe um ID de sessão como parâmetro na URL (`?id={ID}`) e o registra em um conjunto `sessions`.
   - Este servidor escuta na porta `8080` para registrar os IDs de sessão.

2. **WebSocket Server (websockets)**:
   - A função `ws_handler` aceita conexões WebSocket nas URLs `ws://localhost:8765/ws/{ID}`.
   - O WebSocket é estabelecido apenas se o ID fornecido na URL estiver presente no conjunto `sessions`.
   - Após a conexão, o servidor pode enviar e receber mensagens do cliente.

### `index.html`

A interface do cliente, que usa **Bootstrap 5** para estilo. Contém:

- Um campo para registrar um ID de sessão.
- Botões para registrar a sessão e conectar ao WebSocket.
- Um campo de texto para enviar mensagens.
- Uma área para exibir o status e as mensagens recebidas do servidor.

### Comunicação

- Quando o cliente registra um ID de sessão, o servidor HTTP valida o ID.
- Quando o cliente se conecta ao WebSocket, a comunicação é feita em tempo real. As mensagens enviadas pelo cliente são prefixadas com o ID da sessão para identificar de qual cliente as mensagens estão vindo.
  
---

## Possíveis Melhorias

- **Validação mais robusta de IDs**: Atualmente, os IDs são apenas strings simples. Seria interessante adicionar um sistema de validação para garantir que o formato dos IDs esteja correto.
- **Persistência de sessões**: Usar um banco de dados ou arquivo para persistir as sessões registradas, garantindo que não sejam perdidas quando o servidor for reiniciado.
- **Interface mais interativa**: Melhorar a interface com funcionalidades como histórico de mensagens, notificações e mais interatividade.

---

## Conclusão

Este projeto serve como uma boa base para entender como WebSockets podem ser utilizados para comunicação em tempo real entre cliente e servidor, com o uso de sessões para garantir a comunicação personalizada com os clientes. Você pode expandir este projeto conforme necessário para incluir mais funcionalidades como autenticação, histórico de mensagens, e muito mais.