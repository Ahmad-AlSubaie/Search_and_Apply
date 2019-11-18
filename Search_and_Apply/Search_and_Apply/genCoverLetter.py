# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 14:43:16 2019
@author: kerma
"""

from sys import argv
from fpdf import FPDF
import json
import csv

def write_cover_letter():

    # open csv file and read input
    with open("info.csv") as info_csv:

        reader = csv.reader(info_csv)

        for row in reader:

            pdf = FPDF('P', 'mm', 'A4')  # portrait mode, mm , A4 size paper
            pdf.add_page()  # new blank page
            pdf.set_font('Arial', '', 12)  # font, Style (B,U,I) , fontsize in pt.

            temp_cover_letter = open('cover_letter.txt', 'r')

            lines = temp_cover_letter.readlines()
            
            for line in lines:
                
                line = line.replace("#position", row[0])
                line = line.replace("#company", row[1])
               
                #print(line1)
                pdf.write(6, line)

           
            pdf.output('cover_letter.pdf', 'F')
            pdf.close()
            temp_cover_letter.close()
            

if __name__ == "__main__":
  
    write_cover_letter()
