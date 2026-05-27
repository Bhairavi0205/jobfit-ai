from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
import PyPDF2
from groq import Groq
from dotenv import load_dotenv
import os
import io
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.units import inch

load_dotenv()
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_text(file):
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        return f"Error: {str(e)}"

def ask_groq(prompt, max_tokens=4000):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=0.3
    )
    return response.choices[0].message.content

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@app.post("/analyze")
async def analyze(resume: UploadFile = File(...), jd: str = Form(...)):
    content = await resume.read()
    resume_text = extract_text(io.BytesIO(content))
    prompt = f"""You are a senior technical recruiter with 15 years experience. Analyze this resume against the job description.

RESUME:
{resume_text[:3000]}

JOB DESCRIPTION:
{jd[:2000]}

Respond in EXACTLY this format:

ATS_SCORE: [number]/100

SCORE_BREAKDOWN:
Skills: [number]/100
Experience: [number]/100
Keywords: [number]/100
Education: [number]/100

MISSING_KEYWORDS:
- [keyword 1]
- [keyword 2]
- [keyword 3]
- [keyword 4]
- [keyword 5]
- [keyword 6]

REJECTION_REASONS:
- [specific reason 1]
- [specific reason 2]
- [specific reason 3]
- [specific reason 4]

RESUME_REWRITER:
- Original: [exact line from resume] | Rewritten: [stronger version]
- Original: [exact line from resume] | Rewritten: [stronger version]
- Original: [exact line from resume] | Rewritten: [stronger version]

INTERVIEW_QUESTIONS:
TECHNICAL:
- [question 1]
- [question 2]
- [question 3]
- [question 4]
- [question 5]
- [question 6]
- [question 7]
- [question 8]

PROJECT_BASED:
- [question about specific project from resume]
- [question about specific project from resume]
- [question about specific project from resume]
- [question about specific project from resume]
- [question about specific project from resume]

BEHAVIORAL:
- [behavioral question 1]
- [behavioral question 2]
- [behavioral question 3]
- [behavioral question 4]
- [behavioral question 5]

HR:
- [HR question 1]
- [HR question 2]
- [HR question 3]
- [HR question 4]
- [HR question 5]

COMPANY_RESEARCH:
Company Name: [extract from JD or Unknown]
Industry: [identify from JD]
Role Type: [identify from JD]
Key Focus Areas: [3 things this company cares about based on JD]
Talking Points: [2-3 things candidate should mention in interview]

COLD_EMAIL:
Subject: [specific subject]

Dear Hiring Manager,

I am [candidate full name from resume], writing to express strong interest in the [job title from JD] position. [2 sentences about matching achievements]. I would love to discuss how I can contribute.

Best regards,
[candidate name]
[candidate email]
[candidate phone]"""

    result = ask_groq(prompt)
    return {"result": result}

@app.post("/chat")
async def chat(message: str = Form(...), context: str = Form(...)):
    prompt = f"""You are an expert interview coach. 
Candidate context: {context}
Question: {message}
Give specific, actionable advice. If asked for sample answer, give complete STAR format answer."""
    result = ask_groq(prompt, max_tokens=800)
    return {"response": result}

@app.post("/compare")
async def compare(resume: UploadFile = File(...), jds: str = Form(...)):
    content = await resume.read()
    resume_text = extract_text(io.BytesIO(content))
    prompt = f"""Compare this resume against multiple job descriptions and rank them.

RESUME:
{resume_text[:2000]}

JOB DESCRIPTIONS (separated by ---):
{jds[:3000]}

Respond in this EXACT format:

JD_RANK_1:
Company/Role: [name]
Match Score: [number]/100
Why Best Fit: [2 specific sentences]
Key Matching Skills: [3-4 skills]
Gap: [main gap]
Apply First: YES

JD_RANK_2:
Company/Role: [name]
Match Score: [number]/100
Why Best Fit: [2 specific sentences]
Key Matching Skills: [3-4 skills]
Gap: [main gap]
Apply First: NO

JD_RANK_3:
Company/Role: [name]
Match Score: [number]/100
Why Best Fit: [2 specific sentences]
Key Matching Skills: [3-4 skills]
Gap: [main gap]
Apply First: NO"""

    result = ask_groq(prompt)
    return {"result": result}

@app.post("/download-pdf")
async def download_pdf(content: str = Form(...), name: str = Form(default="Candidate")):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=0.75*inch, bottomMargin=0.75*inch)
    styles = getSampleStyleSheet()
    purple = HexColor('#6d28d9')
    dark = HexColor('#1e1b2e')
    gray = HexColor('#6b7280')
    title_style = ParagraphStyle('title', fontSize=20, textColor=purple, fontName='Helvetica-Bold', spaceAfter=4)
    sub_style = ParagraphStyle('sub', fontSize=10, textColor=gray, fontName='Helvetica', spaceAfter=16)
    heading_style = ParagraphStyle('heading', fontSize=11, textColor=purple, fontName='Helvetica-Bold', spaceAfter=8, spaceBefore=14)
    body_style = ParagraphStyle('body', fontSize=9, textColor=dark, fontName='Helvetica', spaceAfter=5, leading=14)
    story = []
    story.append(Paragraph("JobFit AI — Analysis Report", title_style))
    story.append(Paragraph(f"Candidate: {name}", sub_style))
    story.append(HRFlowable(width="100%", thickness=1, color=purple))
    story.append(Spacer(1, 12))
    for line in content.split('\n'):
        if line.strip():
            if line.isupper() or line.endswith(':'):
                story.append(Paragraph(line.strip(), heading_style))
            else:
                story.append(Paragraph(line.strip(), body_style))
    doc.build(story)
    buffer.seek(0)
    return StreamingResponse(buffer, media_type="application/pdf",
        headers={"Content-Disposition": "attachment; filename=JobFitAI_Report.pdf"})

@app.post("/company-info")
async def company_info(company: str = Form(...)):
    prompt = f"""Research the company "{company}" and provide detailed information for a job interview.

Provide information in EXACTLY this format:

COMPANY_NAME: [official name]
FOUNDED: [year]
HEADQUARTERS: [location]
INDUSTRY: [industry type]
EMPLOYEES: [approximate number]
CEO: [current CEO name]
REVENUE: [approximate annual revenue]

ABOUT:
[3-4 sentences about what the company does]

PRODUCTS_SERVICES:
- [main product/service 1]
- [main product/service 2]
- [main product/service 3]
- [main product/service 4]

CULTURE_VALUES:
- [core value 1]
- [core value 2]
- [core value 3]

INTERVIEW_TIPS:
- [specific tip for interviewing at this company]
- [specific tip for interviewing at this company]
- [specific tip for interviewing at this company]
- [specific tip for interviewing at this company]

RECENT_NEWS:
- [recent development about this company]
- [recent development about this company]
- [recent development about this company]

WHY_JOIN:
[2-3 sentences about why this is a good company to work for]

WATCH_OUT:
[1-2 sentences about challenges or things to be aware of]"""

    result = ask_groq(prompt, max_tokens=1500)
    print("RESULT:", result[:500])
    return {"result": result}