import os

def create_project_structure():
    project_name = "Project"

    # Create the Project Folder 
    if not os.path.exists(project_name):
        os.makedirs(project_name)

    # Development
    development_path = os.path.join(project_name, "Development")
    os.makedirs(development_path)
    create_subfolders(development_path, ["Hardware", "Software"])

    # Documentation
    documentation_path = os.path.join(project_name, "Documentation")
    os.makedirs(documentation_path)
    create_subfolders(documentation_path, ["Requirements", "Instruction"])

    # Demonstration
    demonstration_path = os.path.join(project_name, "Demonstration")
    os.makedirs(demonstration_path)
    create_subfolders(demonstration_path, ["raw", "Edition"])

    # PUBLISH
    publish_path = os.path.join(project_name, "PUBLISH")
    os.makedirs(publish_path)
    create_subfolders(publish_path, ["backup_V1", "Current Version"])

def create_subfolders(parent_path, folders):
    for folder in folders:
        folder_path = os.path.join(parent_path, folder)
        os.makedirs(folder_path)

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully.")

