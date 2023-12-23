from registros import registro, arquivos_registro


if __name__ == '__main__':
    usuarios = 'usuarios.json'

    # Logica para verificar a existencia do arquivo
    # Se o arquivo nao existir ira criar
    if not arquivos_registro.verifica_arquivo(usuarios):
        arquivos_registro.cria_arquivo(usuarios)
