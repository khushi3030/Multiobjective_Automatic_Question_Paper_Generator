from flask import Flask, render_template, request, redirect, url_for, Response, send_file
from generatepdf import PDF
import zipfile
import os
import spyder_final2
import pandas as pd


def get_level(level:str)->str:
    if level=='easy':
        return 'Easy'
    elif level=='medium':
        return 'Medium'
    elif level=='hard':
        return 'Hard'
    else:
        return 'Easy'

app = Flask(__name__)
options = [
        "Abstractions",
        "String python"
    ]

@app.route('/')
def index():
    
    return render_template('index.html', options=options)

@app.route('/generate_pdf', methods=['GET', 'POST'])
def generate_pdf():
    if request.method == "POST":
        result = request.form
        #spyder_final2.call_func((result['level']))
        soln = spyder_final2.new_mcq_func((int)(result['number_of_question']), (int)(result['number_of_papers']))
        
        attachment_paths = []
        zip_file_path = 'papers.zip'

        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for i in range(0, (int)(result['number_of_papers'])):  
                pdf = PDF('P', 'mm', 'Letter')
                pdf.alias_nb_pages()
                pdf.set_auto_page_break(auto=True, margin=15)

                pdf.add_page()           
                for j in range(0, (int)(result['number_of_question'])):
                    mcq_key = f"mcq{j+1}"
                    ques_key = f"ques"
                    dist1_key = f"dist1"
                    dist2_key = f"dist2"
                    dist3_key = f"dist3"
                    dist4_key = f"dist4"

                    pdf.set_font('times', '', 12)

                    pdf.cell(0, 8, f'Question{j+1}.: {soln[mcq_key][ques_key][i]}', ln=1)
                    pdf.cell(0, 5, f'Option A. : {soln[mcq_key][dist1_key][i]}', ln=1)
                    pdf.cell(0, 5, f'Option B. : {soln[mcq_key][dist2_key][i]}', ln=1)
                    pdf.cell(0, 5, f'Option C. : {soln[mcq_key][dist3_key][i]}', ln=1)
                    pdf.cell(0, 5, f'Option D. : {soln[mcq_key][dist4_key][i]}', ln=1)
                    pdf.ln(10)

                pdf_file_path = f"{result['filename']}{i+1}.pdf"
                pdf.output(pdf_file_path)  # Save the PDF
                attachment_paths.append(pdf_file_path)
                zipf.write(pdf_file_path, os.path.basename(pdf_file_path))

    return send_file(zip_file_path, as_attachment=True)
'''def generate_pdf():
    if request.method == "POST":
        #result['number_of_question']=4
        #result['number_of_papers']=3
        result = request.form
        pdf=PDF('P','mm','Letter')
        pdf.alias_nb_pages()
        pdf.set_auto_page_break(auto=True,margin=15)
        attachment_paths=[]
        soln=[]
        #spyder_final2.call_func((int)(result['number_of_question']))
        #pdf_buffer = io.BytesIO()
        soln=spyder_final2.new_mcq_func((int)(result['number_of_question']),(int)(result['number_of_papers']))
        #print("ans ", soln)
        for i in range(0, (int)(result['number_of_papers'])):  
            pdf.add_page()           
            for j in range(0, (int)(result['number_of_question'])):
                mcq_key = f"mcq{j+1}"
                ques_key = "ques"
                dist1_key = "dist1"
                dist2_key = "dist2"
                dist3_key = "dist3"
                dist4_key = "dist4"

                
                pdf.set_font('times', '', 12)
                
                pdf.cell(0, 8, f'Question{j+1}.: {soln[mcq_key][ques_key][i]}', ln=1)
                pdf.cell(0, 5, f'Option A. : {soln[mcq_key][dist1_key][i]}', ln=1)
                pdf.cell(0, 5, f'Option B. : {soln[mcq_key][dist2_key][i]}', ln=1)
                pdf.cell(0, 5, f'Option C. : {soln[mcq_key][dist3_key][i]}', ln=1)
                pdf.cell(0, 5, f'Option D. : {soln[mcq_key][dist4_key][i]}', ln=1)
                pdf.ln(10)
                    
            pdf_file_path = rf"{result['filename']}{i+1}.pdf"
            pdf.output(pdf_file_path)  # Save the PDF
            attachment_paths.append(pdf_file_path)
        zip_file_path = 'papers.zip'
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for attachment_path in attachment_paths:
                zipf.write(attachment_path, os.path.basename(attachment_path))

    return send_file(zip_file_path, as_attachment=True)
    #return send_file(rf"{result['filename']}.pdf", as_attachment=True)'''

    
#generate_pdf()

def main():
    app.run(debug=True, port=8000)
    
