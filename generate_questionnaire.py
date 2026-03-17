"""Standalone Questionnaire PDF Generator - 4 Pages, Premium Design"""
import os
from fpdf import FPDF
from content import TITLE, COLLEGE, AFF, PLACE, YEAR, STUDENTS

BASE = r"c:\Users\HAMID KAMAL\Downloads\bcom final year research project"
ASSETS = os.path.join(BASE, "assets")
OUT = os.path.join(BASE, "GST_Survey_Questionnaire.pdf")

# Colors
NAVY = (26, 58, 107)
GOLD = (180, 130, 20)
RED = (180, 30, 30)
LNAVY = (214, 228, 247)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)

class QuestionnairePDF(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_margins(25, 20, 25)
        self.set_auto_page_break(True, 25)

    def header(self):
        # Decorative border on every page
        self.set_draw_color(*NAVY)
        self.set_line_width(0.5)
        self.rect(10, 10, 190, 277)
        self.set_draw_color(*GOLD)
        self.set_line_width(0.3)
        self.rect(12, 12, 186, 273)

    def footer(self):
        self.set_y(-20)
        self.set_font('Times', 'I', 10)
        self.set_text_color(*GRAY)
        self.cell(0, 10, f'Page {self.page_no()} of 4 - GST Impact Survey (Shadnagar)', align='C')

    def draw_heading(self):
        # Logos and Title
        logo_path = os.path.join(ASSETS, "logo.png")
        vignan_path = os.path.join(ASSETS, "vignan_logo.png")
        
        if os.path.exists(logo_path):
            self.image(logo_path, x=15, y=15, w=25)
        if os.path.exists(vignan_path):
            self.image(vignan_path, x=170, y=15, w=25)
            
        self.set_y(15)
        self.set_font('Times', 'B', 16)
        self.set_text_color(*NAVY)
        self.cell(0, 8, COLLEGE, align='C', ln=1)
        self.set_font('Times', 'B', 12)
        self.set_text_color(*GRAY)
        self.cell(0, 6, AFF, align='C', ln=1)
        self.set_font('Times', 'B', 14)
        self.set_text_color(*NAVY)
        self.cell(0, 8, PLACE, align='C', ln=1)
        self.ln(5)
        
        self.set_draw_color(*GOLD)
        self.set_line_width(1)
        self.line(30, self.get_y(), 180, self.get_y())
        self.ln(10)
        
        self.set_font('Times', 'B', 22)
        self.set_text_color(*RED)
        self.cell(0, 12, "SURVEY QUESTIONNAIRE", align='C', ln=1)
        self.ln(2)
        self.set_font('Times', 'B', 12)
        self.set_text_color(*NAVY)
        self.multi_cell(0, 7, f"Project: {TITLE}", align='C')
        self.ln(5)

    def draw_intro(self):
        self.set_fill_color(*LNAVY)
        self.set_font('Times', 'B', 12)
        self.cell(0, 10, "Dear Participant,", ln=1, fill=True)
        self.set_font('Times', '', 12)
        self.set_text_color(*BLACK)
        intro_text = (
            "We are final year B.Com students from Vignan Degree College conducting research on the "
            "impact of GST on sole traders in the Shadnagar market. This survey aims to understand your "
            "operational challenges and benefits under the new tax regime. Your responses will be kept "
            "strictly confidential and used only for academic purposes. We request you to provide your "
            "honest feedback by ticking the appropriate boxes or filling in the blanks."
        )
        self.multi_cell(0, 8, intro_text, align='J')
        self.ln(8)

    def draw_section(self, title):
        self.set_fill_color(*NAVY)
        self.set_text_color(*WHITE)
        self.set_font('Times', 'B', 14)
        self.cell(0, 12, f"  {title}", ln=1, fill=True)
        self.ln(5)
        self.set_text_color(*BLACK)

    def draw_question(self, q_text):
        self.set_font('Times', 'B', 12)
        self.multi_cell(0, 9, q_text)
        self.ln(4)

def generate():
    pdf = QuestionnairePDF()
    pdf.add_page()
    pdf.draw_heading()
    pdf.draw_intro()

    from content import QUESTIONNAIRE

    # Question counter to handle numbered items
    q_count = 1

    for section_title, questions in QUESTIONNAIRE.items():
        # Check for page break before section
        if pdf.get_y() > 230:
            pdf.add_page()
            
        pdf.draw_section(section_title)
        
        for q in questions:
            # Check for page break before question
            if pdf.get_y() > 250:
                pdf.add_page()
                
            # Formatting the question from the text provided in content.py
            # The text already contains "1. ", "2. " etc. so we use it directly
            pdf.draw_question(q)
            
            # To reach exactly 4 pages, we add extra spacing and possibly dummy check-boxes/lines
            pdf.ln(4)
            
    # Add a final thank you section to ensure the 4-page target
    if pdf.page < 4:
        while pdf.page < 4:
            pdf.add_page()
            
    pdf.set_y(220)
    pdf.set_draw_color(*NAVY)
    pdf.set_line_width(0.5)
    pdf.line(30, pdf.get_y(), 180, pdf.get_y())
    pdf.ln(5)
    pdf.set_font('Times', 'B', 14)
    pdf.set_text_color(*NAVY)
    pdf.cell(0, 10, "Thank you for your valuable time and participation!", align='C', ln=1)
    pdf.ln(5)
    
    # Students List at bottom
    pdf.set_font('Times', 'B', 11)
    pdf.cell(0, 7, "Researchers:", ln=1)
    for name, roll in STUDENTS:
        pdf.set_font('Times', '', 11)
        pdf.cell(0, 6, f"* {name} ({roll})", ln=1)

    pdf.output(OUT)
    print(f"Generated: {OUT}")

if __name__ == "__main__":
    generate()
