from transformers import pipeline

# Carregar o pipeline de perguntas e respostas
qa_pipeline = pipeline("question-answering")

# Contexto para as perguntas sobre o Microsoft Copilot Studio
contexto = """
O Microsoft Copilot Studio é uma ferramenta para criar e gerenciar chatbots personalizados. Ele permite
a criação de fluxos interativos para diversos tipos de assistentes virtuais. Ele foi projetado para ser
integrado com outras ferramentas de IA para aprimorar a performance dos bots.
Novidades no Microsoft Copilot Studio incluem integrações aprimoradas com o Azure e ferramentas de IA
para melhorar o desempenho do chatbot. O treinamento oferece recursos para aprender a criar chatbots e
personalizar fluxos, enquanto o conceito envolve a criação de assistentes virtuais inteligentes para
automatizar tarefas e interagir com os usuários. Caso enfrente problemas, consulte a documentação oficial
ou entre em contato com o suporte.
"""

# Função para exibir o menu de perguntas
def exibir_menu():
    """Exibe opções de perguntas de forma descontraída"""
    print("\nAgora que você já me conhece, o que você gostaria de saber sobre o Copilot Studio?")
    print("Aqui estão algumas opções:")
    print("1. O que é o Microsoft Copilot Studio?")
    print("2. Quais são as novidades no Microsoft Copilot Studio?")
    print("3. Como posso aprender a usar o Microsoft Copilot Studio?")
    print("4. O que é o conceito por trás do Copilot Studio?")
    print("5. Estou tendo problemas, o que posso fazer?")
    print("Digite 'sair' para encerrar a conversa.")

# Função para responder a pergunta de forma mais amigável
def responder_pergunta(opcao):
    """Responde de forma amigável às perguntas"""
    perguntas = {
        1: "O que é o Microsoft Copilot Studio?",
        2: "Quais são as novidades no Microsoft Copilot Studio?",
        3: "Como posso aprender a usar o Microsoft Copilot Studio?",
        4: "O que é o conceito por trás do Copilot Studio?",
        5: "Estou tendo problemas, o que posso fazer?"
    }
    
    respostas = {
        1: "Ah, o Microsoft Copilot Studio é uma plataforma super legal para criar chatbots personalizados! "
           "Você pode criar assistentes virtuais, construir fluxos interativos e integrar com ferramentas de IA "
           "para melhorar o desempenho do seu bot. Legal, né?",
        2: "As novidades são incríveis! Agora você pode integrar ainda mais com o Azure, o que dá um poder incrível "
           "para escalar seu chatbot. Também houve melhorias nas ferramentas de IA, tornando os bots mais inteligentes "
           "e interativos. Está demais!",
        3: "Você pode aprender tudo de forma super fácil com o treinamento do Copilot Studio! Ele te ensina a criar chatbots, "
           "personalizar fluxos e integrar ferramentas. Sem stress, é bem tranquilo e super acessível!",
        4: "O conceito é simples: criar assistentes virtuais inteligentes que ajudam a automatizar tarefas e interagir com "
           "os usuários de maneira fluida e eficiente. É basicamente a revolução dos bots no dia a dia!",
        5: "Se está com problemas, não se preocupe, tudo tem solução! Primeiro, dá uma olhada na documentação oficial, "
           "que pode ter uma resposta rápida. Se não resolver, o suporte técnico está aí para te ajudar com tudo o que for "
           "mais específico."
    }
    
    pergunta = perguntas.get(opcao)
    resposta = respostas.get(opcao)

    if not pergunta:
        return "Hmmm, não entendi muito bem. Pode escolher um número de 1 a 5 ou digitar 'sair' se quiser encerrar?"
    
    return resposta

# Função para controlar o fluxo de interação, incluindo introdução personalizada
def main():
    """Interação completa com o usuário de forma mais fluida"""
    print("👋 Olá, tudo bem? Eu sou o Scoob, seu chat Copilot! Estou aqui para te ajudar com o Microsoft Copilot Studio.")
    
    nome = input("Qual é o seu nome? ").strip()
    idade = input("Quantos anos você tem? ").strip()

    # Validação de gênero
    while True:
        genero = input("Qual é o seu gênero? (M para Masculino, F para Feminino, O para Outros): ").strip().upper()
        if genero in ['M', 'F', 'O']:
            if genero == 'M':
                genero_str = "Masculino"
            elif genero == 'F':
                genero_str = "Feminino"
            else:
                genero_str = "Outros"
            break
        else:
            print("Resposta inválida. Por favor, digite 'M' para Masculino, 'F' para Feminino ou 'O' para Outros.")

    print(f"\nPrazer em te conhecer, {nome}! 🎉")
    print(f"Com base nas suas respostas, você é {genero_str} e tem {idade} anos. Legal!")

    print("\nAgora vamos começar! O que você gostaria de saber sobre o Copilot Studio? Eu posso te ajudar com isso! 🤖")

    while True:
        exibir_menu()
        resposta = input("\nEscolha uma opção digitando o número correspondente ou digite 'sair' para finalizar a conversa: ").strip()

        if resposta.lower() == 'sair':
            print("\nFoi um prazer conversar com você, " + nome + "! Até a próxima! 👋😉")
            break

        try:
            opcao = int(resposta)
            resposta_pergunta = responder_pergunta(opcao)
            print(f"CopilotBot: {resposta_pergunta}\n")
        except ValueError:
            print("Ops! Não entendi, pode tentar novamente? Escolha um número de 1 a 5 ou digite 'sair'.")

if __name__ == "__main__":
    main()
