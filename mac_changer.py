
import sys
import os
import time


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)
slowprint('''\033[1;31m \033[91m    
       __  ___                 ________                               
      /  |/  /___ ______      / ____/ /_  ____ _____  ____ ____  _____
     / /|_/ / __ `/ ___/_____/ /   / __ \/ __ `/ __ \/ __ `/ _ \/ ___/
    / /  / / /_/ / /__/_____/ /___/ / / / /_/ / / / / /_/ /  __/ /    
   /_/  /_/\__,_/\___/      \____/_/ /_/\__,_/_/ /_/\__, /\___/_/     
                                                   /____/\033[97m             
''')
print(" ")
print("1- Show the current MAC-ADDRESS")
print("")
print("2- Change your MAC-ADDRESS Randomly")
print("")
print("3- Change your MAC-ADDRESS Customly")
print("")
print("4- Reset the original MAC-ADDRESS")
print("")
input=input("\033[92m[?] \033[96mmake your choise ==>")
if input==('1') :
            print(" ")
            print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
            print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
            print(" ")
            current_mac=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
            if current_mac==('1') :
                      slowprint("\033[97m")
                      os.system('macchanger -s wlan0')
                      print(" ")
                      done=input('press any key to continue')
                      os.system('clear') 
                      os.system('python3 mac.py')
            if current_mac==('2') :
                       slowprint("\033[97m")
                       os.system('macchanger -s eth0')
                       print(" ")
                       doneh=input('press any key to continue')
                       os.system('clear')
                       os.system('python3 mac.py')

if input==('2') :
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               random_mac=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if random_mac==('2') :
                        slowprint("")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -r eth0')
                        os.system('ifconfig eth0 up')
                        print(" ")
                        done=input("press any key to continue")
                        os.system('clear')
                        os.system('python3 mac.py')
               if random_mac==('1') :
                        slowprint("")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -r wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ")
                        done=input("press any key to continue")
                        os.system('clear')
                        os.system('python3 mac.py')

if input==('4'): 
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connexion)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               orginal_mac=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if orginal_mac==('2') :
                        print(" ")
                        slowprint("\033[97m")
                        os.system('macchanger -p eth0')
                        print(" ") 
                        done=input("press any key to continue ")
                        os.system('clear')
                        os.system('python3 mac.py')
               if orginal_mac==('1') : 
                        print(" ")
                        slowprint("\033[97m")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -p wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ") 
                        done=input("press any key to continue ")
                        os.system('clear')
                        os.system('python3 mac.py')


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)

if input==('3'):
               print(" ")
               print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( WIFI connection)")
               print("\033[94m2 \033[97m- \033[91meth0 \033[97m( CABLE connection)")
               print(" ")
               cus_mac=input("   \033[95m[?] \033[97menter your \033[91mconnection type \033[97m:")
               if cus_mac==('2') :
                        print(" ")
                        os.system('ifconfig eth0 down')
                        addr=input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -m'+(addr)+' eth0')
                        os.system('ifconfig eth0 up')
                        print("done")
               if cus_mac==('1') : 
                        os.system('ifconfig wlan0 down')
                        print(" ")
                        addr=input("\033[95m[?] \033[97menter THE NEW \033[92mMAC-ADDRESS \033[97m: ")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -m'+(addr)+' wlan0')
                        os.system('ifconfig wlan0 up')
                        print("done")