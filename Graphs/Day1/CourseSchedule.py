import collections
from collections import defaultdict
def canFinish(numCourses, prerequisites):
    courses = collections.defaultdict(set)
    pres = collections.defaultdict(set)
    for i,j in prerequisites:
        courses[i].add(j)
        pres[j].add(i)
    no_pre_courses=[k for k in range(numCourses) if not courses[k]]
    count=0
    while(no_pre_courses):
        count+=1
        no_pre=no_pre_courses.pop()
        for course in pres[no_pre]:
            courses[course].remove(no_pre)
            if not courses[course]:
                no_pre_courses.append(course)
    return count==numCourses

n=2
p=[[1,0],[0,1]]
print(canFinish(n,p))
        

