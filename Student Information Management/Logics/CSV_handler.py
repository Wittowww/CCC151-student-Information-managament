import csv
import os 

baseDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                          
student_File = os.path.join(baseDIR, "Data", "students.csv")
college_File = os.path.join(baseDIR, "Data", "colleges.csv")
program_File = os.path.join(baseDIR, "Data", "programs.csv")

#headers
student_Fields = ["Student ID" , "Last Name", "First Name", "Gender", "Program Code", "Year"]
college_Fields = ["College Code", "College Name"]
program_Fields = ["Program Code", "Program Name", "College Code"]

"""Everything needs to be updated, all need to be connected or related to each other"""
"""if one is deleted it needs to be relfected to the other all CRUDL"""
"""isn't runn yet"""

def CSV_initialize():

    FILES = {
        student_File: student_Fields,
        college_File: college_Fields,
        program_File: program_Fields
    }

    for file, fields in FILES.items():
        if not os.path.exists(file):
            with open(file, mode='w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()

#COLLEGE
def load_colleges():
    CSV_initialize()
    with open(college_File, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def add_college(college: dict):
    with open(college_File, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=college_Fields)
        writer.writerow(college)

def update_college(updated: dict):
    colleges = load_colleges()
    found = False
    for i, college in enumerate(colleges):
        if college["College Code"] == updated["College Code"]:
            colleges[i] = updated
            found = True
            break
    if found:
        save_colleges(colleges)
        return True
    else:
        return False
    
def delete_college(college_code: str):
    colleges = load_colleges()
    colfiltered = [c for c in colleges if c["College Code"] != college_code]
    if len(colfiltered) == len(colleges):
        return False
    
    programs = load_programs()
    delete_programCode = [p["Program Code"] for p in programs if p["College Code"] == college_code]
    filtered_program = [p for p in programs if p["College Code"] != college_code]
    save_programs(filtered_program)

    student = load_students()
    for student in student:
        if student["Program Code"] in delete_programCode:
            student["Program Code"] = "N/A"
    save_students(student)
    
    save_colleges(colfiltered)
    return True

def save_colleges(colleges:list):
    with open(college_File, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=college_Fields)
        writer.writeheader()
        writer.writerows(colleges)

def search_colleges(keyword: str):
    colleges =load_colleges()
    keyword = keyword.lower()
    results = [
        c for c in colleges
        if keyword in c["College Code"].lower() or
            keyword in c["College Name"].lower()
    ]
    return results

def get_college(college_code: str):
    colleges = load_colleges()
    for college in colleges:
        if college["College Code"] == college_code:
            return college
    return None


#PROGRAM
def load_programs():
    CSV_initialize()
    with open(program_File, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)    
    
def add_program(program: dict):
    with open(program_File, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=program_Fields)
        writer.writerow(program)

def save_programs(program: list):
    with open(program_File, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=program_Fields)
        writer.writeheader()
        writer.writerows(program)

def update_program(updated: dict):
    programs = load_programs()
    found = False

    for i, program in enumerate(programs):
        if program["Program Code"] == updated["Program Code"]:
            programs[i] = updated
            found = True
            break
    if found:
        save_programs(programs)
        return True
    else:
        return False  
     
def delete_program(program_code: str):
    programs = load_programs()
    profiltered = [p for p in programs if p["Program Code"] != program_code]

    if len(profiltered) == len(programs):
        return False
    
    students =load_students()
    for student in students:
        if student["Program Code"] == program_code:
            student["Program Code"] = "N/A"
    save_students(students)

    save_programs(profiltered)
    return True

def search_programs(keyword: str):
    programs = load_programs()
    keyword = keyword.lower()
    results = [
        p for p in programs
        if keyword in p["Program Code"].lower() or
            keyword in p["Program Name"].lower()
    ]
    return results

def get_program(program_code: str):
    programs = load_programs()
    for program in programs:
        if program["Program Code"] == program_code:
            return program
    return None


#STUDENT 
def load_students():
    CSV_initialize()
    with open(student_File, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        return list(reader)
    
def add_student(student: dict):
    with open(student_File, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=student_Fields)
        writer.writerow(student)

def update_student(updated: dict):
    students = load_students()
    found = False
    for i, student in enumerate(students):
        if student["Student ID"] == updated["Student ID"]:
            students[i] = updated
            found = True
            break
    if found:
        save_students(students)
        return True
    else:
        return False
    
def delete_student(student_ID: str):
    students = load_students()
    stufiltered = [s for s in students if s["Student ID"] != student_ID]
    if len(stufiltered) == len(students):
        return False
    save_students(stufiltered)
    return True  

def save_students(students: list):
    with open(student_File, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=student_Fields)
        writer.writeheader()
        writer.writerows(students)

def search_students(keyword: str):
    students = load_students()
    keyword = keyword.lower()
    results = [
        s for s in students
        if keyword in s["Student ID"].lower() or
            keyword in s["Last Name"].lower() or
            keyword in s["First Name"].lower()
    ]
    return results

def get_student(student_ID: str):
    students = load_students()
    for student in students:
        if student["Student ID"] == student_ID:
            return student
    return None
