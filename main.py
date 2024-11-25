from setUpToUser import *



def main():
    flag = True
    print(helloMessage)
    while flag:
        print(list_command)
        option = str(input(choose_option))
        if option == "1":
            user_add_book()
        if option == "2":
            user_del_book()
        if option == "3":
            user_find_book()
        if option == "4":
            user_watch_all_book()
        if option == "5":
            user_change_status_book()
        if option == "0":
            flag = False


if __name__ == "__main__":
    main()
