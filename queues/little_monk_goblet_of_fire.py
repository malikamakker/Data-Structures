'''
Albus Dumbledore announced that the school will host
the legendary event known as Wizard Tournament where
four magical schools are going to compete against each
other in a very deadly competition by facing some dangerous
challenges. Since the team selection is very critical
in this deadly competition. Albus Dumbledore asked Little
Monk to help him in the team selection process. There is a
long queue of students from all the four magical schools.
Each student of a school have a different roll number.
Whenever a new student will come, he will search for his
schoolmate from the end of the queue. As soon as he will find
any of the schoolmate in the queue, he will stand behind him,
otherwise he will stand at the end of the queue. At any moment
Little Monk will ask the student, who is standing in front of
the queue, to come and put his name in the Goblet of Fire and
remove him from the queue. There are Q operations of one of the following types:

E x y: A new student of school x  whose roll number is y  will stand
in queue according to the method mentioned above.

D: Little Monk will ask the student, who is standing in front of the queue,
to come and put his name in the Goblet of Fire and remove him from the queue

Sample Input
5
E 1 1
E 2 1
E 1 2
D
D

Sample Output
1 1
1 2
'''


ordering_of_schools = []
ordering = [[], [], [], []]

q = int(input())

for i in range(q):
    query = input().split(' ')

    if query[0] == 'E':
        school = int(query[1])
        roll_no = int(query[2])

        if len(ordering[school - 1]) == 0:
            ordering_of_schools.append(school)

        ordering[school - 1].append((school, roll_no))

    if query[0] == 'D':
        pair = ordering[ordering_of_schools[0] - 1][0]
        ordering[ordering_of_schools[0] - 1].pop(0)

        if len(ordering[pair[0] - 1]) == 0:
            ordering_of_schools.pop(0)

        print(str(pair[0]) + " " + str(pair[1]))
