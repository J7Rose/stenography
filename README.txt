Jose Gonzalez
1001705536
03/07/2025

Stenography

This primitive user interface is an implementation of steganography.
The program is capable of embedding and retrieving messages from plaintext files (of any format).

It does this by hiding the message (M) within the plaintext (P) file.
Starting from the specified bit (S) and replacing periodically based on the length specified (L).
The program has two modes (C), for embedding and retrieving.

How to run:

To run the program enter:
python3 main.py

The program will then ask the user to enter values in the following format:
Mode of operation: (int) 1 (for embedding) or 2 (for retrieval)
Plaintext file: (str) filename
Starting bit: (int)
Length: (int or list of ints) for a list of ints simply add ',' between each value (i.e. 8,16,24)
Message file: (str) filename

This is an example of how to embed a message in a plaintext file using the program:
Stenography
Modes:
1: Embedding
2: Retrieval
Enter mode of operation: 1
Enter plaintext file: Color-white.JPG
Enter starting bit: 128
Enter length (periodicity) of the replacement (in bits): 4
Enter message file: onesfile

example of retrieval:
Stenography
Modes:
1: Embedding
2: Retrieval
Enter mode of operation: 2
Enter plaintext file: Color-white.JPG
Enter starting bit: 128
Enter length (periodicity) of the replacement (in bits): 4
Enter message file: message

This should lead to the message file containing the initial data from the onesfile

