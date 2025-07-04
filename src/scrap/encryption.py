from cryptography.fernet import Fernet


with open("secrets/filekey.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)


def encrypt_data(content: str, file_name: str) -> None:
    """
    Save text to file

    Args:
        content (str): scraped text
        file_name (str): name of the file
    Returns:
        None
    """

    encrypted = fernet.encrypt(content.encode())

    with open("wiki/" + file_name + ".dat", "wb") as f:
        f.write(encrypted)


def decrypt_data(file_name: str) -> str:
    """
    Read encrypted data from file

    Args:
        file_name (str): name of the file
    Returns:
        str: dencrypted data
    """

    try:
        with open("wiki/" + file_name + ".dat", "rb") as f:
            encrypted = f.read()

        decrypted = fernet.decrypt(encrypted).decode()
        return decrypted

    except FileNotFoundError:
        raise FileNotFoundError
    except Exception as e:
        print(str(e))
        return str(e)
