# Desafio Copilot - Fluxo de Conversa Personalizado
Entendendo o Desafio
O objetivo deste desafio é criar um Fluxo de Conversa Personalizado para interagir com o usuário e fornecer respostas sobre o Microsoft Copilot Studio. Embora o nome "Copilot" esteja presente, este projeto não foi desenvolvido no Microsoft Copilot Studio, mas sim inteiramente utilizando Python para criar um sistema de perguntas e respostas automatizado.

### Objetivos
Desenvolver um fluxo de conversa interativo em Python, onde o chatbot é capaz de responder a perguntas sobre o Microsoft Copilot Studio.
Gerenciar entradas e saídas do usuário, realizando validações e fornecendo respostas com base nas opções escolhidas.
Simular um sistema de chatbot que, embora não esteja integrado ao Microsoft Copilot Studio, simula um fluxo de conversa de maneira eficiente com perguntas e respostas predefinidas.
Como Funciona
O fluxo de conversa funciona através de um menu interativo onde o usuário escolhe uma pergunta, e o sistema responde com uma informação pré-programada sobre o Microsoft Copilot Studio.

Este projeto tem como objetivo criar um assistente virtual interativo, que pode fornecer informações úteis de forma intuitiva e agradável.

### Funcionalidades

Interação com o usuário de maneira natural.

Perguntas sobre o Microsoft Copilot Studio, como o que é, novidades, treinamento, conceito e solução de problemas.
Perguntas personalizadas de usuário, como nome, idade e gênero.
Respostas dinâmicas baseadas em um contexto predefinido.
Integração com o Hugging Face Transformers para processamento de linguagem natural.

### Requisitos

Antes de rodar o projeto, é necessário ter algumas bibliotecas e ferramentas instaladas no seu ambiente. Seguem os requisitos:

Python 3.8 ou superior.
Pip (gerenciador de pacotes do Python).
Ambiente Virtual (recomendado, mas não obrigatório).
Instalação
Passo 1: Clonar o Repositório
Primeiro, clone o repositório do projeto para sua máquina local.

bash
Copiar
git clone https://github.com/seu-usuario/copilot-chatbot.git
cd copilot-chatbot
Passo 2: Criar e Ativar um Ambiente Virtual (opcional, mas recomendado)
Para manter as dependências do projeto isoladas, é altamente recomendável usar um ambiente virtual.

python -m venv venv
No Windows:

Copiar
source venv/bin/activate

### Passo 3: Instalar Dependências

Com o ambiente virtual ativado (ou não, se preferir instalar globalmente), instale as dependências necessárias:

Copiar
pip install -r requirements.txt
Aqui está o conteúdo do arquivo requirements.txt:

Copiar
transformers==4.49.0
torch
transformers: Para integrar com modelos da Hugging Face para perguntas e respostas.
torch: Requisito para o uso de modelos pré-treinados do Hugging Face.

### Configuração

Não há configuração adicional necessária. O script já está pronto para rodar, mas caso queira alterar o comportamento do chatbot, você pode editar o arquivo copilot.py.

### Como Usar
1. Executar o ChatBot
Com todas as dependências instaladas, basta rodar o script copilot.py para iniciar o chatbot. O chatbot será iniciado e irá interagir com você.

python copilot.py

2. Interação
O chatbot iniciará a conversa com uma saudação e, em seguida, fará algumas perguntas para personalizar a interação. Ele irá coletar seu nome, idade e gênero para tornar a conversa mais personalizada.

Após a coleta das informações iniciais, você será apresentado com um menu de perguntas sobre o Microsoft Copilot Studio.

Exemplo de interação:

markdown
Copiar
Olá, tudo bem? Sou o Scoob, seu Copilot ChatBot! 😊
Qual é o seu nome?

João

Quantos anos você tem?

25

Qual é o seu gênero? (M: Masculino, F: Feminino, O: Outros)

M

Beleza, Sr. João! Seja bem-vindo ao Copilot Studio! 😄
Como posso te ajudar? Aqui estão algumas opções:
1. O que é o Microsoft Copilot Studio?
2. Novidades no Microsoft Copilot Studio?
3. Treinamento do Microsoft Copilot Studio
4. Conceito
5. Solucionar problemas
Digite 'sair' para encerrar a conversa.

Escolha o número da pergunta ou digite 'sair' para terminar: 1

Scoob: O Microsoft Copilot Studio é uma ferramenta para criar e gerenciar chatbots personalizados...
O chatbot continuará respondendo às suas perguntas até que você decida sair digitando 'sair'.

Estrutura do Projeto
copilot-chatbot/
│

├── copilot.py             # Script principal para rodar o ChatBot

├── requirements.txt       # Arquivo de dependências

└── README.md              # Este arquivo


### Contribuições


Se você deseja contribuir com o projeto, siga estas etapas:

Faça um fork deste repositório.
Crie uma nova branch (git checkout -b feature/nova-funcionalidade).
Faça as alterações necessárias e faça um commit (git commit -am 'Adicionando nova funcionalidade').
Envie para o repositório (git push origin feature/nova-funcionalidade).
Abra um pull request.
Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.

Agradecimentos
Hugging Face - Para os incríveis modelos de NLP.
PyTorch - Para a implementação de modelos de machine learning.
Você - Por contribuir para o avanço da inteligência artificial! 😊
