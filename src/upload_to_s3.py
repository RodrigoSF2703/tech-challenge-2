import boto3
import os


def upload_to_s3(local_file_path, bucket_name, s3_key):
    """
    Faz o upload de um arquivo local para um bucket S3.

    Args:
        local_file_path (str): Caminho local do arquivo a ser enviado.
        bucket_name (str): Nome do bucket S3.
        s3_key (str): Caminho dentro do bucket onde o arquivo será armazenado.
    """
    s3 = boto3.client("s3")
    try:
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"Arquivo {local_file_path} enviado para o bucket {bucket_name} com a chave {s3_key}")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o S3: {e}")


# Exemplo de uso:
if __name__ == "__main__":
    local_file_path = "caminho/do/seu/arquivo.txt"
    bucket_name = "seu-bucket-s3"
    s3_key = "caminho/dentro/do/bucket/arquivo.txt"

    upload_to_s3(local_file_path, bucket_name, s3_key)