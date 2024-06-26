from dbs import postgres
import os
import shutil
import csv



def move_file(file_path, destination_folder):
    shutil.move(file_path, destination_folder)

def convert_csv_to_object(file_path):
    items = []
    with open(file_path, "r") as file:
      reader = csv.DictReader(file)
      for row in reader:
          items.append(row)
    # filter out empty rows
    items = [item for item in items if item]
    return items
    
def read_base_folder(base_folder, used_base_folder):
    # Get all files in base folder
    files = os.listdir(base_folder)
    # Get all csv files
    csv_files = [f for f in files if f.endswith('.csv')]
    return csv_files



def main():
    script_folder = os.path.dirname(__file__)
    base_folder = os.path.join(script_folder, 'bases')
    used_base_folder = os.path.join(script_folder, 'used_bases')
    if not os.path.exists(used_base_folder):
        os.makedirs(used_base_folder)
    csv_files = read_base_folder(base_folder, used_base_folder)
    items = []
    if not csv_files:
        print("No files to process")
        return
    print(f"Found {len(csv_files)} files to process")
    for file in csv_files:
      file_path = os.path.join(base_folder, file)
      data = convert_csv_to_object(file_path)
      items.extend(data)
      print(f"Moving file: {file}")
      move_file(file_path, used_base_folder)
      
    print(f"Found {len(items)} items to insert")
    print("Inserting data into database")
    conn = postgres.get_connection('postgres', 'postgres', 'example', 'localhost', '5432')
    count = 0
    for item in items:
        postgres.insert_data(conn, 'fast_food_stores', item)
        count += 1
        if count % 2 == 0 or count == len(items):
            print(f"Inserted {count} items")


    
if __name__ == '__main__':
    main()