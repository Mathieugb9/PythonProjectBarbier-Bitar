import os
import math
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def get_list_of_files():
    directory = "./speeches-20231116"
    input_list = list_of_files(directory, "txt")
    return input_list
def get_list_of_clean_files():
    directory = "./Cleaned"
    input_list = list_of_files(directory, "txt")
    return input_list


def get_president_lastname():
    directory = "./speeches-20231116"
    input_list = list_of_files(directory, "txt")
    president_name = []

    for string in input_list:
        president_lastname = string[10:-3]
        filtered_string = ''.join([char for char in president_lastname if char.isalpha() or char.isspace()])
        president_name.append(filtered_string)
    set_withoutdouble = set(president_name)
    president_name_nodouble = list(set_withoutdouble)
    return president_name_nodouble
def get_president_entirename():
    listname = get_president_lastname()
    List_fullname = []

    for name in listname:
        if name == "Sarkozy":
            List_fullname.append("Nicolas Sarkozy")
        elif name == "Giscard dEstaing":
            List_fullname.append("Valéry Giscard d'Estaing")
        elif name == "Macron":
            List_fullname.append("Emmanuel Macron")
        elif name == "Chirac":
            List_fullname.append("Jacques Chirac")
        elif name == "Hollande":
            List_fullname.append("François Hollande")
        elif name == "Mitterrand":
            List_fullname.append("François Mitterrand")
        else:
            List_fullname.append("Unknown President")

    return List_fullname


def convert_file_lowercases():
    file_list = get_list_of_files()

    for filename in file_list:
        source_path = os.path.join('Speeches-20231116', filename)


        if not os.path.exists(source_path):
            print(f"File not found: {source_path}")
            continue
        name, ext = os.path.splitext(filename)
        modified_name = f"{name}_cleaned{ext}"
        dest_path = os.path.join('Cleaned', modified_name)

        with open(source_path, 'r') as source_file:
            with open(dest_path, 'w') as dest_file:
                for line in source_file:
                    dest_file.write(line.lower())

    return()


def delete_all_ponctuation():
    file_list = get_list_of_clean_files()
    punctuation = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'

    for file_path in file_list:
        source_path = os.path.join('Cleaned', file_path)

        with open(source_path, 'r') as file:
            lines = file.readlines()
            processed_lines = []
            for line in lines:

                line = line.replace("'", " ").replace("-", " ")

                line = ''.join(char for char in line if char not in punctuation)
                processed_lines.append(line)


        with open(source_path, 'w') as file:
            file.writelines(processed_lines)

#TF-FUNCTIONS :

def tf_function(file_name): #Il faut modifier pour qu'on puisse choisir qu'elle fichier est le bon

    filepath = f'/Users/mathieu/PycharmProjects/PYTHONPROJECTGPT/Cleaned/{file_name}'
    with open(filepath,'r') as file:
        lines = file.readlines()
        word_count = {}
        for line in lines:

            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return(word_count)

#IDF FUNCTION :
def idf_function(): #modify so it can only take a directory as parameter ( use the function ) and be giving a dictionary and not an list
    file_list = get_list_of_clean_files()
    N = len(file_list)
    word_document_count = {}


    for file_name in file_list:
        word_counts = tf_function(file_name)
        for word in word_counts:
            if word not in word_document_count:
                word_document_count[word] = 0
            word_document_count[word] += 1


    IDFLIST = []
    for word in word_document_count:
        idf_score = math.log(N / word_document_count[word])
        L = [word, idf_score]
        IDFLIST.append(L)

    return IDFLIST
'''
def TF_IDF_function():
'''