# Batch Document Generator 📄⚙️

A scalable automation system designed to take raw form data and instantly generate print-ready documents, certificates, and official letterheads in bulk. 

## 🚨 The Problem
Many administrative offices collect data via online forms (like Google Forms), but rely on manual copy-pasting to transfer that data into official Word documents or PDFs (e.g., scholarship certificates, bonafide letters, event participation certificates). 

**This manual data entry results in:**
* High error rates (incorrect IDs, previous names left on new documents).
* Severe administrative bottlenecks and long waiting lines.
* Wasted administrative hours on repetitive tasks.

## 💡 The Solutions
This repository provides a generalized system to completely automate the pipeline from "Data Collection" to "Print-Ready Document." It includes two approaches based on the user's technical environment.

---

### Solution 1: The "No-Code" Cloud Workflow (Google Workspace)
For organizations that rely entirely on Google Forms and don't want to run local scripts, this system utilizes Google Workspace automation.

**Step-by-Step Workflow:**
1. **The Data Source:** Create a Google Form to collect student/user data. All responses automatically route to a linked Google Sheet.
2. **The Template:** Create a master document in Google Docs. Wherever you need dynamic data (like a name or amount), type placeholders wrapped in double arrows (e.g., `<<Name>>`, `<<Enrollment_Number>>`).
3. **The Engine:** Open the Google Sheet with the responses. Go to `Extensions > Add-ons > Get add-ons` and install **Autocrat** (a free document merge tool).
4. **The Mapping:** Launch Autocrat. It will ask you to select your Google Doc template, and then it will automatically ask you to match the columns in your Sheet to the `<<Tags>>` in your Doc.
5. **The Trigger:** Set Autocrat to run "On form submit." 
6. **The Result:** Every time a new form is submitted, the system automatically generates an individualized, print-ready PDF, saves it to a designated Drive folder, and can even email it directly to the submitter.

---

### Solution 2: The Python Engine (Local Batch Processing)
For generating hundreds of documents locally from a `.csv` database, this Python script acts as a lightweight, offline document engine. 

#### 🚀 Features
* **Data Agnostic:** Automatically maps any `.csv` column headers to your template. No need to rewrite the code for different forms!
* **Template-Based Generation:** Uses standard Microsoft Word (`.docx`) files as templates.
* **Bulk Processing:** Generates and names hundreds of individual files dynamically in seconds for immediate batch printing.

#### 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/Batch-Document-Generator.git](https://github.com/yourusername/Batch-Document-Generator.git)
   cd Batch-Document-Generator

```markdown
## 🛠️ Installation & Setup Guide

Follow these simple steps to run the Python document generator on your local machine:

### 1. Install Dependencies
By default, Python cannot edit Microsoft Word documents. We need to install `docxtpl`, a lightweight library that gives Python the ability to read and write `.docx` files. Open your terminal or command prompt and run:
```bash
pip install docxtpl

```

### 2. Prepare Your Files (The Inputs)

You need to provide two files in the same folder as your Python script:

* **The Template (`template.docx`):** Create your official letterhead or certificate in Word. Wherever you want dynamic data to appear, use Jinja2 tags (double curly brackets). For example, type `{{ Name }}` or `{{ Enrollment }}` right into the Word document.
* **The Data (`data.csv`):** Download your form responses as a CSV file. **Crucial:** The column headers in your CSV must exactly match the words inside your curly brackets!

### 3. Run the Generator

Once your template and data are ready, open your terminal, navigate to the project folder, and start the script by running:

```bash
python main.py

```

### 4. Retrieve Your Output

The script is designed to keep your workspace organized. It will automatically create a new folder named `Generated_Documents` and place all your newly generated, print-ready `.docx` files neatly inside.

```

This format looks incredibly professional. It tells recruiters not only *what* commands to run, but proves that you understand *why* they need to be run! 

<FollowUp label="Want help creating the dummy files?" query="How do I create the dummy template.docx and data.csv files to test this out before I upload everything?"/>

```