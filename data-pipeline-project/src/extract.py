import pandas as pd
import sqlalchemy
import boto3

def extract_data():
    # Conexão com o banco de dados relacional
    db_connection_string = 'postgresql://user:password@host:port/database'
    engine = sqlalchemy.create_engine(db_connection_string)
    
    # Extraindo dados do banco de dados
    query = 'SELECT * FROM table_name'
    data = pd.read_sql(query, engine)
    
    # Conexão com AWS para extrair dados adicionais
    s3 = boto3.client('s3')
    bucket_name = 'your-bucket-name'
    file_key = 'path/to/your/file.csv'
    
    # Baixando arquivo do S3
    s3.download_file(bucket_name, file_key, 'local_file.csv')
    
    # Lendo dados do arquivo CSV
    additional_data = pd.read_csv('local_file.csv')
    
    # Combinando os dados extraídos
    combined_data = pd.concat([data, additional_data], ignore_index=True)
    
    return combined_data