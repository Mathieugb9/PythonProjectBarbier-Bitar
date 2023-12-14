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
def get_president_entirename(listname): #Must use get_president_lastname
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


def delete_all_ponctuation():#must have converted in lowercase first
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

def tf_function(file_name):
    filepath = source_path = os.path.join('Cleaned', file_name)
    with open(filepath,'r') as file:
        lines = file.readlines()
        word_count = {}
        for line in lines:
            words = line.split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
    return(word_count)

#IDF FUNCTION:
def idf_function():
    file_list = get_list_of_clean_files()
    N = len(file_list)
    word_document_count = {}

    for file_name in file_list:
        word_counts = tf_function(file_name)
        for word in word_counts:
            if word not in word_document_count:
                word_document_count[word] = 0
            word_document_count[word] += 1

    idf_dict = {}
    for word in word_document_count:
        idf_dict[word] = math.log10(N / word_document_count[word])

    return idf_dict

def TF_IDF_function_matrix():#it print the matrix in the inverse ,the first document is in the last column of the matrix
    file_list = get_list_of_clean_files()
    idf_dictionary = idf_function()
    tf_idf_dict = {}
    for file_name in file_list:
        word_count = tf_function(file_name)
        for word, tf in word_count.items():
            if word not in tf_idf_dict:
                tf_idf_dict[word] = [0] * len(file_list)
            file_index = file_list.index(file_name)
            tf_idf_dict[word][file_index] = tf * idf_dictionary.get(word, 0)
    tf_idf_matrix = []
    for word in tf_idf_dict:
        row = tf_idf_dict[word]
        tf_idf_matrix.append(row)
    return tf_idf_matrix
def floor_to_three_decimals(number):
    return math.floor(number * 1000) / 1000
def TF_IDF_function_with_names():
    file_list = get_list_of_clean_files()
    idf_dictionary = idf_function()
    tf_idf_dict = {}
    for file_name in file_list:
        word_count = tf_function(file_name)
        for word, tf in word_count.items():
            if word not in tf_idf_dict:
                tf_idf_dict[word] = [0] * len(file_list)
            file_index = file_list.index(file_name)
            tf_idf_dict[word][file_index] = floor_to_three_decimals(tf * idf_dictionary.get(word, 0))
    file_list_name_only=[]
    for names in file_list:
        file_list_name_only.append(names[11:-12])
    header_row = ["word/document"] + file_list_name_only
    tf_idf_matrix = [header_row]
    for word in tf_idf_dict:
        row = [word] + tf_idf_dict[word]
        '''row = tf_idf_dict[word] # if we just want the matrix'''
        tf_idf_matrix.append(row)
    return tf_idf_matrix

def get_list_of_least_important_words(matrix):
    ListofIDF0words = []
    for row in matrix[1:]:
        IDF_0 = True
        for element in row[1:]:
            if (element != 0) :
                IDF_0 = False
        if (IDF_0 == True) :
            ListofIDF0words.append(row[0])

    return(ListofIDF0words)

def get_list_of_highest_TFIDF_score(matrix):
    List_of_Highest_TFIDF_score=[]
    for row in matrix[1:] :
        for element_index in range(1,len(row)):
            element = row[element_index]
            if (element >= 0.9):
                word = row[0]
                document_name = matrix[0][element_index]
                List_of_Highest_TFIDF_score.append((word, document_name, element))
    return(List_of_Highest_TFIDF_score)


def get_list_of_most_repeated_words_by_chirac(N):
    Chirac_count = {}
    List_of_file_by_chirac = ["Nomination_Chirac1_cleaned.txt","Nomination_Chirac2_cleaned.txt"]
    for file in List_of_file_by_chirac:
        word_count = tf_function(file)
        for word, count in word_count.items():
            if word not in Chirac_count:
                Chirac_count[word] = 0
            Chirac_count[word] += count
    sorted_dict = sorted(Chirac_count.items(), key=lambda x: x[1], reverse=True) #function found to sort a dictionary
    for i in range(N):
        print(sorted_dict[i])
    return ()
'''def get_president_lastname_Cleaned_for_Nation(input_list):
    president_name = []
    for string in input_list:
        president_lastname = string[10:-11]
        filtered_string = ''.join([char for char in president_lastname if char.isalpha() or char.isspace()])
        president_name.append(filtered_string)
    set_withoutdouble = set(president_name)
    president_name_nodouble = list(set_withoutdouble)
    return president_name_nodouble'''
def President_Nation_word():
    list=get_list_of_clean_files()
    List_of_names_of_files_containing_Nation = []

    original_dict = {}
    for element in list:
        dict = tf_function(element)
        if "nation" in dict:
            List_of_names_of_files_containing_Nation.append(element)
            original_dict[element] = dict["nation"]
    '''print(original_dict)'''
    new_dict = {}
    for key, value in original_dict.items():
        filtered_string = key[10:-11]
        cleaned_key = ''.join(filter(str.isalpha, filtered_string))
        if cleaned_key in new_dict:
            new_dict[cleaned_key] += value
        else:
            new_dict[cleaned_key] = value
    '''return new_dict,List_of_names_of_files_containing_Nation'''
    return new_dict

def repeated_the_most_time(dictionary,N):
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)  # function found to sort a dictionary
    if N >= len(sorted_dict):
        N = len(sorted_dict)
    for i in range(N):
        print(sorted_dict[i])
    return ()

def get_first_president_speaking_climat_ecologie():
    file_list = get_list_of_clean_files()
    dict_climat = {}
    dict_ecologie = {}
    found_climat = False
    found_écologie = False
    for file_path in file_list:
        source_path = os.path.join('Cleaned', file_path)
        with open(source_path, 'r') as file:
            iteration = 0
            lines = file.readlines()
            for line in lines:
                if "climat" in line and file_path not in dict_climat:
                    dict_climat[file_path] = iteration
                    found_climat = True
                elif "écologie" in line and file_path not in dict_ecologie:
                    dict_ecologie[file_path] = iteration
                    found_écologie = True
                iteration += 1

    if found_climat == True :
        key_cleaned_dict_climat = {}
        for key, value in dict_climat.items():
            filtered_string = key[10:-11]
            cleaned_key_climat = ''.join(filter(str.isalpha, filtered_string))
            key_cleaned_dict_climat[cleaned_key_climat]= value
        sorted_dict_climat = sorted(key_cleaned_dict_climat.items(), key=lambda x: x[1], reverse=True)
        print("The first president to talk about climat is (Name,Line)",sorted_dict_climat[1])

    if found_écologie == True:
        key_cleaned_dict_ecologie = {}
        for key, value in dict_ecologie.items():
            filtered_string = key[10:-11]
            cleaned_key_climat = ''.join(filter(str.isalpha, filtered_string))
            key_cleaned_dict_climat[cleaned_key_climat] = value
        sorted_dict_ecologie = sorted(key_cleaned_dict_ecologie.items(), key=lambda x: x[1], reverse=True)
        print("The first president to talk about écologie is (Name,Line)",sorted_dict_ecologie[1])
    elif found_climat == False :
        print("climat not found in files.")
    elif found_écologie == False :
        print("écologie not found in files")





    return()
def get_list_of_words_all_president_said(matrix):
    List_of_TFIDF_greater_than_zero=[]
    appear_in_doc = False
    for row in matrix[1:]:
        if all(element > 0 for element in row[1:5]) and (row[5] > 0 or row[7] > 0) and (row[6] > 0 or row[8] > 0):
            word = row[0]
            List_of_TFIDF_greater_than_zero.append(word)

    '''list_unimportant = get_list_of_least_important_words(matrix)
    List_of_grzero_not_in_unimportant = []
    for element in List_of_TFIDF_greater_than_zero :
        similarity = False
        for values in list_unimportant:
            if element == values :
                similarity == True
        if similarity == False :
            List_of_grzero_not_in_unimportant.append(element)'''


    return(List_of_TFIDF_greater_than_zero)

def get_tf_idf_without_unimporant_names():
    list = TF_IDF_function_with_names()
    for column in list[1:]:
        for row in column[1:]