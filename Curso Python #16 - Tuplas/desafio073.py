print("Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.")
print(100 * "=")
print("Depois mostre:")
print(100 * "=")
print("A) Apenas os 5 primeiros colocados.")
print(100 * "=")
print("B) Os últimos 4 colocados da tabela.")
print(100 * "=")
print("C) Uma lista com os times em ordem alfabética.")
print(100 * "=")
print("D) Em que posição na tabela está o time da Chapecoense.")
print(100 * "=")

tabela_brasileirao = (
    ("Flamengo", 1),
    ("Atlético Mineiro", 2),
    ("Palmeiras", 3),
    ("Fortaleza", 4),
    ("Bragantino", 5),
    ("Corinthians", 6),
    ("Internacional", 7),
    ("Ceará", 8),
    ("Atlético Paranaense", 9),
    ("Santos", 10),
    ("Fluminense", 11),
    ("Juventude", 12),
    ("Sport", 13),
    ("Bahia", 14),
    ("São Paulo", 15),
    ("Cuiabá", 16),
    ("América Mineiro", 17),
    ("Grêmio", 18),
    ("Chapecoense", 19),
    ("Goiás", 20)
)

# A) Apenas os 5 primeiros colocados.
print(tabela_brasileirao[:5])
print(100 * "=")
# B) Os últimos 4 colocados da tabela.
print(tabela_brasileirao[-4:])
print(100 * "=")
# C) Uma lista com os times em ordem alfabética.
print(sorted(tabela_brasileirao))
print(100 * "=")
# D) Em que posição na tabela está o time da Chapecoense.
print(tabela_brasileirao[18])
print(100 * "=")
