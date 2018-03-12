import os,csv
       
def exportTofile(f_name,t_count,c_votes):
    with open(os.path.join("Output",f_name+"_result.txt"),"w+") as output_file:
        winner=""
        votes=0
        print("Election Results")
        print("----------------")
        print("Total Votes: "+str(t_count))
        print("----------------")
        output_file.write("Election Results")
        output_file.write("\n----------------")
        output_file.write("\nTotal Votes: "+str(t_count))
        output_file.write("\n----------------\n")

        for keys,values in c_votes.items():
            print(keys+": "+str(round(values/t_count*100,1))+"% ("+str(values)+")")
            output_file.write(keys+": "+str(round(values/t_count*100,1))+"% ("+str(values)+")\n")
            if(votes > int(values)):
                votes=votes
            else:
                votes=int(values)
                winner=keys    
        
        print("----------------")
        print("Winner: "+winner)
        print("----------------")
        output_file.write("----------------\n")
        output_file.write("Winner: "+winner)
        output_file.write("\n----------------")

def VoteAnalysis(file_name):
    total_vote_count=0 #To count total votes
    candidate_votes={} #Dictionary to store each candidate's vote count
    f_name, f_ext = os.path.splitext(os.path.basename(file_name)) # parsing file name to create output for each input file

    with open(file_name,newline='',encoding='utf-8') as input_file:
        file_reader=csv.reader(input_file,delimiter=",")
        next(file_reader, None)
        for row in file_reader:
            total_vote_count+=1
            if(candidate_votes):
                #If dictionary is initilze then check vot count is updated for that candidate
                if(candidate_votes): 
                        #check if candidate is already available in dictionary. If yes then increase count
                        if (str(row[2].strip()) in candidate_votes):
                            candidate_votes[row[2].strip()]=int(candidate_votes[row[2]])+1
                        else:
                            #for first occurence initilize count as 1
                            candidate_votes[row[2].strip()]=1
                else:
                    #for first occurence initilize count as 1
                    candidate_votes[row[2].strip()]=1       
            else:
                candidate_votes[row[2].strip()]=1
 
    
    exportTofile(f_name,total_vote_count,candidate_votes)
###########################
###########################
###########################
# Start of main program
###########################
###########################
###########################

for root, dirs, files in os.walk("raw_data"):
    for file in files:
        if file.endswith(".csv"):
             #print(os.path.join(root, file))
             VoteAnalysis(os.path.join(root, file))