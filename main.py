from name_function import  get_format_name
if __name__ == '__main__':
    print("Enter 'q' at any time to quit")
    while True :
        frist =input("\n please give me frist name :")
        if frist=='q':
            break
        last=input("\n please give me last name : ")
        if last=='q':
            break
        print("\n if you have'nt middle name press enter")
        midlle=input("\n please give me midlle name : ")
        if midlle=='q':
            break


        formatted_name=get_format_name(frist,last,midlle)
        print("\n Neatly formatted name: "+formatted_name+".")



