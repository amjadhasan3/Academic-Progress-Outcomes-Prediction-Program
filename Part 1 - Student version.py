def part1():#using 1 function for student version
        while True:#an endless loop until the statement 'break' is entered.
                while True: #used till the correct input is entered
                        try:
                                pass_input=int(input('Please enter your credit at pass: ')) #getting input from the user
                        except:
                                print('Integer required\n') #if non integer input is entered this will output to the user
                                continue #this will go back again and ask for input until a correct input is entered
                        if (pass_input>120 or pass_input<0 and pass_input%20!=0) or (0<=pass_input<=120 and pass_input%20!=0): #checks if input range is within the range of input.
                                print('Out of range\n')
                                continue
                        break #if a correct input is entered then this loop will break and go the next loop
                while True:
                        try:
                                defer_input=int(input('Please enter your credit at defer: '))
                        except:
                                print('Integer required\n')
                                continue
                        if (defer_input>120 or defer_input<0 and defer_input%20!=0) or (0<=defer_input<=120 and defer_input%20!=0):
                                print('Out of range\n')
                                continue
                        break
                while True:
                        try:
                                fail_input=int(input('Please enter your credit at fail: '))
                        except:
                                print('Integer required\n')
                                continue
                        if (fail_input>120 or fail_input<0 and fail_input%20!=0) or (0<=fail_input<=120 and fail_input%20!=0):
                                print('Out of range\n')
                                continue
                        break
                total=pass_input+defer_input+fail_input #calculated the total
                if total!=120: #checks if the total is inccorect.
                        print('Total incorrect\n')
                        continue #if it's incorrect the loop will start from the beginning
                break
        
        #using only pass and fail marks to calculate the status
        if pass_input==120:
                print('Progress\n')
        elif pass_input==100:
                print('Progress - Module Trailer\n')
        elif fail_input in range(80,121):
                print('Exclude\n')
        elif fail_input in range(0,61):
                print('Do not progress - Module Retriever\n')

part1()#calling the function to run the program
