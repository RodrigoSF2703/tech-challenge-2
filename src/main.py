import requests
import datetime
import os
import zipfile
from upload_to_s3 import upload_to_s3


def download_and_extract():
    # Obtém a data atual no formato YYYYMMDD
    data_atual = datetime.datetime.now().strftime("%Y-%m-%d")

    # Monta a URL com a data atual
    url = f"https://arquivos.b3.com.br/apinegocios/tickercsv/{data_atual}"

    # Faz a requisição HTTP
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Salva o conteúdo em um arquivo local
        caminho_arquivo_zip = f"dados_b3_{data_atual}.zip"
        with open(caminho_arquivo_zip, "wb") as arquivo_zip:
            arquivo_zip.write(response.content)

        print(f"Arquivo zipado salvo em {os.path.abspath(caminho_arquivo_zip)}")

        # Descompacta o arquivo
        pasta_destino = "dados_b3_descompactados"
        with zipfile.ZipFile(caminho_arquivo_zip, "r") as zip_ref:
            zip_ref.extractall(pasta_destino)

        print(f"Arquivo descompactado salvo em {os.path.abspath(pasta_destino)}")

        # Caminho local do arquivo descompactado
        local_file_path = os.path.join(pasta_destino, "seu_arquivo.txt")
        # Nome do bucket S3
        bucket_name = "seu-bucket-s3"
        # Caminho dentro do bucket
        s3_key = "caminho/dentro/do/bucket/arquivo.txt"

        # Chama a função para fazer o upload
        upload_to_s3(local_file_path, bucket_name, s3_key)
    else:
        print("Erro ao baixar o arquivo. Verifique a URL ou a conexão.")
        # Encerra o script
        raise SystemExit("Script encerrado devido a erro na URL")


if __name__ == "__main__":
    download_and_extract()
