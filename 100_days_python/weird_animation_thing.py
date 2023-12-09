import os, time, sys
def clear():
    os.system('cts' if os.name == 'nt' else 'clear')
print("how many FPS do you want?")
fps = int(input())
type_of_animation = input("what type of animation do you want? "
                          "choose from GDWave, spinning or piston\n").lower()

if type_of_animation == "ripple":
    for i in range(0, 30):
        print("|")
        time.sleep((1/fps))
        print("||")
        time.sleep((1/fps))
        print("|||")
        time.sleep((1/fps))
        print("||||")
        time.sleep((1/fps))
        print("|||||")
        time.sleep((1/fps))
        print("||||")
        time.sleep((1/fps))
        print("|||")
        time.sleep((1/fps))
        print("||")
        time.sleep((1/fps))
    print("|")
    sys.exit
def wait():
    time.sleep(1/fps)
if type_of_animation == "spinning":
    for i in range(0, 30):
        for _ in range(0, 3):
            print("""  |
  |
  |""")
            wait()
            clear()
            print(""" \\
  \\
   \\""")
            wait()
            clear()
            print("""\n------\n""")
            wait()
            clear()
            print("""   /
  /
 /""")
            wait()
            clear()           

    
    
