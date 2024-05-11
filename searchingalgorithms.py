from time import perf_counter
def linear_search(students, search_string):
    start = perf_counter()
    matching_students = []

    if not search_string:  
        return students 

    if search_string == "student": 
        return students  

    for student in students:
       
        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)
    end = perf_counter()
    elapsed = end - start        
    return matching_students, elapsed

def binary_search(students, search_string):
    start = perf_counter()
    matching_students = []

    if not search_string:  
        return students  

    if search_string == "student":
        return students  

    
    students.sort(key=lambda x: x.get("firstname", "").lower())
    
    left = 0
    right = len(students) - 1

    while left <= right:
        mid = (left + right) // 2
        student = students[mid]

        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)

        if search_string.lower() < str(student.get("firstname", "")).lower():
            right = mid - 1
        else:
            left = mid + 1
            
    end = perf_counter()
    elapsed = end - start        
    return matching_students, elapsed

def hash_table_search(students, search_string):
    start = perf_counter()
    matching_students = []

    if not search_string:  
        return students  

    if search_string == "student":
        return students 

    hash_table = {}
    for student in students:
        key = hash(student['firstname']) % len(students)
        if key not in hash_table:
            hash_table[key] = []
        hash_table[key].append(student)



    # Search for the student
    search_key = hash(search_string) % len(students)
    if search_key in hash_table:
        for student in hash_table[search_key]:
            if (search_string.lower() in student['firstname'].lower() or
                search_string.lower() in student['lastname'].lower() or
                search_string.lower() in student['date_of_birth'].lower() or
                search_string.lower() in student['gender'].lower() or
                search_string.lower() in student['contact_number'].lower() or
                search_string.lower() in student['email'].lower() or
                search_string.lower() in student['address'].lower() or
                search_string.lower() in student['program'].lower() or
                search_string.lower() in str(student['gpa']).lower() or
                search_string.lower() in str(student['accommodation']).lower()):
                    matching_students.append(student)

    end = perf_counter()
    elapsed = end - start        
    return matching_students, elapsed

def interpolation_search(students, search_string):
    start = perf_counter()
    matching_students = []

    if not search_string:  
        return students 

    if search_string == "student":
        return students  

    low = 0
    high = len(students) - 1

    while low <= high and search_string != "":
        pos = low + int((high - low) * ((ord(search_string[0].lower()) - ord('a')) / (ord('z') - ord('a'))))

        if pos < low or pos > high:
            break

        student = students[pos]

        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)
            break

        if search_string.lower() < student.get("firstname"):
            high = pos - 1
        else:
            low = pos + 1

    end = perf_counter()
    elapsed = end - start        
    return matching_students, elapsed

def ternary_search(students, search_string):
    start = perf_counter()

    matching_students = []

    if not search_string:  
        return students  

    if search_string == "student":
        return students  

    students.sort(key=lambda x: x.get("firstname", "").lower())
    left = 0
    right = len(students) - 1

    while left <= right:
        left_third = left + (right - left) // 3
        right_third = right - (right - left) // 3

        left_student = students[left_third]
        right_student = students[right_third]

        if search_string.lower() in str(left_student.get("firstname", "")).lower():
            right = right_third
        elif search_string.lower() in str(right_student.get("firstname", "")).lower():
            left = left_third
        else:
            
            potential_matches = students[left + 1:right]
            for student in potential_matches:
                if search_string.lower() in str(student.get("firstname", "")).lower() or \
                   search_string.lower() in str(student.get("lastname", "")).lower() or \
                   search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
                   search_string.lower() in str(student.get("gender", "")).lower() or \
                   search_string.lower() in str(student.get("contact_number", "")).lower() or \
                   search_string.lower() in str(student.get("email", "")).lower() or \
                   search_string.lower() in str(student.get("address", "")).lower() or \
                   search_string.lower() in str(student.get("program", "")).lower() or \
                   search_string.lower() in str(student.get("gpa", "")).lower() or \
                   search_string.lower() in str(student.get("accommodation", "")).lower():
                    matching_students.append(student)
            break

    end = perf_counter()
    elapsed = end - start        
    return matching_students, elapsed

def exponential_search(students, search_string):
    start = perf_counter()
    matching_students = []

    if not search_string:  
        return students  # Return all students if the search term is empty

    if search_string == "student":
        return students  # Return all students if the search term is "student"

    # Find the range for binary search
    bound = 1
    while bound < len(students) and search_string.lower() not in str(students[bound].get("firstname", "")).lower():
        bound *= 2

    left = bound // 2
    right = min(bound, len(students) - 1)

    # Perform binary search in the found range
    while left <= right:
        mid = (left + right) // 2
        student = students[mid]

        if search_string.lower() in str(student.get("firstname", "")).lower() or \
           search_string.lower() in str(student.get("lastname", "")).lower() or \
           search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
           search_string.lower() in str(student.get("gender", "")).lower() or \
           search_string.lower() in str(student.get("contact_number", "")).lower() or \
           search_string.lower() in str(student.get("email", "")).lower() or \
           search_string.lower() in str(student.get("address", "")).lower() or \
           search_string.lower() in str(student.get("program", "")).lower() or \
           search_string.lower() in str(student.get("gpa", "")).lower() or \
           search_string.lower() in str(student.get("accommodation", "")).lower():
            matching_students.append(student)

        if search_string.lower() < str(student.get("firstname", "")).lower():
            right = mid - 1
        else:
            left = mid + 1
            
    end = perf_counter()
    elapsed = end - start        
    return matching_students, elapsed

    # if not search_string: 
    #         return students
    # matching_students = []

    # if search_string == "student":
    #     return students  
    # students.sort(key=lambda x: x.get("firstname", "").lower())
    # left = 0
    # right = len(students) - 1

    # while left <= right:
    #     left_third = left + (right - left) // 3
    #     right_third = right - (right - left) // 3

    #     left_student = students[left_third]
    #     right_student = students[right_third]

    # if search_string.lower() in str(left_student.get("firstname", "")).lower():
    #   right = right_third
    # elif search_string.lower() in str(right_student.get("firstname", "")).lower():
    #   left = left_third
    # else:
     
    #     potential_matches = students[left + 1:right]
    #     for student in potential_matches:
    #         if search_string.lower() in str(student.get("firstname", "")).lower() or \
    #             search_string.lower() in str(student.get("lastname", "")).lower() or \
    #             search_string.lower() in str(student.get("date_of_birth", "")).lower() or \
    #             search_string.lower() in str(student.get("gender", "")).lower() or \
    #             search_string.lower() in str(student.get("contact_number", "")).lower() or \
    #             search_string.lower() in str(student.get("email", "")).lower() or \
    #             search_string.lower() in str(student.get("address", "")).lower() or \
    #             search_string.lower() in str(student.get("program", "")).lower() or \
    #             search_string.lower() in str(student.get("gpa", "")).lower() or \
    #             search_string.lower() in str(student.get("accommodation", "")).lower():
                
    #             matching_students.append(student)
    #         break

    # return matching_students



quick_runtime = 0
merge_runtime = 0
def quick_runtimer(runtime):
    global quick_runtime
    quick_runtime = runtime
    return quick_runtime

def merge_runtimer(runtime):
    global merge_runtime
    merge_runtime = runtime
    return merge_runtime





'''

**Linear Search:**
1. Create an empty list called "matching_students" to store the matching students.
2. If the search string is empty, return the entire list of students.
3. If the search string is "student", return the entire list of students.
4. Iterate through each student in the list of students.
5. Check if the search string is present in any of the student's attributes (such as firstname, lastname, date_of_birth, etc.).
6. If the search string is found in any attribute, append the student to the "matching_students" list.
7. After iterating through all students, return the "matching_students" list.

**Binary Search:**
1. Create an empty list called "matching_students" to store the matching students.
2. If the search string is empty, return the entire list of students.
3. If the search string is "student", return the entire list of students.
4. Sort the list of students based on the firstname attribute.
5. Set the left pointer to 0 and the right pointer to the index of the last student in the list.
6. Repeat the following steps until the left pointer is less than or equal to the right pointer:
   - Calculate the middle index as the average of the left and right pointers.
   - Get the student at the middle index.
   - Check if the search string is present in any of the student's attributes.
   - If the search string is found in any attribute, append the student to the "matching_students" list.
   - If the search string is less than the student's firstname, update the right pointer to be the middle index minus 1.
   - Otherwise, update the left pointer to be the middle index plus 1.
7. After the loop, return the "matching_students" list.

**Hash Table Search:**
1. Create an empty list called "matching_students" to store the matching students.
2. If the search string is empty, return the entire list of students.
3. If the search string is "student", return the entire list of students.
4. Create an empty hash table to store the students based on their firstname.
5. Iterate through each student in the list of students.
6. Hash the student's firstname to obtain a key.
7. If the key is not present in the hash table, add an empty list as the value for that key.
8. Append the student to the list associated with the key in the hash table.
9. Hash the search string to obtain a search key.
10. If the search key is present in the hash table:
   - Iterate through each student in the list associated with the search key.
   - Check if the search string is present in any of the student's attributes.
   - If the search string is found in any attribute, append the student to the "matching_students" list.
11. After iterating through all the relevant students, return the "matching_students" list.

**Interpolation Search:**
1. Create an empty list called "matching_students" to store the matching students.
2. If the search string is empty, return the entire list of students.
3. If the search string is "student", return the entire list of students.
4. Set the low pointer to 0 and the high pointer to the index of the last student in the list.
5. Repeat the following steps while the low pointer is less than or equal to the high pointer and the search string is not empty:
   - Calculate the position as the low pointer plus the range between the low and high pointers scaled by the position of the first character of the search string relative to 'a' and 'z'.
   - If the calculated position is out of range, exit the loop.
   - Get the student at the calculated position.
   - Check if the search string is present in any of the student's attributes.
   - If the search string is found in any attribute, append the student to the "matching_students" list and exit the loop.
   - If the search string is less than the student's firstname, update the high pointer to be the position minus 1.
   - Otherwise, update the low pointer to be the position plus 1.
6. After the loop, return the "matching_students" list.

**Ternary Search:**
1. Create an empty list called "matching_students" to store the matching students.
2. If the search string is empty, return the entire list of students.
3. If the search string is "student", return the entire list of students.
4. Sort the list of students based on the firstname attribute.
5. Set the left pointer to 0 and the right pointer to the index of the last student in the list.
6. Repeat the following steps while the left pointer is less than or equal to the right pointer:
   - Calculate the left third as the left pointer plus one-third of the range between theI apologize for the incomplete response. Let me continue from where we left off:

**Ternary Search (continued):**
6. Repeat the following steps while the left pointer is less than or equal to the right pointer:
   - Calculate the left third as the left pointer plus one-third of the range between the left and right pointers.
   - Calculate the right third as the left pointer plus two-thirds of the range between the left and right pointers.
   - Get the students at the left third and right third positions.
   - Check if the search string is present in any of the students' attributes.
   - If the search string is found in any attribute, append the students to the "matching_students" list.
   - If the search string is less than the students' firstname, update the right pointer to be the left third minus 1.
   - If the search string is greater than the students' firstname, update the left pointer to be the right third plus 1.
   - Otherwise, update the left pointer to be the left third plus 1 and the right pointer to be the right third minus 1.
7. After the loop, return the "matching_students" list.

'''