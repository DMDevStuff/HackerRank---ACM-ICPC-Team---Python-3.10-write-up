##    https://www.hackerrank.com/challenges/acm-icpc-team/problem
##
##    There are a number of people who will be attending ACM-ICPC World
##    Finals. Each of them may be well versed in a number of topics. Given a
##    list of topics known by each attendee, presented as binary strings,
##    determine the maximum number of topics a 2-person team can know. Each
##    subject has a column in the binary string, and a '1' means the subject
##    is known while '0' means it is not. Also determine the number of teams
##    that know the maximum number of topics. Return an integer array with two
##    elements. The first is the maximum number of topics known, and the
##    second is the number of teams that know that number of topics.

##### ##### ##### #####

#   O(n*n*m)
#   n is the number of people
#   m is the number of topics

#   Idea:
#       bruteforce

#   Algo:
#       1. initiate a variable to store the max number of topics
#           known by a team => O(1)
#       2. initiate a variable to store the number of teams that
#           know the max number of topics = O(1)
#       3. using nested for loops iterate over every 'person a'
#           and every possible partner 'person b' => O(n*n)
#       4. for every possible pair, compare the topics they know,
#           a seperate function is used for this => O(m)
#       5. compare results to current most topics known, increment
#           if necessary, disregard otherwise => O(1)
#       6. return most topics known and the number of teams that know that number => O(1)

def topicsKnown(person_a, person_b):
    
    topics_known = 0
    
    for index in range(len(person_a)):
        
        if person_a[index] == '1' or person_b[index] == '1':
            
            topics_known += 1
            
    return topics_known
        

def acmTeam(topic):
    
    most_topics_known = 0
    number_of_teams = 0
    
    for person_a in range(len(topic) - 1):
        
        for person_b in range(person_a + 1, len(topic)):
            
            topics_known = topicsKnown(topic[person_a], topic[person_b])
            
            if topics_known > most_topics_known:
                
                most_topics_known = topics_known
                number_of_teams = 1
                
            elif topics_known == most_topics_known:
                
                number_of_teams += 1
                
    return [most_topics_known, number_of_teams]
