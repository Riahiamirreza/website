import os
import re
import datetime


def print_help():
    print(
        """Usage: python3 export_to_pdf.py source_dir [output_file]
        """
    )

def listfiles(path):
    return [os.path.join(path, f) for f in os.listdir(path)]
    

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print_help()
        raise SystemExit
    
    sourcedir = sys.argv[1]
    outputfile = sys.argv[2] if len(sys.argv) > 2 else "export.txt"
    files = listfiles(sourcedir)


    files_with_date = [
        (
            datetime.datetime.strptime(
                re.search(
                    "([0-9]{4}-[0-9]{2}-[0-9]{2})", 
                    file
                ).group(0),
                '%Y-%m-%d'
            ),
            file
        ) for file in files
    ]

    files = sorted(files_with_date)
    with open(outputfile, 'w') as export_file:
        for _, file in files:
            with open(file) as f:
                export_file.write(f.read())
