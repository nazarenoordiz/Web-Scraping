import urllib.request, json
import pandas as pd
import csv
from Modulos.Funciones import replace_all



Informacion = []

with urllib.request.urlopen("https://playdata.starz.com/metadata-service/play/partner/Web_ES/v8/blocks?playContents=map&lang=es-ES&pages=MOVIES,SERIES&includes=contentId,contentType,title,actors,genres,seriesName,directors,seasonNumber,runtime,releaseYear,episodeCount,logLine,details") as url:
    
    data = json.loads(url.read().decode())

    play = data['blocks'][2]['playContentsById']
    for i in play:
        All_Data = data['blocks'][2]['playContentsById'][str(i)]
        Informacion.append(All_Data)
    with open('data.json', 'w') as outfile:

        json.dump(Informacion, outfile)
        
df = pd.read_json (r'.\data.json')
Column = ['Titulos', 'Tipo de Contenido','ID', 'Duración (segundos)', 'Año de Estreno', 'Sinopsis', 'Actores', 'Director/es', 'Generos', 'Episodios (Total)']
df.to_csv (r'.\data.csv', header=Column)
df_2 = pd.read_csv (r'.\data.csv')
New_Column = ['Titulos', 'Tipo de Contenido', 'Duración (segundos)', 'Año de Estreno', 'Sinopsis', 'Actores', 'Director/es', 'Generos', 'Episodios (Total)']
Pandas_csv = df_2[New_Column]
Pandas_csv = Pandas_csv.fillna("------")





replace_all(Pandas_csv, 'Actores', 'id', " ")
replace_all(Pandas_csv, 'Actores', 'fullName', " ")
replace_all(Pandas_csv, 'Actores', r'\d', " ")
replace_all(Pandas_csv, 'Actores', r'\W', " ")
Pandas_csv['Actores'] = Pandas_csv['Actores'].str.split()

replace_all(Pandas_csv, 'Director/es', 'id', " ")
replace_all(Pandas_csv, 'Director/es', 'fullName', " ")
replace_all(Pandas_csv, 'Director/es', r'\d', " ")
replace_all(Pandas_csv, 'Director/es', r'\W', " ")
Pandas_csv['Director/es'] = Pandas_csv['Director/es'].str.split()


replace_all(Pandas_csv, 'Generos', 'description', " ")
replace_all(Pandas_csv, 'Generos', r'\d', " ")
replace_all(Pandas_csv, 'Generos', r'\W', " ")
Pandas_csv['Generos'] = Pandas_csv['Generos'].str.split()



Pandas_csv.to_csv("data_Starz_Peliculas_Series.csv", index=False)



