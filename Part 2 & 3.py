def part2_and_3():
    print('Staff Version with Histogram.\n')
    count=0 #counts  initialized to zero
    progress_count=0
    trailer_count=0
    retriver_count=0
    exclude_count=0
    pass_input=0
    defer_input=0
    fail_input=0
    star= "       *     " 
    space="             "
    pass_stored=[] #creating a list for part3 question
    defer_stored=[]
    fail_stored=[]
    attempt=[]
    content=[]
    while True:
            while True:
                    try:
                            pass_input=int(input('Please enter your credit at pass: '))
                    except:
                            print('Integer required')
                            continue
                    if (pass_input>120 or pass_input<0 and pass_input%20!=0) or (0<=pass_input<=120 and pass_input%20!=0):
                            print('Out of range')
                            continue
                    break
            while True:
                    try:
                            defer_input=int(input('Please enter your credit at defer: '))
                    except:
                            print('Integer required')
                            continue
                    if (defer_input>120 or defer_input<0 and defer_input%20!=0) or (0<=defer_input<=120 and defer_input%20!=0):
                            print('Out of range')
                            continue
                    break
            while True:
                    try:
                            fail_input=int(input('Please enter your credit at fail: '))
                    except:
                            print('Integer required')
                            continue
                    if (fail_input>120 or fail_input<0 and fail_input%20!=0) or (0<=fail_input<=120 and fail_input%20!=0):
                            print('Out of range')
                            continue
                    break

            total_outcome=pass_input+defer_input+fail_input
            if total_outcome!=120:
                    print('Total incorrect')
                    continue

            pass_stored.append(pass_input) #puts the value entered in a list
            defer_stored.append(defer_input)
            fail_stored.append(fail_input)

            if pass_input==120:
                progress_count+=1
                print('Progress')
                attempt.append('Progress')
            elif pass_input==100:
                trailer_count+=1
                print('Progress - Module Trailer')
                attempt.append('Progress - Module Trailer')
            elif fail_input in range(80,121):
                exclude_count+=1
                print('Exclude')
                attempt.append('Exclude')
            elif fail_input in range(0,61):
                retriver_count+=1
                print('Do not progress - Module Retriever')
                attempt.append('Do not progress - Module Retriever')               
            count=count+1
            
            while True:
                option=(input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: \n"))
                if (option==('y') or option==('Y')) or (option==('q') or option==('Q')):
                    print("")
                else:
                    print ('Invalid output. Please re-enter.')
                    continue
                if option==('y') or option==('Y') or option==('q') or option==('Q'):
                    break
            if option==('q') or option==('Q'):
                break
        
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    print('Vertical Histogram.\n')#displays a vertical histogram
    print('Progress ', progress_count ,'|', 'Trailer ', trailer_count,'|','Retriever ', retriver_count,'|', 'Excluded ', exclude_count)

    for histogram in range(count):#for count to display stars.
        if progress_count>=1:#checks if there are any progress results that have appeared
            print(star, end="")
            progress_count-=1#the count reduces after each IF condition
        else:
            print(space, end="")

        if trailer_count>=1:
            print(star, end="")
            trailer_count-=1
        else:
            print(space, end="")

        if retriver_count>=1:
            print(star, end="")
            retriver_count-=1
        else:
            print(space, end="")

        if exclude_count>=1:
            print(star, end="\n")
            exclude_count-=1
        else:
            print(space, end="\n")

    print(count, 'outcomes in total.')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')

    length=len(pass_stored)#calculates the number of times the program has been looped
    for stored_data in range(length):
       content_details=(attempt[stored_data]+" "+"-"+" "+str(pass_stored[stored_data])+","+" "+str(defer_stored[stored_data])+","+" "+str(fail_stored[stored_data]))#concentation has been used to add string values
       print(content_details)
       content.append(content_details)#every record is added to a variable called content

    length_2=len(content)#calculates the number of times the results have been displayed
    for text_file in range(length_2):
        file = open('file_for_part2.txt', 'a')#a file named myfile is opened and the value is stored in the file. Also the letter 'a' helps to open a file
        file.write(content[text_file]+'\n')
        file.flush() #clears the internal buffer of the file
        file.close()#closes the opened file
    

part2_and_3()
