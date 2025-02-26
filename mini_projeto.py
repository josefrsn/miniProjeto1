import json

with open ('trilha\projetos\Cópia de movies_and_series.json') as file:
    data = json.load(file)

def escrever(n):
    arquivo = open('trilha\projetos\Parsing_de_Json_Jose.txt', 'a')
    arquivo.write(n)

# Primeira questão
filme = data.get('data', '')
filme_t = filme.get('movies', '')
filme = filme_t[0]
titulo_filme = filme.get('title', '')  

escrever('============================================\n')
escrever(f'1. Listar todos os títulos de filmes:\n{titulo_filme}\n')
escrever('============================================\n')

# Segunda questão
serie = data.get("data", '')
serie = serie.get('series', '')
serie = serie[0]
titulo_serie = serie.get('title', '')  

escrever(f'2. Listar todas as séries:\n{titulo_serie}\n')
escrever('============================================\n')

# Terceira questão
if serie.get('rating', '') > filme.get('rating', ''):
    maior_rating = serie.get('rating')
    escrever(f'3. Recuperar o filme/série com maior nota (rating):\n{titulo_serie}({maior_rating})\n')
    escrever('============================================\n')
else:
    maior_rating = filme.get('rating')
    escrever(f'3. Recuperar o filme/série com maior nota (rating):\n{titulo_filme}({maior_rating})\n')
    escrever('============================================\n')

# Quarta questão
generos_filme = filme.get('genres', '')
generos_serie = serie.get('genres', '')
generos = generos_serie

for i in range(len(generos_filme)):
    if generos_filme[i] not in generos_serie:
        generos.append(generos_filme[i])

escrever(f'4. Listar os gêneros de todos os filmes e séries:\n{generos}\n')
escrever('============================================\n')

# Quinta questão
total_filmes = []
total_series = []

total_filmes.append(titulo_filme)

f_anteriores_1 = filme.get('cast', '')[0].get('previousMovies', '')
f_anteriores_1 = f_anteriores_1[0].get('title', '')
total_filmes.append(f_anteriores_1)

f_anteriores_2 = filme.get('cast', '')[1].get('previousMovies', '')
f_anteriores_2 = f_anteriores_2[0].get('title', '')
total_filmes.append(f_anteriores_2)

nomiados_1 = filme.get('awards', '')
nomiados_1 = nomiados_1[0].get('nominees', '')
for i in nomiados_1:
    total_filmes.append(i)

total_series.append(titulo_serie)

s_anteriores_1 = serie.get('cast', '')[0].get('previousShows', '')
s_anteriores_1 = s_anteriores_1[0].get('title', '')
total_series.append(s_anteriores_1)

s_anteriores_2 = serie.get('cast', '')[1].get('previousShows', '')
s_anteriores_2 = s_anteriores_2[0].get('title', '')
total_series.append(s_anteriores_2)

nomiados_2 = serie.get('awards', '')
nomiados_2 = nomiados_2[0].get('nominees', '')
for i in nomiados_2:
    total_series.append(i)

total_midias = str(len(total_filmes) + len(total_series))

escrever(f'5. Obter o número total de filmes e séries:\n{total_midias}\n')
escrever('============================================\n')

# Sexta questão
streaming = []
def buscar_streaming(n: dict, st: list) -> list:
    for i in n.get('streaming', ''):
        st.append(i)
    return st

buscar_streaming(filme, streaming)
buscar_streaming(serie, streaming)

streaming = set(streaming)

escrever('6. Listar todas as plataformas de streaming disponíveis:\n')

for i in streaming:
    escrever(f'{i}\n')
escrever('============================================\n')

# Sétima questão
def disponível_em_4K(n: dict) -> bool:
    netflix = n.get('streaming', '')
    netflix = netflix.get('Netflix', '')
    resolucao = netflix.get('resolution', '')
    if '4K' in resolucao:
        return True

if disponível_em_4K(filme) == True and disponível_em_4K(serie) == True:
    escrever(f'7. Filtrar os filmes/séries disponíveis em 4K no Netflix:\n{titulo_filme}, {titulo_serie}.\n')
    escrever('============================================\n')

# Oitava questão
streaming_filme = []
streaming_serie = []

buscar_streaming(filme, streaming_filme)
buscar_streaming(serie, streaming_serie)
                 
url_filme = filme.get('streaming', '')
url_netflix_filme = url_filme.get('Netflix', '')
url_netflix_filme = url_netflix_filme.get('url', '')

if url_netflix_filme == '':
    url_netflix_filme = 'Não disponível'
    streaming_filme.remove('Netflix')

url_prime_filme = url_filme.get('Amazon Prime', '')
url_prime_filme = url_prime_filme.get('url', '')

if url_prime_filme == '':
    url_prime_filme = 'Não disponível'
    streaming_filme.remove('Amazon Prime')

url_serie = serie.get('streaming', '')
url_netflix_serie = url_serie.get('Netflix', '')
url_netflix_serie = url_netflix_serie.get('url', '')

if url_netflix_serie == '':
    url_netflix_serie = 'Não disponível'
    streaming_serie.remove('Netflix')

escrever('8. Identificar plataformas onde um filme específico está disponível:\n')
escrever(f'{titulo_filme} = {streaming_filme}, Netflix: {url_netflix_filme}, Amazon Prime: {url_prime_filme}\n')
escrever(f'{titulo_serie} = {streaming_serie}, Netflix: {url_netflix_serie}, Amazon Prime: Não disponível\n')
escrever('============================================\n')

#Nona questão
personagens_atores = {}
cast_filme = filme.get('cast', '')
cast_serie = serie.get('cast', '')

def elenco(n: list, p_v: str, s_v: str, d: dict) -> dict:
    for i in n:
        d[i.get(p_v, '')] = i.get(s_v, '')
    return d

elenco(cast_filme, 'actor', 'character', personagens_atores)
elenco(cast_serie, 'actor', 'character', personagens_atores)

escrever('9. Listar todos os atores e os personagens que interpretam:\n')
for i, j in personagens_atores.items():
    escrever(f'{i}, interpretou: {j}\n')
escrever('============================================\n')

#Décima questão
salario_atores = {}

elenco(cast_filme, 'salary', 'actor', salario_atores)
elenco(cast_serie, 'salary', 'actor', salario_atores)

escrever('10. Obter o ator com maior salário em um filme ou série:\n')
for i, j in salario_atores.items():
    if i == max(salario_atores):
        escrever(f'{j} teve o maior salário com {i}\n')
escrever('============================================\n')

#Décima primeira questão
locais = {}

producao = filme.get("production", "")
localizacao = producao.get('filmingLocations', '')
locais[f'Locais de {titulo_filme}'] = localizacao

escrever(f'11. Listar todas as localizações de filmagem dos filmes:\n')
for i, j in locais.items():
    escrever(f'{i}: {j}\n')
escrever('============================================\n')

#Décima segunda questão
diretores = filme.get('directors', '')

escrever('12. Listar os diretores de cada filme:\n')
escrever(f'{diretores[0]} é o diretor do filme: {titulo_filme}\n')
escrever('============================================\n')

#Décima terceira questão
d_revenue = {}
caixa = producao.get('boxOffice', '')
revenue = caixa.get('revenue', '')
d_revenue[titulo_filme] = revenue

for i, j in d_revenue.items():
    escrever(f'13. Obter o filme com maior receita na bilheteria (revenue):\n{i}: {j}\n')
escrever('============================================\n')

#Décima quarta questão
profit = caixa.get('profit', '')
mediaProfit = profit / len(filme_t)

escrever(f'14. Calcular o lucro médio dos filmes:\nA média é igual a : {mediaProfit}\n')
escrever('============================================\n')

#Décima quinta questão
vendas = caixa.get('ticketSales', '')

escrever('15. Obter a distribuição de vendas de ingressos por região:\n')
for i, j in vendas.items():
    escrever(f'{i}: {j}\n')
escrever('============================================\n')

#Décima sexta questão
premios_filme = {}
premios_serie = {}

def premios(n: dict,d: dict) -> dict:
    awards = n.get('awards', '')
    for i in range(len(awards)):
        d['Ano'] = awards[i].get('year', '')
        d['Prêmio'] = awards[i].get('award', '') 
        d['Categoria'] = awards[i].get('category', '')
    return d

premios(filme, premios_filme)
premios(serie, premios_serie)

escrever(f'{premios_filme}, {premios_serie}')



