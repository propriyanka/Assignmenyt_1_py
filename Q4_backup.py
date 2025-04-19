import os
import shutil
import time

def backup_files(source_path, destination_dir):
    """
    📂 Step 1: Validate source and destination directories
    """
    if not os.path.exists(source_path):
        print("📁 Source directory does not exist. Creating it now...")
        os.makedirs(source_path)
    
    if not os.path.exists(destination_dir):
        print("📁 Destination directory does not exist. Creating it now...")
        os.makedirs(destination_dir)
    
    # 🔄 Step 2: Iterate through files in the source directory and copy them
    if os.path.isdir(source_path):
        for file_name in os.listdir(source_path):
            source_file_path = os.path.join(source_path, file_name)
            destination_path = os.path.join(destination_dir, file_name)
            
            # 📄 Step 3: If a file with the same name exists, append a timestamp
            if os.path.exists(destination_path):
                timestamp = time.strftime("%Y%m%d%H%M%S")
                file_name_no_ext, file_ext = os.path.splitext(file_name)
                new_file_name = f"{file_name_no_ext}_{timestamp}{file_ext}"
                destination_path = os.path.join(destination_dir, new_file_name)
            
            # 📌 Step 4: Copy the file to the destination
            try:
                shutil.copy2(source_file_path, destination_path)
                print(f"✅ {file_name} backed up successfully to {destination_path}")
            except Exception as e:
                print(f"❌ Error copying {file_name}: {e}")
    else:
        print("❌ Error: Provided source path is not a directory!")

if __name__ == "__main__":
    """
    🚀 Step 5: Ask for user input for directories and execute backup
    """
    source_directory = input("📌 Enter the source directory: ") or "source_directory"
    destination_directory = input("📌 Enter the destination directory: ") or "backup_directory"
    
    backup_files(source_directory, destination_directory)
