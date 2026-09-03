class Solution(object):
    def minMovesToSeat(self, seats, students):
        count=0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            count+=abs(students[i]-seats[i])
        return count
