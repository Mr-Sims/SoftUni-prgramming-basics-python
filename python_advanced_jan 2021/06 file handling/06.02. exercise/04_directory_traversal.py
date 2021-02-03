import os


def extract_files(content):
    return [el for el in dir_content if os.path.isfile(el)]


def get_report_for_files_extensions(files):
    report = {}
    for file in files:
        file_name, extension = os.path.splitext(file)
        if extension not in report:
            report[extension] = []
        report[extension].append(file_name)
    return report


dir_content = (os.listdir())
files = extract_files(dir_content)
report_info = get_report_for_files_extensions(files)
result = ""
for extension, file_name in sorted(report_info.items(), key=lambda x: x[0]):
    result += f"{extension}\n"
    for name in file_name:
        result += f"- - - {name}{extension}\n"

user = input() # Enter username please!(only win users. Other OS... eh!)

with open(f"C:\\Users\\{user}\\Desktop\\report.txt", "w") as file:
    file.write(result)

