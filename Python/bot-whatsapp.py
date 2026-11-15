print("==========")
print("Clínica")
print("==========")

nome = input("Qual seu nome: ")
print("Olá, seja bem vindo(a):  " + nome)
print("Como podemos te ajudar?")
opcao = input("Digite uma das opções abaixo: ")
print("1 - Agendar consulta")
print("2 - Cancelar consulta")
print("3 - Informações sobre a clínica")
if opcao == "1":
    print("Você escolheu agendar uma consulta.")
    data = input("Digite a data desejada (dd/mm/aaaa): ")
    hora = input("Digite o horário desejado (hh:mm): ")
    print("Consulta agendada para " + data + " às " + hora + ".")
elif opcao == "2":
    print("Você escolheu cancelar uma consulta.")
elif opcao == "3":
    print("Você escolheu obter informações sobre a clínica.")
else:
    print("Opção inválida. Por favor, escolha uma das opções disponíveis.")
    