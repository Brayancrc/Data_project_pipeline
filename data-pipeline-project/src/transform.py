import pandas as pd

def transform_data(data):
    # Limpeza de dados
    data.dropna(inplace=True)
    
    # Conversão de tipos de dados
    data['date'] = pd.to_datetime(data['date'])
    
    # Exemplo de junção de diferentes conjuntos de dados
    # data = data.merge(outra_base_de_dados, on='chave_comum', how='inner')
    
    return data