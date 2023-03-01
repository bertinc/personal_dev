import argparse
import constants as const
from cryptography.fernet import Fernet
import os

def enc_dec(args):
    # Encrypt DATA
    if hasattr(args, 'enc'):
        print(encrypt(args.enc))
    
    # Decrypt DATA
    elif hasattr(args, 'dec'):
        print(decrypt(args.password, args.dec))

    elif hasattr(args, 'key'):
        if args.key:
            print(get_key())
        elif args.clean:
            clear_files()

def clear_files():
    if os.path.isfile(const.DEC_FILE):
        os.remove(const.DEC_FILE)
        print('Decrypted files have been removed.')
    else:
        print('No files found.')

def get_key():
    key = Fernet.generate_key()
    return key.decode()            

def encrypt(dec_str=''):
    if dec_str:
        dec_text = dec_str
    else:
        dec_file = open(const.DEC_FILE, 'r')
        dec_text = dec_file.read()
        dec_file.close()

    # Do some encryption
    fernet = Fernet(const.ENC_DEC_KEY)
    enc_text = fernet.encrypt(dec_text.encode()).decode()

    if not dec_str:
        enc_file = open(const.ENC_FILE, 'w')
        enc_file.write(f'{enc_text}')
        enc_file.close()
        enc_text = 'Text has been encoded.'

    return enc_text

def decrypt(password='temp', enc_str=''):
    if enc_str:
        enc_text = enc_str
    else:
        enc_file = open(const.ENC_FILE, 'r')
        enc_text = enc_file.read()
        enc_file.close()

    # Do some encryption
    fernet = Fernet(const.ENC_DEC_KEY)
    dec_text = fernet.decrypt(enc_text.encode()).decode()

    # Check password
    stored_pass = fernet.decrypt(const.PASS.encode()).decode()
    if stored_pass != password:
        return 'Password invalid.'

    if not enc_str:
        dec_file = open(const.DEC_FILE, 'w')
        dec_file.write(f'{dec_text}')
        dec_file.close()
        dec_text = 'Text has been decoded.'

    return dec_text

def run():
    """
    
    """
    desc = "Encrypt decrypt tool."
    final_note = "For safe keeping!"
    parser = argparse.ArgumentParser(description=desc, epilog=final_note)

    subs = parser.add_subparsers(title='commands')

    arg_decrypt_file = subs.add_parser('dec', help='Import timesheet entries from a file.')
    arg_decrypt_file.add_argument('-dec', '-d', type=str, help='Enter any string to decrypt.')
    arg_decrypt_file.add_argument('-password', '-p', type=str, required=True, help='Enter the decryption password.')

    arg_encrypt_file = subs.add_parser('enc', help='Generate a timesheet report for management.')
    arg_encrypt_file.add_argument('-enc', '-e', type=str, help='Enter any string to encrypt.')

    arg_gen_key = subs.add_parser('tools', help='')
    arg_gen_key.add_argument('-key', '-k', action='store_true', help='Get a new encryption key.')
    arg_gen_key.add_argument('-clean', '-c', action='store_true', help='Delete decryption output.')

    args = parser.parse_args()
    enc_dec(args)

if __name__ == "__main__":
    run()