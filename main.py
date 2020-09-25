

import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    def __init__(self, cid, cname, credits):
        # YOUR CODE STARTS HERE
        self.cid = cid
        self.cname = cname
        self.credits = credits


    def __str__(self):
        return f"{self.cid}({self.credits}) : {self.cname}"

    def __repr__(self):
        return f"{self.cid}({self.credits}) : {self.cname}"

    def __eq__(self, other):
        if(other is None):
            return False
        if(self.cid==other.cid):
            return True
        else:
            return False
    def isValid(self):
        if(type(self.cid)==str and type(self.cname)==str and type(self.credits)==int):
            return True
        return False


class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'CMPSC360': CMPSC360(3): Discrete Mathematics}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': CMPSC132(3): Programming in Python II}
    '''
    def __init__(self):
        self.courseOfferings = {}

    def addCourse(self, cid, cname, credits):
        self.courseOfferings[cid] = Course(cid,cname,credits)
        return "Course Added successfully"

    def removeCourse(self, cid):
        del self.courseOfferings[cid]
        return "Course removed successfully"



class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132(3): Programming in Python II, MATH 230(4): Calculus
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.addCourse(Course(42, 'name',"zero credits"))
        'Invalid course'
        >>> semester.courses
        [CMPSC132(3): Programming in Python II, MATH 230(4): Calculus, PHYS 213(2): General Physics, ECON 102(3): Intro to Economics, JAPNS 001(4): Japanese I]
    '''

    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = []

    def __str__(self):
        if(len(self.courses)==0):
            return "No courses"
        else:
            formattedS = ""
            for course in self.courses:
                formattedS += str(course)
                formattedS += ","
            return formattedS

    def __repr__(self):
        if(len(self.courses)==0):
            return "No courses"
        else:
            formattedS = ""
            for course in self.courses:
                formattedS += str(course)
                formattedS += ","
            return formattedS

    def addCourse(self, course):
        if(not isinstance(course,Course) or not course.isValid()):
            return "Invalid Course"
        if(course in self.courses):
            return "Course already added"
        else:
            self.courses.append(course)

    def dropCourse(self, course):
        if(not isinstance(course,Course) or not course.isValid()):
            return "Invalid Course"
        if(course not in self.courses):
            return "No such course"
        else:
            self.courses.remove(course)

    @property
    def totalCredits(self):
        totalcredit = 0
        for course in self.courses:
            totalcredit += course.credits
        return totalcredit
        
    @property
    def isFullTime(self):
        if(self.totalCredits>=12):
            return True
        return False




class Loan:
    '''
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC360', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        'Not full-time'
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> s1.getLoan(4000)
        >>> s1.account.loans
        {27611: Balance: $4000}
        >>> s1.getLoan(6000)
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $6000}
    '''
    

    def __init__(self, amount):
        self.loan_id = self.__loanID
        self.amount = amount

    def __str__(self):
        return f"Balance: {self.amount}"

    def __repr__(self):
        return f"Balance: {self.amount}"

    @property
    def __loanID(self):
        return random.randint(10000,99999)




class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn

    def __str__(self):
        return f"Person({self.name},***-**-{self.get_ssn()[-4:]}"

    def __repr__(self):
        return f"Person({self.name},***-**-{self.get_ssn()[-4:]}"

    def get_ssn(self):
        return self.__ssn

    def __eq__(self, other):
        if(self.get_ssn()==other.get_ssn()):
            return True
        return False



class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> st1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
    '''
    def __init__(self, name, ssn, supervisor=None):
        Person.__init__(self,name,ssn)
        self.supervisor = supervisor

    def __str__(self):
        return f"Staff({self.name},{self.id})"
    def __repr__(self):
        return f"Staff({self.name},{self.id})"

    @property
    def id(self):
        return "905" +  self.name.split()[0][0].lower() + self.name.split()[1][0].lower() + self.get_ssn()[-4:]

    @property   
    def getSupervisor(self):
        return self.supervisor

    def setSupervisor(self, new_supervisor):
        if(type(new_supervisor)!="Staff"):
            return None
        else:
            self.supervisor = new_supervisor
            return "Completed"

    def applyHold(self, student):
        if(not isinstance(student,Student)):
            return None
        else:
            student.hold = True
            return "Completed"

    def removeHold(self, student):
        if(not isinstance(student,Student)):
            return None
        else:
            student.hold = False
            return "Completed"

    def unenrollStudent(self, student):
        if(not isinstance(student,Student)):
            return None
        else:
            student.active = False
            return "Completed"




class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Sophomore')
        >>> s2
        Student(Karen Lee, kl2670, Sophomore)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II, CMPSC360(3): Discrete Mathematics]}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360', 1)
        'Course not found'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II]}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II], 2: [No courses]}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: [CMPSC132(3): Programming in Python II], 2: [CMPSC360(3): Discrete Mathematics]}
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        Person.__init__(self,name,ssn)
        self.year = year
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()

    def __createStudentAccount(self):
        if(not self.active):
            return None
        return StudentAccount(self)


    @property
    def id(self):
        return self.name.split()[0][0].lower() + self.name.split()[1][0].lower() + self.get_ssn()[-4:]

    def registerSemester(self):
        if(not self.active or self.hold):
           return "Unsuccessful Operation"
        else:
            self.semesters[str(len(self.semesters)+1)] = Semester(len(self.semesters)+1) 


    def enrollCourse(self, cid, catalog, semester):
        if(not self.active or self.hold):
            return "Unsuccessful Operation"

        for ccid in catalog.courseOfferings:
            if(ccid==cid):
                if(catalog.courseOfferings[cid] in self.semesters[str(semester)].courses):
                    return "Course already enrolled"
                self.semesters[str(semester)].courses.append(catalog.courseOfferings[cid])
                self.account.balance += ((self.account.ppc)*(catalog.courseOfferings[cid]).credits)
                return "Course added successfully"
        return "Course not found"

    def dropCourse(self, cid, semester):
        if(not self.active or self.hold):
            return "Unsuccessful Operation"
        for course in semester.courses:
            if(cid==course.cid):
                semester.courses.remove(course)
                self.account.balance -= ((self.account.ppc)*course.credits)
                return "Course Dropped Successfully"
        return "Course not found"

    def getLoan(self, amount):
        l = Loan(amount)
        if(not self.active):
            return "Unsuccessful Operation"
        if(len(self.semesters)==0):
            return "Student is not enrolled in any of semesters yet"
        if(len(self.semesters)>0):
            if(not self.semesters[str(len(self.semesters))].isFullTime):
                return "Not Full-time"
        if(l.loan_id in StudentAccount(self).loans):
            self.account.loans[l.loan_id] += amount
        else:
            self.account.loans[l.loan_id] = amount


class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.makePayment(5000, 27611)
        'Loan Balance: 4000'
        >>> s1.account.makePayment(3000, 27611)
        8900
        >>> s1.account.loans
        {27611: Balance: $1000}
    '''
    
    def __init__(self, student):
        self.student = student
        self.ppc = 1000
        self.balance = 0
        self.loans = {}

    def __str__(self):
        return f"Name: {self.student.name} \n ID: {self.student.id} \n Balance: ${self.balance}"
    def __repr__(self):
        return f"Name: {self.student.name} \n ID: {self.student.id} \n Balance: ${self.balance}"

    def makePayment(self, amount, loan_id=None):
        if(loan_id is None):
            self.balance -= amount
            return self.balance
        else:
            if(loan_id not in self.loans):
                return None
            elif(self.loans[loan_id]<amount):
                return f"Loan Balance : {self.loans[loan_id]}"   
            else:
                self.balance -= amount
                self.loans[loan_id] -= amount
                return self.balance    


    def chargeAccount(self, amount):
        self.balance += amount
        return self.balance



# ######################################################################


def createStudent(person):
    """
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> s = createStudent(p)
        >>> s
        Student(Jason Smith, js2629, Freshman)
    """
    return Student(person.name,person.get_ssn(),"Freshman")
