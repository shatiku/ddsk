import random

def main():
    str_ddsk = ["どど","すこ"]
    str_love = "LOVE注入♡"
    str_buf = ""
    str_ddsksksk = str_ddsk[0] + str_ddsk[1] + str_ddsk[1] + str_ddsk[1]
    str_end = str_ddsksksk + str_ddsksksk + str_ddsksksk
    i = 0
    while(True):
        str_random = str_ddsk[random.randint(0,1)]
        i += 1
        print(str_random,end = "")
        str_buf += str_random
        if(str_buf[-(str_end.__len__()):] == str_end):
            print("\n" + i.__str__() + "回目に " + str_buf[-(str_end.__len__()):] + " " + str_love)
            input("Please press any keys to quit.")
            break        

if __name__ == '__main__':
    main()