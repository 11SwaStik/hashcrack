import re
import os
import requests
import concurrent.futures
import logging
import pyfiglet
from colorama import init, Fore
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Initialize colorama
init()

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Custom ASCII art font
custom_figlet = pyfiglet.Figlet(font='block')

# Custom colors
RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
RESET = Fore.RESET

def get_user_input():
    print(custom_figlet.renderText("# CRACK"))
    print(f"{YELLOW}Please provide the following information:{RESET}")
    hash_input = input("Enter the hash value(s) to crack: ")
    choice = input("Do you want to provide a single hash, a file containing hashes, or a directory containing files with hashes? (S/F/D): ")
    if choice.upper() == 'S':
        hash_type = 'single'
        file_or_dir = hash_input
    elif choice.upper() == 'F':
        hash_type = 'file'
        file_or_dir = input("Enter the path to the file containing hash values: ")
    elif choice.upper() == 'D':
        hash_type = 'directory'
        file_or_dir = input("Enter the path to the directory containing files with hash values: ")
    else:
        print(f"{RED}Invalid choice. Please choose 'S', 'F', or 'D'.{RESET}")
        return None, None, None, None
    thread_count = int(input("Enter the number of threads to use for concurrent hash cracking tasks (default is 4): ") or 4)
    return hash_type, hash_input, file_or_dir, thread_count

def f1(hashvalue, hashtype):
    return False

def f2(hashvalue, hashtype):
    response = requests.get('https://hashtoolkit.com/reverse-hash/?hash=' + hashvalue).text
    match = re.search(r'/generate-hash/\?text=(.*?)"', response)
    if match:
        return match.group(1)
    else:
        return False

def f3(hashvalue, hashtype):
    response = requests.get('https://www.nitrxgen.net/md5db/' + hashvalue, verify=False).text
    if response:
        return response
    else:
        return False

def f4(hashvalue, hashtype):
    return False

def f5(hashvalue, hashtype):
    response = requests.get('https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=deanna_abshire@proxymail.eu&code=1152464b80a61728' % (hashvalue, hashtype)).text
    if len(response) != 0:
        return response
    else:
        return False

md5_custom_functions = [f3, f1, f2, f5, f4]
sha1_custom_functions = [f1, f2, f5, f4]
sha256_custom_functions = [f1, f2, f5]
sha384_custom_functions = [f1, f2, f5]
sha512_custom_functions = [f1, f2, f5]

def custom_crack(hashvalue):
    result = False
    if len(hashvalue) == 32:
        print ('%s Hash function : MD5' % YELLOW)
        for custom_api in md5_custom_functions:
            r = custom_api(hashvalue, 'md5')
            if r:
                return r
    elif len(hashvalue) == 40:
        print ('%s Hash function : SHA1' % YELLOW)
        for custom_api in sha1_custom_functions:
            r = custom_api(hashvalue, 'sha1')
            if r:
                return r
    elif len(hashvalue) == 64:
        print ('%s Hash function : SHA-256' % YELLOW)
        for custom_api in sha256_custom_functions:
            r = custom_api(hashvalue, 'sha256')
            if r:
                return r
    elif len(hashvalue) == 96:
        print ('%s Hash function : SHA-384' % YELLOW)
        for custom_api in sha384_custom_functions:
            r = custom_api(hashvalue, 'sha384')
            if r:
                return r
    elif len(hashvalue) == 128:
        print ('%s Hash function : SHA-512' % YELLOW)
        for custom_api in sha512_custom_functions:
            r = custom_api(hashvalue, 'sha512')
            if r:
                return r
    else:
        print ('%s This hash type is not supported.' % RED)
        return False

custom_result = {}

def custom_threaded(hashvalue):
    resp = custom_crack(hashvalue)
    if resp:
        print (hashvalue + ' : ' + resp)
        custom_result[hashvalue] = resp

def custom_grepper(directory):
    os.system('''grep -Pr "[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" %s --exclude=\*.{png,jpg,jpeg,mp3,mp4,zip,gz} |
        grep -Po "[a-f0-9]{128}|[a-f0-9]{96}|[a-f0-9]{64}|[a-f0-9]{40}|[a-f0-9]{32}" >> %s/%s.txt''' % (directory, cwd, directory.split('/')[-1]))
    print ('%s Results saved in %s.txt' % (info, directory.split('/')[-1]))

if __name__ == "__main__":
    hash_type, hash_input, file_or_dir, thread_count = get_user_input()
    if hash_type == 'single':
        result = custom_crack(hash_input)
        if result:
            print("Cracked hash:", result)
        else:
            print("Failed to crack hash.")
    elif hash_type == 'file':
        try:
            custom_grepper(file_or_dir)
        except KeyboardInterrupt:
            pass
    elif hash_type == 'directory':
        try:
            custom_grepper(file_or_dir)
        except KeyboardInterrupt:
            pass
    else:
        print(f"{RED}Exiting due to invalid input.{RESET}")
