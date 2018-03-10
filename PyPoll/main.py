import os,csv
       
###########################
###########################
###########################
# Start of main program
###########################
###########################
###########################
def VoteAnalysis(file_name):
    VoteCount=0
    Candidates=[]
    lcandidate=[]
    lcounty=[]

    with open(file_name,newline='',encoding='utf-8') as input_file:
        file_reader=csv.reader(input_file,delimiter=",")
        next(file_reader, None)
        for row in file_reader:
            VoteCount+=1
            County=row[1]
            Candidate=row[2]
            Candidates.append([County,Candidate])  
            lcandidate.append(row[2])
            lcounty.append(row[1])


    #print(Candidates)
    for can,con in zip(lcandidate,lcounty):
        print(can+" "+con)
        
for root, dirs, files in os.walk("raw_data"):
    for file in files:
        if file.endswith(".csv"):
             #print(os.path.join(root, file))
             VoteAnalysis(os.path.join(root, file))