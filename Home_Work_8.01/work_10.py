"""
home_work_10
"""
import os
import shutil
def move_contents(source_folder, destination_folder):
    try:
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        for item in os.listdir(source_folder):
            source_path = os.path.join(source_folder, item)
            destination_path = os.path.join(destination_folder, item)
            shutil.move(source_path, destination_path)
        print(f"Содержимое {source_folder} успешно перемещено в {destination_folder}.")
    except Exception as e:
        print(f"Произошла ошибка при перемещении: {e}")
def task1():
    source_video_folder = 'video'
    source_sub_folder = 'sub'
    destination_folder = 'watch_me'
    move_contents(source_video_folder, destination_folder)
    move_contents(source_sub_folder, destination_folder)
def rename_files():
    try:
        for filename in os.listdir('.'):
            if filename.endswith('.jpg'):
                parts = filename.split('_')
                if len(parts) == 2:
                    new_filename = f"{parts[1]}_{parts[0]}.jpg"
                    os.rename(filename, new_filename)
                    print(f"{filename} успешно переименован в {new_filename}.")
    except Exception as e:
        print(f"Произошла ошибка при переименовании: {e}")
def create_folder_and_move_files():
    try:
        with open('list.tsv', 'r') as file:
            content = file.read().splitlines()
            if not os.path.exists('list'):
                os.makedirs('list')
            for filename in content:
                shutil.move(filename, os.path.join('list', os.path.basename(filename)))
        print("Файлы успешно перемещены в папку list.")
    except Exception as e:
        print(f"Произошла ошибка при создании папки и перемещении файлов: {e}")
def remove_last_line(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            lines = file.readlines()
        with open(output_file, 'w') as file:
            file.writelines(lines[:-1])
        print(f"Последняя строка файла {input_file} успешно удалена. Результат записан в {output_file}.")
    except Exception as e:
        print(f"Произошла ошибка при удалении строки: {e}")
if __name__ == "__main__":
    task1()
    rename_files()
    create_folder_and_move_files()
    remove_last_line('input.txt', 'output.txt')