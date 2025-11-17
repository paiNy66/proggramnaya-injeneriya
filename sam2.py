def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            if not content.strip():
                raise Exception("файл пустой")
            print(content)
    except Exception as e:
        print(e)

read_file("empty.txt")
read_file("with_content.txt")