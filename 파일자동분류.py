import os
import shutil

def organize_files(download_path):
    # 폴더 생성
    folders = ['images', 'PDFs', 'datasets']
    for folder in folders:
        folder_path = os.path.join(download_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # 파일 분류
    for filename in os.listdir(download_path):
        file_path = os.path.join(download_path, filename)

        # 이미지 파일 분류
        if filename.lower().endswith(('.jpg', '.jpeg')):
            shutil.move(file_path, os.path.join(download_path, 'images', filename))

        # PDF 파일 분류
        elif filename.lower().endswith('.pdf'):
            shutil.move(file_path, os.path.join(download_path, 'PDFs', filename))

        # 엑셀, CSV, 텍스트 파일 분류
        elif filename.lower().endswith(('.xlsx', '.csv', '.txt')):
            shutil.move(file_path, os.path.join(download_path, 'datasets', filename))

if __name__ == "__main__":
    download_path = r'C:\Users\sangm\Downloads'
    organize_files(download_path)
