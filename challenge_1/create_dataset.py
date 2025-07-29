import pandas as pd
import random

categories = ["Data Science", "Web Development", "Marketing", "Finance", "Engineering"]
skills_dict = {
    "Data Science": ["Python", "Machine Learning", "SQL", "Statistics", "Pandas", "NumPy", "Scikit-learn", "TensorFlow"],
    "Web Development": ["JavaScript", "HTML", "CSS", "React", "Node.js", "Python", "Django", "Flask"],
    "Marketing": ["Digital Marketing", "SEO", "Social Media", "Content Creation", "Analytics", "Campaign Management"],
    "Finance": ["Financial Analysis", "Excel", "Accounting", "Risk Management", "Investment", "Bloomberg"],
    "Engineering": ["CAD", "Project Management", "Problem Solving", "MATLAB", "AutoCAD", "Design"]
}

resumes = []
for i in range(100):
    category = random.choice(categories)
    skills = random.sample(skills_dict[category], k=random.randint(3, 6))
    experience = random.randint(0, 10)
    education = random.choice(["Bachelor", "Master", "PhD", "High School"])
    
    resume_text = f"Experienced professional in {category.lower()} with {experience} years of experience. "
    resume_text += f"Education: {education} degree. Skills: {', '.join(skills)}. "
    resume_text += f"Looking for opportunities in {category.lower()} field."
    
    resumes.append({
        "Category": category,
        "Resume": resume_text,
        "Experience_Years": experience,
        "Education": education
    })

df = pd.DataFrame(resumes)
df.to_csv("data/resume_dataset.csv", index=False)
print("Sample resume dataset created successfully!")
print(f"Dataset shape: {df.shape}")
print(df.head())


