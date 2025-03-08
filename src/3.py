def school_project(students):
    projects = []
    for student in students:
        if student["Grade"] == "12":
            project = {
                "Name": student["Name"],
                "Project": "School Project",
                "Grade": student["Grade"],
                "Class": student["Class"],
            }
            projects.append(project)
    return projects
