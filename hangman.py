from class_group import *



def main():
    a = Game()
    print(a)
    while not a.win:
        print("Type in the indext of the letter and the alphabet for what you want to guess: ")
        print(a.guess)
        i = int(input("index: "))
        if i < 0 or i >= a.current_word.length:
            print("index out of bound")
            return 0
        
        l = input("letter: ")
        
        if type(l) is not str or len(l) != 1:
            print("please put in a valid letter")
            return 1

        a.check_answer(i,l)


# game needs word 
# game can check if the answer is correct
#game should load the word lists in to list that are fomated as a signle letters
#it should be able to schose game 




if __name__ == "__main__":
    main()

    
    

