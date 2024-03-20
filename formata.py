# Abra o arquivo de texto
with open('saida.txt', 'r', encoding="utf-8") as file:
    # Leia o conteúdo do arquivo
    filmes = file.readlines()

# Remova quebras de linha e espaços em branco e crie a lista de filmes
lista_filmes = [filme.strip() for filme in filmes if filme.strip()]

# Crie a lista formatada
lista_formatada = [f'"{filme}"' for filme in lista_filmes]

# Imprima a lista formatada
print("[" + ",".join(lista_formatada) + "]")

with open("movies_data_formatada.txt", "w", encoding="utf-8") as txt_file:
    # Escreve o conteúdo do csv_data no arquivo
    txt_file.write("[" + ",".join(lista_formatada) + "]")

# Crie a lista formatada
#lista_formatada = ['filme' for _ in range(len(lista_filmes))]

# Imprima a lista formatada

