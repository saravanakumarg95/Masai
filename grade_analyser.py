def process_scores(students):
    return {name: round(sum(scores) / len(scores), 2) for name, scores in students.items()}


def classify_grades(averages):
    grade_a_threshold = 90
    grade_b_threshold = 75
    grade_c_threshold = 60
    
    result ={}
    for name, average in averages.items():
        if average >= grade_a_threshold:
            grade ='A'
        elif average >= grade_b_threshold:
            grade = 'B'
        elif average >= grade_c_threshold:
            grade = 'C'
        else:
            grade = 'F'
        
        result[name]= (average, grade)
    
    return result


def generate_report(classified, passing_avg=70):
    print("===== Student Grade Report =====")
    
    passed_count = 0
    failed_count = 0
    
    for name, (average, grade) in classified.items():
        status ="PASS" if average >= passing_avg else "FAIL"
        if average >= passing_avg:
            passed_count +=1
        else:
            failed_count +=1
        
        print(f"{name:<10}| Avg: {average:<6} | Grade: {grade} | Status: {status}")
    
    print("================================")
    total_students = passed_count + failed_count
    print(f"Total Students : {total_students}")
    print(f"Passed         : {passed_count}")
    print(f"Failed         : {failed_count}")
    
    return passed_count


if __name__ == "__main__":
    students = {
        "Alice": [85, 90, 78, 92],
        "Bob": [88, 76, 85, 79],
        "Charlie": [92, 95, 89, 91]
    }
    

    averages = process_scores(students)
    
    classified = classify_grades(averages)
 
    passed = generate_report(classified)
   