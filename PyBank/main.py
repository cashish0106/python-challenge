import os,csv
def ExportToFile(f_name,output):
    output_path=os.path.join("Output",f_name+"_final.txt")
    with open(output_path,"w+") as output_file:
        print("\r\r\n")
        print("Financial Analysis")
        output_file.write("Financial Analysis")
        print("----------------------------")
        output_file.write("\n----------------------------")
        print("\r\nTotal Months: "+str(output[5]))
        output_file.write("\r\nTotal Months: "+str(output[5]))
        print("\r\nTotal Revenue: $"+str(output[6]))
        output_file.write("\r\nTotal Revenue: $"+str(output[6]))
        print("\r\nAverage Revenue Change: $"+str(output[7]/output[5]))
        output_file.write("\r\nAverage Revenue Change: $"+str(output[7]/output[5]))
        print("\r\nGreatest Increase in Revenue: "+output[0]+" ($"+str(output[1])+")")
        output_file.write("\r\nGreatest Increase in Revenue: "+output[0]+" ($"+str(output[1])+")")
        print("\r\nGreatest Decrease in Revenue: "+output[2]+" ($"+str(output[3])+")")
        output_file.write("\r\nGreatest Decrease in Revenue: "+output[2]+" ($"+str(output[3])+")")

def FinAnalysis(file_name):
    #str(os.path.basename(file_name))
    #print(os.path.splitext(file_name)[0])
    f_name, file_ext = os.path.splitext(os.path.basename(file_name))
   
    Gr_change=['Jan-01',0,'Jan-01',0,False,0,0,0] # Creating list to record values for greatest increase and decrease
    Pr_data=['Jan-01',0] # This will hold value for previus month

    #print(str(file_name))
    with open(file_name,newline='',encoding='utf-8') as input_file:
        file_reader=csv.reader(input_file,delimiter=",")
        next(file_reader, None)
        for row in file_reader:
            Gr_change[5]+=1 # To Calculate total Month
            Gr_change[6]=Gr_change[6]+int(row[1]) #To calculate total revenue
            if(Gr_change[4]==False):
                Gr_change[0]=row[0] # Date for Greatest Increase
                Gr_change[1]=int(row[1]) # Revenue for Greatest Increase revenue
                Gr_change[2]=row[0] # Date for Greatest Decrease
                Gr_change[3]=int(row[1]) # Revenue for Greatest decrease revenue
                Gr_change[4]=True # This is just to enter first record
                Gr_change[7]=row[1] # This will calculate Average Revenue Change

                #Initilizing Previous month as first one
                Pr_data[0]=row[0]
                Pr_data[1]=int(row[1])

            else:
                # This will find Increase in change of revenue (Month2-Month1)

                if((int(row[1])-int(Pr_data[1]))> int(Gr_change[1])):
                    Gr_change[1]=int(row[1])-int(Pr_data[1])
                    Gr_change[0]=row[0]
                
                # This will find Decrease in change of revenue (Month2-Month1)
                if((int(row[1])-int(Pr_data[1]))< int(Gr_change[3])):
                    Gr_change[3]=int(row[1])-int(Pr_data[1])
                    Gr_change[2]=row[0]
                
                # Adding all monthly revenu change (for average Revenue change)
                Gr_change[7]=int(Gr_change[7]) +(int(row[1])-int(Pr_data[1]))
                
                #Storing previous month values
                Pr_data[0]=row[0]
                Pr_data[1]=row[1]
        # Calling function to write a file
        ExportToFile(f_name,Gr_change)
        
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
             FinAnalysis(os.path.join(root, file))