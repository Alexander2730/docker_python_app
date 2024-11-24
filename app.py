import os
import sys
import datetime

def count_files(path):
    return len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))])

def top_files(path):
    files = [(f, os.path.getsize(os.path.join(path, f))) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files.sort(key=lambda x: x[1], reverse=True)
    return files[:10]

if __name__ == "__main__":
    path = "/"
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "World"
    
    print(f"Привет, {name}! Текущее время: {datetime.datetime.now()}")
    print(f"Количество файлов в '{path}': {count_files(path)}")
    print("Топ-10 файлов по размеру (Кб):")
    for file, size in top_files(path):
        print(f"{file}: {size / 1024:.2f} Кб")
