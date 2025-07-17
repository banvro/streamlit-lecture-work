import streamlit as st
from fpdf import FPDF

# PDF class
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Resume', ln=True, align='C')
        self.ln(10)

# Streamlit UI
st.title("📄 Resume Builder")

with st.form("resume_form"):
    st.subheader("Personal Information")
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    linkedin = st.text_input("LinkedIn URL")
    github = st.text_input("GitHub URL")

    st.subheader("Education")
    education = st.text_area("Education Details")

    st.subheader("Work Experience")
    experience = st.text_area("Work Experience")

    st.subheader("Skills")
    skills = st.text_area("Skills (comma-separated)")

    st.subheader("Projects")
    projects = st.text_area("Projects")

    st.subheader("Certifications")
    certifications = st.text_area("Certifications")

    st.subheader("Hobbies/Interests")
    hobbies = st.text_area("Hobbies/Interests")

    submit = st.form_submit_button("Generate Resume")

if submit:
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)

    pdf.cell(0, 10, f'Name: {name}', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Email: {email} | Phone: {phone}', ln=True)
    pdf.cell(0, 10, f'LinkedIn: {linkedin}', ln=True)
    pdf.cell(0, 10, f'GitHub: {github}', ln=True)
    pdf.ln(5)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Education:', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, education)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Experience:', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, experience)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Skills:', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, skills)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Projects:', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, projects)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Certifications:', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, certifications)

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Hobbies/Interests:', ln=True)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, hobbies)

    # Generate PDF in memory
    pdf_output = pdf.output(dest='S').encode('latin-1')

    st.success("✅ Resume generated!")
    st.download_button(
        label="📥 Download Resume PDF",
        data=pdf_output,
        file_name=f"{name.replace(' ', '_')}_Resume.pdf",
        mime='application/pdf'
    )
