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
    colleges = load_colleges()

    for c in colleges:
        if c["College Code"].lower() == college["College Code"].lower():
            return False

    with open(college_File, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=college_Fields)
        writer.writerow(college)
    return True

def update_college(old_code:str,updated: dict):
    colleges = load_colleges()
    found = False
    new_code = updated["College Code"]

    if old_code != new_code:
        for c in colleges:
            if c["College Code"] != old_code and c["College Code"].lower() == new_code.lower():
                return False
            
    for i, college in enumerate(colleges):
            if college["College Code"] == old_code:
                colleges[i] = updated
                found = True
                break

    if not found:
        return False
    
    save_colleges(colleges)

    if old_code != new_code:
        programs = load_programs()
        changed = False
        for p in programs:
            if p["College Code"] == old_code:
                p["College Code"] = new_code
                changed = True
        if changed:
            save_programs(programs)

    return True
    
def delete_college(college_code: str):
    colleges = load_colleges()
    colfiltered = [c for c in colleges if c["College Code"] != college_code]
    if len(colfiltered) == len(colleges):
        return False
    
    programs = load_programs()
    for p in programs:
        if p["College Code"] == college_code:
            p["College Code"] = "N/A"
    save_programs(programs)

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
    programs = load_programs()

    for p in programs:
        if p["Program Code"].lower() == program["Program Code"].lower():
            return False 
        
    with open(program_File, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=program_Fields)
        writer.writerow(program)
    return True

def save_programs(program: list):
    with open(program_File, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=program_Fields)
        writer.writeheader()
        writer.writerows(program)

def update_program(old_code: str, updated: dict):
    programs = load_programs()
    found = False
    new_code = updated["Program Code"]

    if old_code != new_code:
        for p in programs:
            if p["Program Code"] != old_code and p["Program Code"].lower() == new_code.lower():
                return False

    for i, program in enumerate(programs):
        if program["Program Code"] == old_code:
            programs[i] = updated
            found = True
            break

    if not found:
        return False

    save_programs(programs) 

    if old_code != new_code:
        students = load_students()
        changed = False
        for s in students:
            if s["Program Code"] == old_code:
                s["Program Code"] = new_code
                changed = True
        if changed:
            save_students(students)

    return True
     
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
    students = load_students()

    for s in students:
        if s["Student ID"].lower() == student["Student ID"].lower():
            return False

    with open(student_File, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=student_Fields)
        writer.writerow(student)
    return True

def update_student(old_id: str,updated: dict):
    students = load_students()
    found = False
    new_id = updated["Student ID"]

    if old_id != new_id:
        for s in students:
            if s["Student ID"] != old_id and s["Student ID"].lower() == new_id.lower():
                return False

    for i, student in enumerate(students):
        if student["Student ID"] == old_id:
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
