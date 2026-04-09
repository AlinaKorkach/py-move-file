import os


def move_file(command: str) -> None:
    user_command, file_name, path = command.split()
    if user_command == "mv":
        with open(file_name, "r") as content:
            file_content = content.read()

        if path.endswith("/"):
            final_path = os.path.join(path, file_name)
        else:
            final_path = path

        folder_structure = os.path.dirname(final_path)

        if folder_structure:
            os.makedirs(folder_structure, exist_ok=True)

        with open(final_path, "w") as created_file:
            created_file.write(file_content)

        os.remove(file_name)
