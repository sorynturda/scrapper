from cryptography.fernet import Fernet

# Load the key from the .key file
with open("../secrets/filekey.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)


def encrypt_data(text: str) -> None:
    # Create a Fernet object using the key
    txt = "text de encryptat"
    # Open the file to be encrypted in binary read mode
    encrypted = fernet.encrypt(txt.encode())

    # Overwrite the original file with the encrypted data
    with open("file.dat", "wb") as f:
        f.write(encrypted)


def decrypt_data(file_name: str) -> str:
    # Read the encrypted data from the file
    try:
        with open(file_name + ".dat", "rb") as f:
            encrypted = f.read()

        # Decrypt the encrypted data
        decrypted = fernet.decrypt(encrypted).decode()
        return decrypted

    except FileNotFoundError:
        return "File " + file_name + ".dat does not exist"
    except Exception as e:
        print(str(e))
        return str(e)
