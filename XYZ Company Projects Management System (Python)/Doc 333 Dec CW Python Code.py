from datetime import datetime

#List
projects = []
workers = []

#Add total workers
print("                   XYZ Company")
print("\n")
nums_of_workers = int(input("Number of Team Members you need to add: "))
for _ in range(nums_of_workers):
    workers.append({'worker_id': len(workers) + 1})

save_workers = input("           Do you want to add workers? (Y/N) ")
if save_workers.upper() == "Y":
    print("{} Added successfully.".format(nums_of_workers))

else:
    print("          Team Members not added.")

while True:  #Main menu
    print("""                          XYZ Company
                           Main menu
                                                        
          \n1. Add a new project to existing projects
          \n2. Remove a completed project from existing projects
          \n3. Add new workers to available workers group
          \n4. Update details on ongoing projects
          \n5. Project Statistics
          \n6. Exit
    """)

    choice = input("       Select Your Option: ")

 
    if choice == '1':          # Add new project
        add_the_project = True
        while add_the_project:
            print("""                           XYZ Company
                        Add a new project        """)
            project_code_no = int(input("Project Code (Enter '0' to exit): "))  #Back to the main menu

            if project_code_no == 0 or not str(project_code_no).strip():
                add_the_project = False
                break

            num_workers_to_add_for_list = int(input("Enter the number of Team Members to add: "))
            if len(workers) < num_workers_to_add_for_list:
                print("               Not enough Team Members available.")
                continue

            clients_name = str(input("Client's Name: "))
            start_date_str = input("Start Date (YYYY-MM-DD): ")
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date_str = input("Expected End Date (YYYY-MM-DD): ")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            current_position = input("Project Status (ongoing/on hold/completed): ")

            if current_position.lower() == 'completed':
                actual_end_date_str = input("Actual End Date (YYYY-MM-DD): ")
                actual_end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            else:
                actual_end_date = None

            for _ in range(num_workers_to_add_for_list):
                workers.pop()

            save_project = input("Do you want to save the above project? (Y/N) ")
            if save_project.upper() == "Y":
                print("      Project added successfully.")
                projects.append({
                    'project_code': project_code_no,
                    'client_name': clients_name,
                    'start_date': start_date,
                    'end_date': end_date,
                    'num_workers': num_workers_to_add_for_list,
                    'status': current_position,
                    'actual_end_date': actual_end_date})
            else:
                print("          Not saved")

            add_the_project = False
            break

    elif choice == '2':
        print("""                 XYZ Company
            Remove a Completed Project""")  #Remove a completed project
        project_code_no = input("Project Code: ")

        project_code_no = int(project_code_no)

        project_index_to_remove = next(
            (index for index, project in enumerate(projects) if project['project_code'] == project_code_no), None)

        if project_index_to_remove is not None:

            if projects[project_index_to_remove]['status'].lower() == 'completed':

                remove_project = projects.pop(project_index_to_remove)
                for _ in range(remove_project['num_workers']):
                    workers.append({'worker': len(workers) + 1})  #Add workers back to available workers

                save_project = input("Do you want to remove the project? (Y/N) ")

                if save_project.upper() == 'Y':
                    print("Project removed successfully")

                    print("Project Code: " + str(remove_project['project_code']))
                    print("Client's Name: " + str(remove_project['client_name']))
                    print("Start date: " + str(remove_project['start_date']))
                    print("Expected end date: " + str(remove_project['end_date']))
                    print("Number of workers: " + str(remove_project['num_workers']))
                    print("Project Status: " + str(remove_project['status']))

                else:
                    print("Project not removed.")
            else:
                print("Cannot remove. Project is not completed.")
        else:
            print("Project not found")

    elif choice == '3':
        print("""                   XYZ Company
            Add new workers""")

        nums_of_workers = int(input("Number of Team Members to add: "))
        for _ in range(nums_of_workers):
            workers.append({'worker': len(workers) + 1})

        save_workers = input("           Do you want to add workers? (Y/N) ")
        if save_workers.upper() == "Y":
            print(str(nums_of_workers) + " workers added successfully.")

        else:
            print("          Team Members not added.")

    elif choice == '4':
        update_the_project = True
        while update_the_project:
            print("""                 XYZ Company                                        
            Update an existing project""")  #Update an existing project 
            project_code_no = int(input("Project Code to update (Enter '0' to exit): ")) #Back to the main menu
            if project_code_no == 0:
                update_the_project = False
                break

            num_workers_to_add_for_list = int(input("Enter the number of Team Members to add: "))
            if len(workers) < num_workers_to_add_for_list:
                print("              Error: Not enough Team Members available. Please add more Team Members first.")
                continue

            for project in projects:
                if project['project_code'] == project_code_no:
                    project['client_name'] = str(input("Client's Name ({}) - ".format(project['client_name'])))
                    project['start_date'] = input("Start date ({}) - ".format(project['start_date']))
                    start_date = datetime.strptime(project['start_date'], "%Y-%m-%d")
                    project['end_date'] = input("Expected end date ({}) - ".format(project['end_date']))

                    end_date = datetime.strptime(
                        project['end_date'], "%Y-%m-%d")
                    project['status'] = input("Project Status (ongoing/on hold/completed): ")

                    if project['status'].lower() == 'completed':
                        project['actual_end_date'] = input(
                            "Actual End Date (YYYY-MM-DD): ")
                        actual_end_date = datetime.strptime(
                            project['actual_end_date'], "%Y-%m-%d")
                    else:
                        project['actual_end_date'] = None

                    project['num_workers'] += num_workers_to_add_for_list

            for _ in range(num_workers_to_add_for_list):
                workers.pop()

            save_project = input(
                "             Do you want to save the updated project? (Y/N) ")
            if save_project.upper() == "Y":
                print("             Project details updated successfully.")
            else:
                print("             Project details not updated")

            update_the_project = False
            break

    elif choice == '5':
        print("""XYZ Company
    Project Statistics""") #Project Statistics

        ongoing_projects = 0

        completed_projects = 0
        on_hold_projects = 0

        for project in projects:
            if project['status'] == 'ongoing':
                ongoing_projects += 1
            elif project['status'] == 'completed':
                completed_projects += 1
            elif project['status'] == 'on hold':
                on_hold_projects += 1

            available_workers = len(workers)

            print("Number of ongoing projects: {}".format(ongoing_projects))
            print("Number of completed projects: {}".format(completed_projects))
            print("Number of on-hold projects: {}".format(on_hold_projects))
            print("Number of available Team Members: {}".format(available_workers))

        while True:
            view_details = input(
                "Do you want to see full details of a project? (Y/N) ")
            if view_details.upper() == "Y":
                print("Saved Project Codes:")
                for project in projects:
                   print("Project Code: {}".format(project['project_code']))
                project_code_view = input("Enter the project code: ")
                for project in projects:
                    if project['project_code'] == int(project_code_view):
                        print("Project Details:")
                        for key, value in project.items():
                            print("   {}: {}".format(key, value))
                        break
                else:
                    print("Project with code " + str(project_code_view) + " not found.")

            else:
                break

        save_project = input("Do you want to add the project? (Y/N) ")
        if save_project.upper() == "Y":
            print("Project added successfully")
        else:
            print("""               Exiting the program.
                     Thank You Visiting!""")
            break

#Exit
    elif choice == '6':
        print("""               Exiting the program.
                     Thank You Visiting!""")
        break

    else:
        print("                 Invalid choice.")
