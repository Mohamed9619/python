
from concurrent.futures.process import _python_exit
from pickle import TRUE



class people:
    def __init__(self, name, id, phone, email, location):
        self.name = name
        self.id = id 
        self.phone = phone
        self.email = email
        self.location = location 

class students(people):
	students_list =[]
	def __init__(self, name, id, phone, email, location, fees, grade):
		super().__init__(name, id, phone, email, location)
		self.__class__.students_list.append(self)
		self.fees = fees
		self.grade = grade
		self.__str__ = f'''
Name          : {self.name}
Student ID    : {self.id}
Phone         : {self.phone}
Email         : {self.email}
Location      : {self.location}
fees          : {self.fees}
grade         : {self.grade}'''

	def student_by_id(self,student_id):
		for student in self.students_list:
			if student.id == student_id:
				return student
		raise Exception('Not Found')
        
    	

	__subjectes = []
	__grades = []
	__degree = []
				

	def subject_degree(self, grade):
		if (grade >= 90) :
			return 'A'
		elif (grade >= 80) and (grade < 90):
			return 'B'
		elif (grade >= 70) and (grade < 80):
			return 'C'
		elif (grade >= 60) and (grade < 70):
			return 'D'
		else:
			return 'F'
	
	def subject_add(self,subject,grade):
		self.__subjectes.append(subject)
		self.__grades.append(grade)
		self.__degree.append(self.subject_degree(grade))
		print(" subject is : "+self.__subjectes[-1]+" score : "+self.__grades[-1] + " grade : "+self.__degree[-1])
	
	def subject_mod(self,subject,new_grade):
		i = self.__subjectes.index(subject)
		self.__grades[i] = new_grade
		self.__degree[i] = self.subject_degree(new_grade)
		print(" subject is : "+self.__subjectes[i]+" score : "+self.__grades[i] + " grade : "+self.__degree[i])

	def get_grades_percentage(self):
		list_length = len(self.grades)
		i = 0
		sum = 0 
		while i < list_length:
			sum += self.__grades[i]
			i += 1
		avg = (sum/list_length)
		return avg

class teachers(people):
    teachers_list = []
    def __init__(self, name, id, phone, email, location, subjectes, salary):
        super().__init__(name, id, phone, email, location)
        self.__class__.teachers_list.append(self)
        self.subjectes = subjectes
        self.salary = salary
        self.__str__ = f'''
Name          : {self.name}
Teacher ID    : {self.id}
Phone         : {self.phone}
Email         : {self.email}
Location      : {self.location}
Salary        : {self.salary}
Subjects      : {self.subjects}'''
    def teacher_by_id(self,teacher_id):
        for teacher in self.teachers_list:
            
            if teacher.id == teacher_id:
                return teacher
        raise Exception('Not Found')


def checking_input(input_val,input_type):
	if input_type == 'phone':
		try:
			int(input_val)
			return True
		except:
			return False
	elif input_type in ['salary','fees']:
		try:
			float(input_val)
			return True
		except:
			return False
	elif input_type == 'subjects':
		if type(input_val) is list:
			return True
		else:
			return False


def add_student():
	while TRUE:
		name=input("please enter student name : ")
		id=input("please enter student id : ")
		while TRUE:
			phone=input("please enter a student phone number starting with +  : ")
			check=checking_input(phone,'phone')
			if check:
				break
			else:
				print("wrong phone number format: ")
		email=input(" please enter student email: ")
		location=input("please enter student location: ")
		while TRUE:
			fees=input("please enter tuition fees : ")
			check=checking_input(fees,'fees')
			if check:
				break
			else:
				print("you entered wrong format of fees")
		grade=input("please enter student grade : ")
		students(name,id,phone,email,location,fees,grade)
		student_=students.student_by_id(id)
		print(student_.__str__)
		flag=input("please press q to quit ")

		if flag.lower() == 'q':
			break
		else :
			print("continue to create another student \n")
			


def add_teacher():
	while TRUE:
		name=input("please enter teacher name : ")
		id=input("please enter teacher id : ")
		while TRUE:
			phone=input("please enter a student phone number starting with +  : ")
			check=checking_input(phone,'phone')
			if check:
				break
			else:
				print("wrong phone number format: ")
		email=input(" please enter teacher email: ")
		location=input("please enter teacher location: ")
		while TRUE:
			subjectes=input("please enter subjectes to teach in a list of strings  : ")
			check=checking_input(subjectes,'subjects')
			if check:
				break
			else:
				print("you entered wrong format of subjectes")
		while TRUE:
			salary=input("please enter teacher salary : ")
			check=checking_input(salary,'salary')
			if check:
				break
			else:
				print("you entered wrong format of salary")
		flag=input("please press q to quit ")
		teachers(name,id,phone,email,location,subjectes,salary)
		if flag.lower() == 'q':
			break
		else :
			print("continue to create another student \n")




		
	



		

