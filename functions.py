import os
import math
def list_of_files(directory, extension):#function that takes as parameter a string directory and a extention.txt and gives all the files that are realted to this directory with those extension
    files_names = []
    for filename in os.listdir(directory): #For loop for every file in the directory
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names

def get_list_of_files(): #Get the list of all the files for the directory speeches-2023116
    directory = "./speeches-20231116"
    input_list = list_of_files(directory, "txt")
    return input_list
def get_list_of_clean_files(): #Get the list of all the files from the directory Cleaned
    directory = "./Cleaned"
    input_list = list_of_files(directory, "txt")
    return input_list


def get_president_lastname():
    directory = "./speeches-20231116" #get the list of all the files from speeches directory
    input_list = list_of_files(directory, "txt")
    president_name = []

    for string in input_list: # for every file_name in the directory
        president_lastname = string[10:-3] #get only the part where the president name appear
        filtered_string = ''.join([char for char in president_lastname if char.isalpha() or char.isspace()]) #replace by nothing all the character that are not letter
        president_name.append(filtered_string)
    set_withoutdouble = set(president_name)# transform in a set the list of president name
    president_name_nodouble = list(set_withoutdouble)#retransform in a list the set of president name , this method delete all the doubles
    return president_name_nodouble
def get_president_entirename(listname): #Must use get_president_lastname
    List_fullname = []

    for name in listname: #for every Last name in the list of president name
        if name == "Sarkozy":# it detect which name is it and append it with the full name
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

    return List_fullname #return the list of all the president with their full name


def convert_file_lowercases(): # function to convert the Speeches directory files to a Cleaned directory
    file_list = get_list_of_files() #get list of all speeches files

    for filename in file_list:# for every file in the list of all files
        source_path = os.path.join('Speeches-20231116', filename) # we add the all path of each file


        if not os.path.exists(source_path):
            print(f"File not found: {source_path}")
            continue
        name, ext = os.path.splitext(filename)
        modified_name = f"{name}_cleaned{ext}"
        dest_path = os.path.join('Cleaned', modified_name)

        with open(source_path, 'r') as source_file:
            with open(dest_path, 'w') as dest_file:
                for line in source_file:
                    dest_file.write(line.lower())# copy each file but every line is in lower cases

    return()


def delete_all_ponctuation():#must have converted in lowercase first # deleted all the punctuation of cleaned files
    file_list = get_list_of_clean_files() #get the list of cleaned files
    punctuation = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~' # list all punctuation that should be deleted

    for file_path in file_list: # for every file in the file name list
        source_path = os.path.join('Cleaned', file_path) # give it the full path list

        with open(source_path, 'r') as file: # open the file
            lines = file.readlines() # get a list of all lines
            processed_lines = []#new group of lines which will be added the lines cleaned
            for line in lines: # for each string in the list all lines

                line = line.replace("'", " ").replace("-", " ") # replace ' by space and replace - by space so it doesnt modify the integrity of words

                line = ''.join(char for char in line if char not in punctuation) # every element of the punctuation list in the lines will be replace by '' which is nothing
                processed_lines.append(line)# append each line to a new group of lines


        with open(source_path, 'w') as file:# 'w' so it delete everything and add proccessed lines
            file.writelines(processed_lines)

#TF-FUNCTIONS :

def tf_function(file_name): # function that take as parameter a only file and give it is tf dictionary associated to it
    filepath = source_path = os.path.join('Cleaned', file_name) # join full path to the file name
    with open(filepath,'r') as file: # read the file
        lines = file.readlines() # get a list of all lines
        word_count = {}
        for line in lines: # for each line in all the lines
            words = line.split() # get a list of all the words in each line
            for word in words: # for every word in the list
                word_count[word] = word_count.get(word, 0) + 1 # add in a dictionary [word] = count of the word
    return(word_count)

#IDF FUNCTION:
def idf_function(): # idf function
    file_list = get_list_of_clean_files() # get list of clean files
    N = len(file_list) # get the number of all documents
    word_document_count = {}

    for file_name in file_list: # for every file in the list of all files
        word_counts = tf_function(file_name) # give the dictionary associated to each word of each file name
        for word in word_counts: # for word in the dictionarry
            if word not in word_document_count: #get the number of time the document appear for each file
                word_document_count[word] = 0
            word_document_count[word] += 1

    idf_dict = {}
    for word in word_document_count:
        idf_dict[word] = math.log10(N / word_document_count[word])

    return idf_dict

def TF_IDF_function_matrix():#it print the matrix in the inverse ,the first document is in the last column of the matrix
    file_list = get_list_of_clean_files()# get the list of files
    idf_dictionary = idf_function()  # get the idf_dictionary
    tf_idf_dict = {} # get the
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

def get_tf_idf_without_unimporant_names_with_word():
    list = TF_IDF_function_with_names()
    for column in list[1:]:
        All_values_are_zero = True
        for row in column[1:]:
            if row != 0 :
                All_values_are_zero = False
                break
        if All_values_are_zero == True :
            list.pop(list.index(column))
    return (list)

def get_the_count_of_all_words():
    matrix = TF_IDF_function_matrix()
    count = 0
    for row in matrix:
        count += 1
    return(count)

###PART 2 QUESTION PART
def get_question():
    string=''
    while string == '':
        string = input("Enter your question : ")
    return string

def clean_question(string):
    punctuation = '!"#$%&()*+,./:;<=>?@[\\]^_`{|}~'
    str2 = string.lower()
    str2 = ''.join(char for char in str2 if char not in punctuation)
    line = str2.replace("'", " ").replace("-", " ").replace("_"," ")
    Final_list = line.split(' ')
    return Final_list


def Terms_question_in_matrix(string):
    input_list = clean_question(string)
    matrix = TF_IDF_function_with_names()
    List_of_element_found_in_the_matrix = []

    for word in input_list:
        found = False
        for element in matrix:
            if element[0] == word:
                List_of_element_found_in_the_matrix.append(element[0])
                found = True
                break
        if not found:
            List_of_element_found_in_the_matrix.append(0)

    return List_of_element_found_in_the_matrix
def TF_IDF_STRING(string):

    input_list = clean_question(string)

    idf_dict = idf_function()
    tf_idf_vector = [0] * len(idf_dict)

    word_freq = {}
    for word in input_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    for word in input_list:
        if word in idf_dict:
            tf = word_freq[word] / len(input_list)
            idf = idf_dict[word]
            tf_idf = tf * idf
            index = list(idf_dict.keys()).index(word)
            tf_idf_vector[index] = floor_to_three_decimals(tf_idf)

    return tf_idf_vector



def dot_product(A,B):
    Output = 0
    for i in range (len(A)):
        Output += A[i]*B[i]
    return (Output)

def norm_of_vector(A):
    sum_square = 0
    for i in range (len(A)):
        sum_square += A[i]**2
    Output = math.sqrt(sum_square)
    return Output

def calculate_similarity(A,B):
    Output = (dot_product(A,B))/(norm_of_vector(A)*norm_of_vector(B))
    return Output

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def most_relevant_doc(matrix, TF_idf_string_questions,List_of_docs):
    matrix = transpose(matrix)
    max_similarity = 0
    doc_index_with_max_similarity = 0
    index = 0

    for doc_vector in matrix:
        current_similarity = calculate_similarity(doc_vector, TF_idf_string_questions)
        if current_similarity > max_similarity:
            max_similarity = current_similarity
            doc_index_with_max_similarity = index
        index += 1

    nom_document_max = List_of_docs[doc_index_with_max_similarity]
    return nom_document_max

def get_file_name_from_clean_name(clean_name):
    Output = clean_name[:-12]
    Output += '.txt'
    return(Output)

def get_sentence_from_question():
    Question = get_question()
    Question_cleaned = clean_question(Question)
    matrix = TF_IDF_STRING(Question)
    tfidfcorpus = TF_IDF_function_matrix()
    tfidfnames = transpose(TF_IDF_function_with_names())
    list_files = get_list_of_clean_files()
    value = 0
    index_of_value = 0
    for index, element in enumerate(matrix):
        if element >= value:
            value = element
            index_of_value = index
    Document_cleaned = most_relevant_doc(tfidfcorpus, matrix, list_files)
    Document_normal = get_file_name_from_clean_name(Document_cleaned)

    wordhighest = tfidfnames[0][index_of_value + 1]
    source_path_cleaned = os.path.join('Cleaned', Document_cleaned)
    source_path = os.path.join('Speeches-20231116', Document_normal)

    first_time_encounter = None 
    with open(source_path_cleaned, 'r') as file:
        lines = file.readlines()
        for line_number, line in enumerate(lines):
            list_string = line.split()
            for word_position, string in enumerate(list_string):
                if string == wordhighest:
                    first_time_encounter = (line_number, word_position)
                    break
            if first_time_encounter is not None:
                break
    with open(source_path,'r') as file :
        lines2 = file.readlines()
        final_sentence = lines2[line_number]
    print("Question entered: ",Question)
    print("Relevant document returned : ",Document_normal)
    print("Highest important word : ",wordhighest)


    question_starters = {
        "Comment": "Après analyse, ",
        "Pourquoi": "Car, ",
        "Peux-tu": "Oui, bien sûr! "
    }
    Question_split = Question.split(" ")

    if Question_split[0] in question_starters:
        response = question_starters[Question_split[0]]
        sentence = response + final_sentence
    else :
        sentence = "Pour repondre :"+ final_sentence

    
    

    print("AI response : ",sentence)