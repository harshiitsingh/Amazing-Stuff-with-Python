import math

def FSPL(): # free space path loss
    r = eval(input("\nEnter the value of distance: "))
    f = eval(input("Enter the value of frequency: "))
    value = 32.4 + 20 * math.log(r) + 20 * math.log(f)
    return value

def Noise_density():
    Ts = eval(input("\nEnter the value of System Noise Temperature for ground station receiver, Ts : "))
    value = -228.6 + 10 * math.log(Ts)
    return value

# def Gain_to_noise_temp():

# def switcher(x):
#     print("*****WHAT DO YOU WANT TO CALCULATE?*****\n")
#     print("1. FSPL")
#     print("2. Noise Denisty")
#     print("3. Quit")

#     choice = int(input("\nEnter your choice : ")) 
#     if(choice==1):
#         ans = FSPL()
#         print(f"The value of FSPL is {ans} dB")
#     elif(choice==2):
#         ans = Noise_density()
#         print(f"The value of Noise Density is {ans} dB")
#     elif(choice==3):
#         exit()
#     else:
#         print("Wrong Choice")


while(1):
    print("\n*****WHAT DO YOU WANT TO CALCULATE?*****\n")
    print("1. FSPL")
    print("2. Noise Denisty")
    print("3. Quit")

    choice = int(input("\nEnter your choice : "))
    if(choice==1):
        ans = FSPL()
        print(f"The value of FSPL is {ans} dB\n\n")
        # break
    elif(choice==2):
        ans = Noise_density()
        print(f"The value of Noise Density is {ans} dB\n\n")
    elif(choice==3):
        print("\n*****THANK YOU*****\n")
        exit()
    else:
        print("Wrong Choice")
