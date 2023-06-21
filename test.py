text_file_path = "text.txt"
new_text_content = ""
with open(text_file_path, "r") as f:
    body = f.read()
body = body.replace("java", "python")

with open(text_file_path, "w") as f:
    f.write(body)
