from functions import *
import sys
import os

def print_matrix(matrix): #web found function to print on pycharm a large matrix in a proper way for the eyes
    for row in matrix:
        for element in row:
            print(f"{element:20}", end="")
        print()

dict = get_the_count_of_all_words()
print(dict)

'''
def printspaces():
    print("\n")

def main():
        GREEN = '\033[92m'
        WHITE = '\033[97m'
        RESET = '\033[0m'

        print(GREEN + "\n*********************************")
        print("      MY FIRST CHATBOT")
        print("*********************************" + RESET)
        print(WHITE + "\n      Project Python" + RESET)
        print(WHITE + "\n   BITAR RALPH BARBIER MATHIEU" + RESET)
        print(WHITE + "\n      Promo 2028 int-2" + RESET)
        input("Press Enter to continue...")
        while True:
            print("\nMain Menu:")
            print("1. Print the list of files")
            print("2. Start the cleaning of files")
            print("3. Print the TF-IDF matrix")
            print("4. Print the list of least important words")
            print("5. Print the list of words with the highest TF-IDF score")
            print("6. Print the most repeated words by a specific president")
            print("7. Print the word 'nation' repeated the most times")
            print("8. Find the first president speaking about 'climat' and 'écologie'")
            print("9. Print the list of words said by all presidents")
            print("0.Exit ")
            printspaces()

            choice = input("Enter the number corresponding to the function you want to access: ")

            if choice == '1':
                list = get_list_of_files()
                printspaces()
                print(list)
                printspaces()
                input("To return to the menu press any key :")


            elif choice == '2':
                input("Press Enter to convert the files to lowercase .( All the file will be added to the Cleaned directory)")
                convert_file_lowercases()
                printspaces()
                input("Press Enter to delete the punctuation of the files")
                delete_all_ponctuation()
                printspaces()
                choice_f = input("PRESS ENTER TO RELAUNCH THE APP TO CREATE THE NEW CLEANED FILES")
                break


            elif choice == '3':
                printspaces()
                print("1. Print the TF-IDF matrix with names")
                print("2. Print the TF-IDF matrix only the grid")
                choiceIDFTF = input("Enter the number corresponding to the function you want to access: ")
                if choiceIDFTF == "1":
                    idftfname = TF_IDF_function_with_names()
                    print_matrix(idftfname)
                elif choiceIDFTF == "2":
                    idftf = TF_IDF_function_matrix()
                    print_matrix(idftf)
                else:
                    while choiceIDFTF != 0:
                        print(("Invalid choice. Please enter a valid number:"))
                        choiceIDFTF = input("Enter the number corresponding to the function you want to access: ")
                input("To return to the menu press any key :")
                printspaces()

            elif choice == '4':
                printspaces()
                matrix = TF_IDF_function_with_names()
                List_impr = get_list_of_least_important_words(matrix)
                print(List_impr)
                input("To return to the menu press any key :")
                printspaces()
            elif choice == '5':
                printspaces()
                matrix = TF_IDF_function_with_names()
                List_impr2 = get_list_of_highest_TFIDF_score(matrix)
                print(List_impr2)
                input("To return to the menu press any key :")
                printspaces()
            elif choice == '6':
                printspaces()
                N = int(input("Enter an integer for the integer-most said words by chirac : "))
                ListChr = get_list_of_most_repeated_words_by_chirac(N)
                print(ListChr)
                input("To return to the menu press any key :")
                printspaces()
            elif choice == '7':
                printspaces()
                dictnation = President_Nation_word()
                repeated_the_most_time(dictnation,4)
                input("To return to the menu press any key :")
                printspaces()
            elif choice == '8':
                printspaces()
                get_first_president_speaking_climat_ecologie()
                input("To return to the menu press any key :")
                printspaces()
            elif choice == '9':
                printspaces()
                print(get_list_of_words_all_president_said(TF_IDF_function_with_names()))
                input("To return to the menu press any key :")
                printspaces()

            elif choice == '0':
                print("Exiting the application.")
                break

            else:
                print("Invalid choice. Please enter a valid number.")


if __name__ == "__main__":
    main()
'''