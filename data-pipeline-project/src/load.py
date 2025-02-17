import pandas as pd
from google.cloud import bigquery
import yaml

# Carregamento de dados
def load_data(data):
    # Carregar configurações do arquivo YAML
    with open('config/config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Configuração do cliente BigQuery
    client = bigquery.Client.from_service_account_json(config['bigquery']['service_account_json'])

    # Definindo a tabela de destino
    table_id = config['bigquery']['table_id']

    # Carregando os dados no BigQuery
    job = client.load_table_from_dataframe(data, table_id)

    # Espera o job terminar
    job.result()

    print(f'Dados carregados com sucesso na tabela {table_id}.')