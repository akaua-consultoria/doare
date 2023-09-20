# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 09:29:40 2023

@author: nfama
"""

import requests
import pandas as pd


def get_data(url):    
     
    page = 0  # Página inicial
    data = True  # Variável para verificar se há dados

    # Criar a tabela inicial vazia
    df = pd.DataFrame()

    while data:
        page_url = url + str(page)  # Constrói a URL completa para a página atual
        response = requests.get(page_url)  # Faz a solicitação HTTP para a página
        data = response.json()  # Converte a resposta JSON em um objeto Python
        
        
        df = pd.concat([df,pd.DataFrame(data)], ignore_index=True)
        page += 1
        print(page)
        
    print('Importação de dados concluída, total de linhas: ' + str(len(df)))
    
    return df