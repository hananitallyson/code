pontos = 0

print("\n1. Você costuma estudar com horário definido?")
primeira_pergunta = input("a) Sempre\nb) Às vezes\nc) Nunca\nReposta: ")

match primeira_pergunta:
    case 'a':
        pontos += 2
    case 'b':
        pontos += 1
    case 'c':
        pontos += 0

print("\n2. Quando recebe uma atividade, você:")
segunda_pergunta = input("a) Começa logo\nb) Deixa para depois, mas faz\nc) Só lembra no último momento\nReposta: ")

match segunda_pergunta:
    case 'a':
        pontos += 2
    case 'b':
        pontos += 1
    case 'c':
        pontos += 0

print("\n3. Você anota prazos e compromissos?")
terceira_pergunta = input("a) Sim\nb) Às vezes\nc) Não\nReposta: ")

match terceira_pergunta:
    case 'a':
        pontos += 2
    case 'b':
        pontos += 1
    case 'c':
        pontos += 0

print("\n4. Durante os estudos, você se distrai com facilidade?")
quarta_pergunta = input("a) Raramente\nb) Às vezes\nc) Frequentemente\nReposta: ")

match quarta_pergunta:
    case 'a':
        pontos += 2
    case 'b':
        pontos += 1
    case 'c':
        pontos += 0

if pontos >= 7:
    print(f"\nTotal de pontos: {pontos}\nPerfil muito organizado.\n")
elif pontos >= 4 and pontos <= 6:
    print(f"\nTotal de pontos: {pontos}\nPerfil moderadamente organizado.\n")
elif pontos < 4:
    print(f"\nTotal de pontos: {pontos}\nPerfil pouco organizado.\n")
