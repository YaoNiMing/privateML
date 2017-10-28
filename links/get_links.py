from __future__ import print_function

import sys, os
import requests
import subprocess
from pprint import pprint
import csv
import os

BASE_REPO_DIR = os.path.join(os.path.dirname(__file__), "..")
LECTURES_DIR = os.path.join(BASE_REPO_DIR, "class_lectures")
OUTPUT_FILE = os.path.join(BASE_REPO_DIR, "links", "all_links.md")

def extract_files(search, out_prefix):
    """
    Searches for files of type, and outputs list to a file
    """
    if not out_prefix:
        out_prefix = search
    outfile = "files_" + out_prefix + ".temp"

    # Find all files that match the pattern
    command = ("find {} | grep {} > {}").format(LECTURES_DIR, search, outfile)
    result = subprocess.check_output(command,shell=True)

    # Convert the temp file to md
    write_links(out_prefix)

    # Remove the Temp files
    command = ("rm " + outfile)
    result = subprocess.check_output(command,shell=True)


def write_links(filetype):

    with open("files_" + filetype + ".temp", "r") as filein,  \
            open(OUTPUT_FILE, "a") as fileout:

        fileout.write("\n\n## " + filetype + "\n\n")
        linect = -1
        for line in filein:
            linect += 1
            if linect == 0:
               table_row1 = "| Week | Day | File |"
               table_row2 = "|------|-----|------|"
               fileout.write(table_row1 + '\n')
               fileout.write(table_row2 + '\n')

            line = line.rstrip('\n')
            filelink=line
            items = line.split("/")
            if "copy" in items[-1].lower() or ".ipynb_checkpoints" in items:
                continue  # Exclude copy notebooks / markdowns
            info_week = items[-3]
            info_day = items[-2]
            link = "[" + items[-1] + "]" + "(" + filelink + ")"
            tableout = "| " + info_week + " | " + info_day + " | " + link + " | " + str(linect+1) + " |"

            fileout.write(tableout + '\n')

    print("Successfully generated: links for " + filetype)

if __name__ == "__main__":

    with open(OUTPUT_FILE, "w"):
        pass
    extract_files(".ipynb", "ipynb")
    extract_files(".pdf", "pdf")
    extract_files("pair-", "pair")
