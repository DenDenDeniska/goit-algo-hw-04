import pathlib

def get_cats_info(path):
    
    path = pathlib.Path(path)
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file.readlines():
                cat = line.strip().split(",")
                cats.append({"id": cat[0], "name": cat[1], "age": cat[2]})
    except FileNotFoundError as err:
        print(f"Файл не найден так как: {err}")
    except Exception as err:
        print(f"Произошла ошибка: {err}")
    return cats

def main():
    cats_info = get_cats_info("./cats_file.txt")
    print(cats_info)

if __name__ == "__main__":
    main()