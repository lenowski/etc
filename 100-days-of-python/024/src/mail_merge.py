"""
Generates personalized invitations based on a template and a list of names
"""

import os

PLACEHOLDER = "[name]"


def main():
    current_directory = os.getcwd()
    invited_names_path = os.path.join(
        current_directory, "input", "names", "invited_names.txt"
    )
    template_path = os.path.join(
        current_directory, "input", "templates", "template.txt"
    )
    output_path = os.path.join(current_directory, "output")

    try:
        with open(invited_names_path) as invited_names:
            names = [name.strip() for name in invited_names]
    except FileNotFoundError:
        print(f"Error: {invited_names_path} not found.")
        return

    try:
        with open(template_path) as template:
            content = template.read()

        os.makedirs(output_path, exist_ok=True)
        for name in names:
            with open(
                f"{output_path}/{name.lower().replace(' ', '_')}.txt", "w"
            ) as finished_letter:
                content = content.replace(PLACEHOLDER, name)
                finished_letter.write(content)
    except FileNotFoundError:
        print(f"Error: {template_path} not found.")
        return


if __name__ == "__main__":
    main()
