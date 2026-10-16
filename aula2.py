import yfinance
import pyautogui
from time import sleep
import pyperclip
import webbrowser

ticker = input("Digite o código da ação: ")
dt_inicial = input("Digite a data inicial (aaaa-mm-dd): ")
dt_final = input("Digite a data final (aaaa-mm-dd): ")

dados = yfinance.Ticker(ticker)
tabela = dados.history(start=dt_inicial, end=dt_final)

fechamento = tabela.Close

maximo = round(fechamento.max(),2)
minimo = round(fechamento.min(),2)
media = round(fechamento.mean(),2)

email = input("Digite o e-mail do destinatário: ")
assunto = f"Análises Projeto {ticker}"
mensagem = f"""Bom dia,

Seguem abaixo as análises da ação {ticker} do período solicitado: {dt_inicial} a {dt_final}:

Cotação máxima: R${maximo}
Cotação mínima: R${minimo}
Valor médio: R${media}
"""
pyautogui.PAUSE=3

webbrowser.open("www.gmail.com")
sleep(5)

pyautogui.click(x=144, y=214)

pyperclip.copy(email)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

pyautogui.click(x=1197, y=976)

pyautogui.hotkey("ctrl", "f4")
pyautogui.hotkey("alt", "f4")

print("E-mail enviado com sucesso!")