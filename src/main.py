import requests
import datetime
from sanitize import Sanitize
import pandas as pd
import json

sanitizer = Sanitize()

def download_and_extract():
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")
    
    url = f"https://sistemaswebb3-listados.b3.com.br/indexProxy/indexCall/GetPortfolioDay/eyJsYW5ndWFnZSI6InB0LWJyIiwicGFnZU51bWJlciI6MSwicGFnZVNpemUiOjEyMCwiaW5kZXgiOiJJQk9WIiwic2VnbWVudCI6IjIifQ=="

    response = requests.get(url, verify=False)

    if response.status_code == 200:
        response = json.loads(response.content.decode()).get("results")
        df = pd.DataFrame(response)
        df = Sanitize.clean_df(df)
        df.to_parquet(f"data/b3_pregao_{data_atual}.parquet")
    else:
        print("Erro ao baixar o arquivo. Verifique a URL ou a conexão.")
        raise SystemExit("Script encerrado devido a erro na URL")


if __name__ == "__main__":
    download_and_extract()
