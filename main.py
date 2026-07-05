from planner import create_project_plan


def main():
    print("=== Project Planning Agent ===")
    

    project_description = input("Project description: ")

    result = create_project_plan(project_description)

    print("\n" + result)


if __name__ == "__main__":
    main()