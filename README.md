HashCrack
HashCrack is a simple yet effective Python-based tool that attempts to crack common hash types (MD5, SHA1, SHA256, SHA384, SHA512) by querying publicly available online hash databases.

Overview
HashCrack supports the detection and cracking of the following hash types:

MD5

SHA1

SHA256

SHA384

SHA512

By identifying the hash type based on its length, it queries multiple online sources to find the original plaintext value—if it's publicly available.

Features
Automatically detects hash type by length

Queries multiple public hash cracking APIs and websites

Supports:

Cracking a single hash

Cracking multiple hashes from a file

Searching and cracking hashes found inside directories

Multi-threaded for faster cracking

Clean and colored terminal output using colorama and pyfiglet


Required packages:

requests

colorama

pyfiglet

urllib3

How to Use
Run the tool:

bash
python hashcrack.py

You'll be prompted to choose between:

A single hash

A file containing hashes

A directory to scan for hash patterns

You can also configure the number of threads for concurrent cracking.

Example:

vbnet

Enter the hash value(s) to crack: 5d41402abc4b2a76b9719d911017c592
Do you want to provide a single hash, a file containing hashes, or a directory containing files with hashes? (S/F/D): S
Enter the number of threads to use for concurrent hash cracking tasks (default is 4): 4
Notes
The tool uses requests to query online databases like:

hashtoolkit.com

nitrxgen.net

md5decrypt.net

The cracking process depends entirely on whether the hash exists in those databases. It does not attempt brute-force or dictionary-based attacks locally.

Legal Disclaimer
This tool is intended strictly for educational purposes and authorized testing.
Do not use this software to crack passwords or hashes you do not have permission to test.
The developer is not responsible for any misuse of this tool.



