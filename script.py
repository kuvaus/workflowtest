
with open('CHANGELOG.md', 'r') as file:
    lines = file.readlines()
    print(lines)

filtered_lines = []
start_processing = False
for line in lines:
    if line.startswith("#### [v"):
        if start_processing:
            break
        else:
            start_processing = True
    if start_processing:
        filtered_lines.append(line)

with open('FILTERED_CHANGELOG.md', 'w') as file:
    file.writelines(filtered_lines)
