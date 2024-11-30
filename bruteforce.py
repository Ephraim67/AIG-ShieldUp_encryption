'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile

# Use a method to attempt to extract the zip file with a given password
# def attempt_extract(zf_handle, password):

def attempt_extract(zf_handle, password):
    try:
        zf_handle.extractall(pwd=password)
        return True
    except RuntimeError:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    print("[+] Beginning bruteforce ")
    try:
        with ZipFile('enc.zip') as zf:

            with open('rockyou.txt', 'rb') as f:
                # Iterate through each line in the password list
                for line in f:
                    # Strip newline characters and encode the password
                    password = line.strip()
                    print(f"[*] Trying password: {password.decode(errors='ignore')}")

                    # Attempt extraction with the current password
                    if attempt_extract(zf, password):
                        print(f"[+] Password found: {password.decode(errors='ignore')}")
                        return
        
        print(f"[+] Password not found in list")

    except FileNotFoundError as e:
        print(f"File not found: {e}")

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()