import os

def write_directory_structure(root_path, output_file):
    for root, dirs, files in os.walk(root_path):
        level = root.replace(root_path, "").count(os.sep)
        indent = "│   " * level
        output_file.write(f"{indent}📁 {os.path.basename(root) or root}\n")

        subindent = "│   " * (level + 1)
        for file in files:
            output_file.write(f"{subindent}📄 {file}\n")


def write_file_contents(root_path, output_file):
    for root, _, files in os.walk(root_path):
        for file in files:
            if file.endswith((".py", ".txt", ".html", ".js", ".css", ".cpp", ".java")):
                file_path = os.path.join(root, file)

                output_file.write("\n" + "=" * 80 + "\n")
                output_file.write(f"FILE PATH: {file_path}\n")
                output_file.write("=" * 80 + "\n")

                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        output_file.write(f.read())
                except Exception as e:
                    output_file.write(f"\n[ERROR READING FILE: {e}]\n")


def export_folder_to_text(folder_path, output_txt="output.txt"):
    with open(output_txt, "w", encoding="utf-8") as out:
        out.write("DIRECTORY STRUCTURE\n")
        out.write("=" * 80 + "\n")
        write_directory_structure(folder_path, out)

        out.write("\n\nFILE CONTENTS\n")
        out.write("=" * 80 + "\n")
        write_file_contents(folder_path, out)

    print(f"Done ✅ Output saved to: {output_txt}")


if __name__ == "__main__":
    folder = input("Enter folder path: ").strip()
    export_folder_to_text(folder)
