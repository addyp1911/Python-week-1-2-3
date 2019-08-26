def calculateChange(bill):
    notes=[1000,500,100,50,20,10,5,2,1]
    notes_counter=[]
    for i in range(0,9):
        if(bill>=notes[i]):
            notes_counter.append(bill//notes[i])
            bill=bill-notes[i]*notes_counter[i]
        else:
            notes_counter.append(0)    


    for i in range(0,9):
        if(notes_counter[i]!=0):
            print(notes[i], notes_counter[i] ) 