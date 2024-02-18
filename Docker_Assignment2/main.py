import os
from collections import Counter
import string
import socket
import sys

# Folder paths
resFile = r'/home/output/result.txt'
dir_path = r'/home/data/'
ifFilePath = r'/home/data/IF.txt'

# Open result file
with open(resFile, 'w+') as result_file:

    # List to store files
    files_list = []

    # List name of all the text files at location: /home/data
    for file_name in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file_name)):
            files_list.append(file_name)

    # Write file names to result file
    result_file.write("Files at location /home/data are:\n")
    for file_name in files_list:
        result_file.write("->" + file_name + "\n")

        # Total number of words in each text file
        with open(os.path.join(dir_path, file_name), 'r') as file:
            read_data = file.read()
            per_word = read_data.split()
            total_words = len(per_word)
            result_file.write("Total Words: " + str(total_words) + "\n")

    # Total number of words in all text files
    total_words_all_files = sum(len(open(os.path.join(dir_path, file_name), 'r').read().split()) for file_name in files_list)
    result_file.write("Total number of words in all text files: " + str(total_words_all_files) + "\n")

    # Top 3 words with maximum number of counts in IF.txt
    with open(ifFilePath, 'r') as file:
        read_data = file.read()
        per_word = read_data.split()
        word = [i.translate(str.maketrans('', '', string.punctuation)).capitalize() for i in per_word]
        Counter = Counter(word)
        most_occur = Counter.most_common(3)
        result_file.write("Top 3 words with maximum number of counts in IF.txt " + str(most_occur) + "\n")

    # Get and write computer's IP address
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    result_file.write("Your Computer IP Address is: " + IPAddr + "\n")

# Print the content of result file
with open(resFile, 'r', encoding='utf-8') as file:
    print(file.read())