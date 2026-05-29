courses = {
    "Python Basics": {
        "duration": "4 weeks",
        "level": "Beginner",
        "topics": ["Variables", "Data Types", "Control Flow", "Functions"]
    },
    "Data Science": {
        "duration": "8 weeks",
        "level": "Intermediate",
        "topics": ["Pandas", "NumPy", "Matplotlib", "Scikit-learn"]
    },
    "Web Development": {
        "duration": "6 weeks",
        "level": "Beginner",
        "topics": ["HTML", "CSS", "JavaScript", "Django"]
    }
}
# Get the keys of the dictionary
course_names = courses.keys()
print("Course names:", course_names)
print("Type of course_names:", type(course_names))
# Get the values of the dictionary
course_details = courses.values()
print("Course details:", course_details)
print("Type of course_details:", type(course_details))  
# Get the items of the dictionary
course_items = courses.items()
print("Course items:", course_items)
print("Type of course_items:", type(course_items))
print("Iterating through course items:")
for course_name, details in course_items:
    print(f"Course: {course_name}")
    print(f"Details: {details}")
    print()

print("Converting course names to a list:")
course_names_list = list(course_names)
print("Course names as a list:", course_names_list)
print("Converting course details to a list:")
course_details_list = list(course_details)
print("Course details as a list:", course_details_list)

print("Getting the duration of each course:")
for course_name, details in course_items:
    duration = details.get("duration")
    print(f"{course_name} duration: {duration}")    

    