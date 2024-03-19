import pathlib

def total_salary(path):
    path = pathlib.Path(path)

    total, average, count = 0, 0, 0

    try:
        file_open = open(path, "r", encoding="utf-8")
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    except Exception as err:
        print(err)
        return 0, 0

    with file_open as file:
        for line in file.readlines():
            line = line.strip().split(",")
            total += int(line[1])
            count += 1
    average = total / count
    return total, average

def main():
    total, average = total_salary("./salary.txt")
    if total and average:
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()