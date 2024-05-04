# Copie os nomes dos filmes em caixa alta para um novo arquivo

# def file_copy(origin, destiny):
#     try: 
#         with open("class-06-files/files/films.txt", "r+", encoding="utf-8") as list_origin:
#             movies = list_origin.read()

#         with open("class-06-files/files/upper_films.txt", "w+", encoding="utf-8") as list_destiny:
#             list_destiny.write(movies)  

#         print("Copia feita com sucesso")

#         with open(destiny, "r", encoding="utf-8") as destiny_file:
#             print(destiny_file.read())

#     except FileNotFoundError:
#         print("Arquivo não encontrado!")   

# origin = 'class-06-files/files/films.txt'       
# destiny = 'class-06-files/files/upper_films.txt' 

# file_copy(origin, destiny)

try:
    with open("class-06-files/files/films.txt", "r", encoding="utf-8") as films, \
        open("class-06-files/files/upper_films.txt", "w", encoding="utf-8") as upper_films:

        for film in films:
            upper_films.write(film.upper())
except FileNotFoundError:
    print("Arquivo não encontrado!")