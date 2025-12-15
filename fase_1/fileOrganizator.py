import os
import shutil

def creat_a_folder_on_the_desktop(extension):
    """
    Creates a folder named after the file extension on the desktop.

    Args:
    extension (str): The file extension without the dot.

    Returns:
    str: The path to the created folder.
    """
    desktop = os.path.join(r"C:\Users\silva\OneDrive\Desktop\folder_organizator", extension) 
    os.makedirs(desktop, exist_ok=True) 
    return desktop 

directory_download  = os.path.join(os.path.expanduser("~"), "Downloads") #endereço da pasta Downloads

contador_arquivos_movidos = 0
for item in os.listdir(directory_download): #Itera sobre todos os itens da pasta
    file_path = os.path.join(directory_download, item) #cria o endereço exato de cada arquivo
    name, ext = os.path.splitext(item) #separa o nome do arquivo do nome da extensão

    if os.path.isfile(file_path): #verifica se é pasta ou arquivo
        contador_arquivos_movidos += 1 # contador de arquivos movidos
        destination_folder = creat_a_folder_on_the_desktop(ext.replace(".", "")) #passa o nome da extensão sem o ponto para a função, e retorna o endereço da nova pasta
        shutil.move(file_path, destination_folder) #endereço de onde esta o arquivo e o seu destino.
        
print(f"🚀 Organização concluída!")
print(f"📁 Arquivos movidos: {contador_arquivos_movidos}")
