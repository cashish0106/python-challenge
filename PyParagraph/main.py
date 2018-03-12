import os,csv,re
       
def num_sentence(input_txt):
#    p=re.compile(r'\b[a-z]+\b', re.IGNORECASE)

    p=re.compile("(?<=[.!?]) +")   
    match=p.split(input_txt)
    print(len(match))
    print(match)

def num_words(input_txt):
    p=re.compile(r'\b[a-z]{2,}\b', re.IGNORECASE)
    match=p.split(input_txt)
    print(len(match))
    #print(match)
   
    
###########################
###########################
###########################
# Start of main program
###########################
###########################
###########################

for root, dirs, files in os.walk("raw_data"):
    for file in files:
        if file.endswith(".txt"):
             #print()
            if_name, f_ext = os.path.splitext(os.path.basename(os.path.join(root, file))) # parsing file name to create output for each input file
            with open(os.path.join(root, file),newline='',encoding='utf-8') as input_file:
                pgrph=input_file.read()
                print(pgrph)
               # num_words(pgrph)
                num_sentence(pgrph.strip())
