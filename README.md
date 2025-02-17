# Data Pipeline Project

Este projeto é um pipeline de dados que extrai, transforma e carrega dados de um banco de dados relacional e de serviços de nuvem AWS para o Google Cloud BigQuery. O workflow é programado para ser executado diariamente às 15:00 horas.

## Estrutura do Projeto

```
data-pipeline-project
├── src
│   ├── extract.py       # Funções para extração de dados
│   ├── transform.py     # Funções para transformação e limpeza de dados
│   ├── load.py          # Funções para carregamento de dados no BigQuery
│   ├── main.py          # Ponto de entrada do pipeline
│   └── utils
│       └── __init__.py  # Funções utilitárias
├── config
│   └── config.yaml      # Configurações do projeto
├── requirements.txt      # Dependências do projeto
├── Dockerfile            # Instruções para construção da imagem Docker
├── .gitignore            # Arquivos a serem ignorados pelo Git
└── README.md             # Documentação do projeto
```

## Instalação

1. Clone o repositório:
   ```
   git clone <URL_DO_REPOSITORIO>
   cd data-pipeline-project
   ```

2. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```

3. Configure as credenciais e parâmetros no arquivo `config/config.yaml`.

## Uso

Para executar o pipeline, utilize o seguinte comando:
```
python src/main.py
```

## Agendamento

O pipeline está configurado para ser executado diariamente às 15:00 horas. Certifique-se de que o ambiente de execução esteja configurado corretamente para suportar o agendamento.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.
