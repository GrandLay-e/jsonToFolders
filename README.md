# jsonToFolders

A Python utility to convert JSON structures into folder hierarchies.

## Description

This tool reads a JSON file and creates a corresponding folder structure on your filesystem based on the JSON's hierarchical organization.

## Installation

```bash
git clone https://github.com/GrandLay-e/jsonToFolders.git
cd jsonToFolders
```

## Usage

```bash
python3 jsonToFolders.py exemple.json
```

It will create folder structures in the current working directory.

## JSON Format
The expected JSON format should represent a hierarchical structure where keys become folder names.
For example:

```json
{
    "Type": "Folder",
    "Name": "Documents",
    "content": [
        {
            "Type": "Folder",
            "Name": "Work",
            "content": [
                {
                    "Type": "File",
                    "Name": "Report.txt"
                },
                {
                    "Type": "File",
                    "Name": "Presentation.py"
                }
            ]
        },
        {
            "Type": "Folder",
            "Name": "Personal",
            "content": [
                {
                    "Type": "File",
                    "Name": "Diary.docx"
                }
            ]
        }
    ]
}

```

### It will create the following folder structure:

```
Documents/
├── Work/
│   ├── Report.txt
│   └── Presentation.py
└── Personal/
    └── Diary.docx
```
With "Documents" as the root folder.

## Requirements
You need to have the following installed:
- `docx` library for Word documents,
- `openpyxl` library for Excel files,
- `pptx` library for PowerPoint files.
You can install the required libraries using pip:

```bash
pip install python-docx openpyxl python-pptx
```

## License
MIT License