class Solution(object):
    def numRescueBoats(self, people, limit):
        people.sort()
        list_people=[]
        i=0
        j=len(people)-1
        while i<=j:
           sum_weight=people[i]+people[j]
           if sum_weight<=limit:
               list_people.append((people[i],people[j]))
               i+=1
               j-=1
           elif i==j:
                list_people.append(people[j])
                return len(list_people)
           else:
               list_people.append((people[j]))
               j-=1  
        return len(list_people) 