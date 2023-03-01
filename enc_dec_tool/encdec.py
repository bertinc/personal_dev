import argparse
import constants as const
from cryptography.fernet import Fernet

def enc_dec(args):
    # Encrypt DATA
    if hasattr(args, 'enc'):
        print(encrypt())
    
    # Decrypt DATA
    elif hasattr(args, 'dec'):
        print(decrypt())

    elif hasattr(args, 'key'):
        print(get_key())

def get_key():
    key = Fernet.generate_key()
    return key.decode()            

def encrypt():
    dec_file = open(const.DEC_FILE, 'r')
    dec_text = dec_file.read()
    dec_file.close()

    # Do some encryption
    fernet = Fernet(const.ENC_DEC_KEY)
    enc_text = fernet.encrypt(dec_text.encode())

    enc_file = open(const.ENC_FILE, 'w')
    enc_file.write(f'{enc_text.decode()}')
    enc_file.close()

    return 'Text has been encoded.'

def decrypt():
    enc_file = open(const.ENC_FILE, 'r')
    enc_text = enc_file.read()
    enc_file.close()

    # Do some encryption
    fernet = Fernet(const.ENC_DEC_KEY)
    dec_text = fernet.decrypt(enc_text.encode()).decode()

    dec_file = open(const.DEC_FILE, 'w')
    dec_file.write(f'{dec_text}')
    dec_file.close()

    return 'Text has been decoded.'

def run():
    """
    
    """
    desc = "Encrypt decrypt tool."
    final_note = "For safe keeping!"
    parser = argparse.ArgumentParser(description=desc, epilog=final_note)

    subs = parser.add_subparsers(title='commands')

    # 
    arg_decrypt_file = subs.add_parser('dec', help='Import timesheet entries from a file.')
    arg_decrypt_file.add_argument('-dec', action='store_true', help='')

    # 
    arg_encrypt_file = subs.add_parser('enc', help='Generate a timesheet report for management.')
    arg_encrypt_file.add_argument('-enc', action='store_true', help='')

    arg_gen_key = subs.add_parser('key', help='')
    arg_gen_key.add_argument('-key', help='')

    args = parser.parse_args()
    enc_dec(args)

if __name__ == "__main__":
    run()