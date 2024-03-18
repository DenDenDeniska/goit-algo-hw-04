import pathlib

def total_salary(path):
    path = pathlib.Path(path)

    total, average, count = 0, 0, 0
    with open(path, "r", encoding="utf-8") as file:
        for line in file.readlines():
            line = line.strip().split(",")
            total += int(line[1])
            count += 1
    average = total / count
    return total, average

def main():
    total, average = total_salary("./salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()