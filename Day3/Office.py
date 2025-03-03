from database import Database
class Office:
    num_emp = 0
    def __init__(self,name,employees,db):
        self.name = name
        self.employees = employees
        self.db = db
        self.cursor = self.db.cursor
        self.num_emp+=1

    def get_all_employees(self):
        self.cursor.execute("select * from employee")
        return self.cursor.fetchall()

    def get_employee(self,id):
        self.cursor.execute("SELECT * FROM employee WHERE id = %s", (id,))
        result = self.cursor.fetchone()
        return result

    def hire(self,name, healthRate, email, distanceToWork, salary):
        self.cursor.execute("INSERT INTO employee (name, healthRate, email, distanceToWork, salary) VALUES (%s, %s, %s, %s, %s)",(name, healthRate, email, distanceToWork, salary))
        self.db.conn.commit()
        print(f"{name} has been hired.")

    def fire(self,id):
        self.cursor.execute("delete from employee where id =%s",(id,))
        self.db.conn.commit()
        print(f"Employee {id} has been fired.")

    # -deduct (empId, deduction): Method in Office Class (Deduce Money from salary from Employee)
    def deduct(self,id,deduction):
        self.cursor.execute("select salary from employee where id =%s",(id,))
        result= self.cursor.fetchone()  
        salary_for_emp = result[0]
        if (salary_for_emp-deduction) > 0:
            new_salary = salary_for_emp - deduction 
        else:
            print("faild the deduction is bigger than salary !")
        
        self.cursor.execute("update employee set salary = %s where id = %s",(new_salary,id))
        self.db.conn.commit()
        print (f"{deduction} was deducted from employee {id}'s salary.")

    def reward(self,id,reward):
        self.cursor.execute("select salary from employee where id =%s",(id,))
        result= self.cursor.fetchone()  
        salary_for_emp = result[0]
        # if (salary_for_emp-deduction) > 0:
        new_salary = salary_for_emp + reward 
        # else:
        #     print("faild the deduction is bigger than salary !")
        
        self.cursor.execute("update employee set salary = %s where id = %s",(new_salary,id))
        self.db.conn.commit()
        print (f"{reward} was rewarded to employee {id}'s salary.")

    def check_lateness(self,id,moveHour,deadline):
        # office.get_employee(3)
        employee = self.get_employee(id)
       
        distanceToWork = employee[3]  
        velocity = 50  
        time = self.calc_distance(employee.distanceToWork,employee.velocity)
        if time + moveHour > deadline:
            print(f"Employee {id} was late. -10 deducted.")
            self.deduct(id,10)
        else:
            print(f"Employee {id} was on time. +10 rewarded.")
            self.reward(id,10)

    def calc_distance(self,distance,velocity):
        time = distance / velocity  

    # def get_num_employees(self):
    #     self.cursor.execute("SELECT COUNT(*) FROM employee")
    #     return self.cursor.fetchone()[0] 
    def get_num_employees(self):
        self.cursor.execute("select count(*) from employee")
        return self.cursor.fetchone()[0]
    

    # num_emp = get_num_employees(self=None)
db = Database()
office = Office("TechCorp", 50, db)
num_emp = office.get_num_employees()
print(f"Number of Employees : {num_emp}")
# # office.reward(6,1000)
# office.check_lateness(1,2,9)
# employees = office.get_all_employees()
# emp = office.get_employee(3)
print(office.num_emp)
# print(emp)
# print(office.)
# for emp in employees:
#     print(emp)
# office.fire(1)
# office.hire("mohamed mustafa",70,"mohamed@gmail.com",200,4000)