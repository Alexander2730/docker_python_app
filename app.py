import os
import sys
import datetime

def count_files(path):
    count = 0
    files = []
    for root, dirs, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(root, filename)
            try:
                file_size = os.path.getsize(file_path)
                files.append((file_path, file_size))
                count += 1
            except:
                pass
    return count, files

def top_files(files):
    # Сортируем файлы по размеру и берем топ-10
    files.sort(key=lambda x: x[1], reverse=True)
    return files[:10]

def main():
    path = '/'
    # Получаем имя для приветствия
    name = sys.argv[1] if len(sys.argv) > 1 else "User"
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"Привет, {name}! Текущее время: {current_time}")

    count, files = count_files(path)
    print(f"Количество файлов в '{path}': {count}")

    top_ten = top_files(files)
    print("Топ-10 файлов по размеру (в Кб):")
    for file, size in top_ten:
        print(f"{file}: {size / 1024:.2f} Кб")

if __name__ == "__main__":
    main()
