import schedule
import time
from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    data = extract_data()
    transformed_data = transform_data(data)
    load_data(transformed_data)

# Agendar a execução do pipeline diariamente às 15:00 horas
schedule.every().day.at("15:00").do(run_pipeline)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)