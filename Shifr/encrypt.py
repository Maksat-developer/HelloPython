import pyAesCrypt as sc
import os 

def encryption(file, password):
    buffer_size = 512 * 1024
    
    sc.encryptFile(
            str(file),
            str(file) + ".crp",
            password,
            buffer_size
            )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "'Зашифрован ]") 

    os.remove(file)

def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = input("Введиье пароль для шифрования: ")
walking_by_dirs("/home/fedora/Downloads", password)

    
