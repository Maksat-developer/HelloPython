import pyAesCrypt as sc
import os

def decryption(file, password):
    buffer_size =  512 * 1024

    sc.decryptFile(
            str(file),
            str(os.path.splitext(file)[0]),
            password,
            buffer_size
            )

    print("[Файл '" + str(os.path.splitext(file)[0]) + "'Расшифрован ]")

    os.remove(file)

def walking_by_dirs(dir, password):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        else:
            walking_by_dirs(path, password)

password = input("Введиье пароль для расшифровки: ")
walking_by_dirs("/home/fedora/Downloads", password)

