import urllib.request
import re
#first_url = http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
#number = 44827
nothing="12345"
num=('')
for i in range (300):
    print(i)
    print ("this is current",nothing)
    url_1 = urllib.request.urlopen(f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}")
    read_content = url_1.read()
    print('this is what I have read :',read_content) 
    a = str(read_content)
    words = a.split()
    if len(words) != 6:
        new = input("new text detected. user input required:  next nothing or 'stop' to exit  ")
        if new =="stop":
            break
        nothing = new
        continue
    b = re.findall('[\d]',a)
    now = num.join(b)
    print(f"this is the isolated numbers",{now})
    nothing = now
    


    
