def part1_staff_version():
    print('Staff Version with Histogram\n')
    count=0 #counts  initialized to zero
    progress_count=0
    trailer_count=0
    retriever_count=0
    exclude_count=0
    pass_input=0
    defer_input=0
    fail_input=0
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

            if pass_input==120:
                progress_count+=1
                print('Progress')
            elif pass_input==100:
                trailer_count+=1
                print('Progress - Module Trailer')
            elif fail_input in range(80,121):
                exclude_count+=1
                print('Exclude')
            elif fail_input in range(0,61):
                retriever_count+=1
                print('Do not progress - Module retriever')
            count=count+1
            while True:
                #where the user decides whether to quit or continue
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
    print('Horizontal Histogram\n') #displays a horizontal histogram
    print('Progress ', progress_count,' : ', progress_count*"*")
    print('Trailer ', trailer_count,'  : ', trailer_count*"*")
    print('Retriever ', retriever_count,' : ', retriever_count*"*")
    print('Excluded ', exclude_count,' : ', exclude_count*"*")

    print(count, 'outcomes in total.')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')

part1_staff_version()
