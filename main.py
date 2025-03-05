import os
from merger import merge_pdfs

def welcome():
    print("\n📄 Welcome to Larona's PDF Merger CLI! 📄")
    print("This tool will help you merge multiple PDFs into a single file.")
    print("------------------------------------------------------\n")

def get_pdf_files():
    files = []
    print("👉 Enter the file names **in the order you want them merged**.")
    print("👉 Press Enter on a blank line when you are done.\n")

    while True:
        file_path = input("Add PDF file (or press Enter to finish): ").strip()
        if file_path == "":
            break

        if not file_path.lower().endswith(".pdf"):
            print(f"⚠️ Warning: '{file_path}' does not seem to be a PDF file.")
        
        if not os.path.exists(file_path):
            print(f"❌ Error: '{file_path}' does not exist. Try again.")
        else:
            files.append(file_path)

    if len(files) < 2:
        print("❗ You need at least **two files** to merge. Start again.")
        return get_pdf_files()  # Loop until valid input

    return files

def get_output_file():
    while True:
        output_file = input("\n📁 Enter name for the merged output file (e.g., merged.pdf): ").strip()
        if not output_file.lower().endswith(".pdf"):
            output_file += ".pdf"
        return output_file

def main():
    welcome()

    files = get_pdf_files()
    output_file = get_output_file()

    print("\n🚀 Merging files...")
    merge_pdfs(files, output_file)
    print(f"✅ Merge complete! Saved as '{output_file}'.")

if __name__ == "__main__":
    main()
