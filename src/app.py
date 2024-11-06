 # app.py
def to_uppercase(text):
    """
    Convertește textul la majuscule.

    :param text: Textul de convertit
    :return: Textul în majuscule
    """
    return text.upper()

def to_lowercase(text):
    """
    Convertește textul la litere mici.

    :param text: Textul de convertit
    :return: Textul în litere mici
    """
    return text.lower()

def main():
    """
    Funcția principală care permite utilizatorului să aleagă transformarea textului
    în majuscule sau litere mici și să introducă textul.
    """
    print("Alege transformarea:")
    print("1. Transformă în MAJUSCULE")
    print("2. Transformă în litere mici")

    choice = input("Introdu opțiunea (1 sau 2): ")
    text = input("Introdu textul: ")

    if choice == '1':
        print("Text în majuscule:", to_uppercase(text))
    elif choice == '2':
        print("Text în litere mici:", to_lowercase(text))
    else:
        print("Opțiune invalidă.")

if __name__ == "__main__":
    main()