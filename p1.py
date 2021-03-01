nominee_1 = input("enter the nominee 1 name:")
nominee_2 = input("enter the nominee 2 name:")

nom_1_votes = 0          # initialy nominee1 has 0 vote
nom_2_votes = 0           ## initialy nominee2 has 0 vote
votes_id = [1,2,3,4,5,6,7,8,9,10]
num_of_voters = len(votes_id)

while True :
    if votes_id==[]:     # all the voters voted , all votes id removed so list is empty
        print("voting session is over")
        if nom_1_votes > nom_2_votes:     #chk for nominee1 win check which nominees won and got how many percentage votes
            percent=(nom_1_votes/num_of_voters)*100
            print(nominee_1 ,"has won","with",percent,"% votes")
            break
        elif nom_2_votes > nom_1_votes:     #chk for nominee2 win check which nominees won and got how many percentage votes
            percent=(nom_2_votes/num_of_voters)*100
            print(nominee_2,"has won","with",percent,"% votes")   
            break 


    else:
            
        voter=int(input("enter your voter id number:"))
        if voter in votes_id:                   #if entered id by voter matche mith voters id then he is valid voter.
            print("you are the voter")
            votes_id.remove(voter)               # after giving one time vote voter id will remove from list.
            vote=int(input("enter your vote 1 or 2:"))
            if vote==1:
                nom_1_votes+=1
                print("Thank you for casting your vote")       # voter give vote 1 then incriment by 1 in nom__1_votes
            elif vote==2:
                nom_2_votes+=1        # voter give vote 2 then incriment by 1 in nom__2_votes
                print("Thank you for casting your vote")    
        else:
            print(" you are not voter here or you have all rady voted")
