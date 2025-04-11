import os
import tkinter as tk
from tkinter import messagebox

def renomear_arquivos():
    data = entrada_data.get()

    if not data:
        messagebox.showerror("Erro", "Por favor, insira a data!")
        return

    caminho_pasta = r'C:\Users\Filipe\Desktop\Filipe\pasta_teste'

    numeros_conta = [
        '353452475',
        '35344498',
        '123456789',
        '987654321',
        '112233445',
        '556677889',
        '998877665',
        '443322110',
        '667788990',  # conta só corrente
        '776655443',
        '221100334'
    ]

    conta_so_corrente = '667788990'

    arquivos_extrato = [
        f for f in os.listdir(caminho_pasta)
        if 'extrato' in f.lower() and os.path.isfile(os.path.join(caminho_pasta, f))
    ]

    arquivos_extrato.sort(key=lambda f: os.path.getmtime(os.path.join(caminho_pasta, f)))
    arquivo_index = 0

    for conta in numeros_conta:
        if arquivo_index >= len(arquivos_extrato):
            break

        nome_corr = arquivos_extrato[arquivo_index]
        ext_corr = os.path.splitext(nome_corr)[1]
        novo_nome_corr = f'Banestes_conta_corr_{conta}_{data}{ext_corr}'

        antigo_corr = os.path.join(caminho_pasta, nome_corr)
        novo_corr = os.path.join(caminho_pasta, novo_nome_corr)
        os.rename(antigo_corr, novo_corr)
        print(f'✅ Renomeado: {nome_corr} → {novo_nome_corr}')
        arquivo_index += 1

        if conta == conta_so_corrente:
            continue

        if arquivo_index >= len(arquivos_extrato):
            break

        nome_aplic = arquivos_extrato[arquivo_index]
        ext_aplic = os.path.splitext(nome_aplic)[1]
        novo_nome_aplic = f'Banestes_conta_aplic_{conta}_{data}{ext_aplic}'

        antigo_aplic = os.path.join(caminho_pasta, nome_aplic)
        novo_aplic = os.path.join(caminho_pasta, novo_nome_aplic)
        os.rename(antigo_aplic, novo_aplic)
        print(f'✅ Renomeado: {nome_aplic} → {novo_nome_aplic}')
        arquivo_index += 1

    messagebox.showinfo("Concluído", "Todos os arquivos foram renomeados com sucesso!")

# Interface gráfica
janela = tk.Tk()
janela.title("Renomeador de Extratos")

tk.Label(janela, text="Digite a data (ex: 09_04_2025):").pack(pady=5)
entrada_data = tk.Entry(janela, width=20)
entrada_data.pack(pady=5)

botao_executar = tk.Button(janela, text="Renomear Arquivos", command=renomear_arquivos)
botao_executar.pack(pady=10)

janela.mainloop()
