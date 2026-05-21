from PIL import Image, ImageDraw, ImageFont
import os

# Create og-images directory if it doesn't exist
os.makedirs('og-images', exist_ok=True)

def create_course_image(filename, course_code, course_title, subtitle, stats, accent_color, text_color_light):
    """Generate a 1200x1200 course preview image"""
    
    # Create image with dark background
    img = Image.new('RGB', (1200, 1200), color='#0f172a')
    draw = ImageDraw.Draw(img)
    
    # Try to use default fonts, fall back to basic if unavailable
    try:
        title_font = ImageFont.truetype("arial.ttf", 140)
        subtitle_font = ImageFont.truetype("arial.ttf", 80)
        label_font = ImageFont.truetype("arial.ttf", 28)
        stat_font = ImageFont.truetype("arial.ttf", 60)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        stat_font = ImageFont.load_default()
    
    # Draw semi-transparent accent circles
    draw.ellipse([800, 0, 1400, 600], fill=tuple(int(accent_color.lstrip('#')[i:i+2], 16) + 80 for i in (0, 2, 4)))
    
    # Draw department label
    draw.text((80, 60), f"CAPITAL UNIVERSITY", fill=accent_color, font=label_font)
    
    # Draw course code
    draw.text((80, 200), course_code, fill='white', font=title_font)
    
    # Draw course title
    draw.text((80, 380), course_title, fill=text_color_light, font=subtitle_font)
    
    # Draw subtitle
    draw.text((80, 520), subtitle, fill='rgba(255,255,255,0.7)', font=label_font)
    
    # Draw stats
    y_stat = 700
    stat_labels = ['QUESTIONS', 'CHAPTERS', 'FORMAT']
    
    for i, (stat_value, stat_label) in enumerate(zip(stats['values'], stat_labels)):
        x_pos = 80 + (i * 350)
        
        # Draw stat value
        draw.text((x_pos, y_stat), str(stat_value), fill='white', font=stat_font)
        
        # Draw stat label
        draw.text((x_pos, y_stat + 90), stat_label, fill='rgba(255,255,255,0.5)', font=label_font)
    
    # Draw footer text if available
    if 'footer' in stats:
        draw.text((80, 1050), stats['footer'], fill='rgba(255,255,255,0.7)', font=label_font)
    
    img.save(f'og-images/{filename}')
    print(f'Created {filename}')

# IT 223 - Internet Technology
create_course_image(
    'it.png',
    'IT 223',
    'Internet Technology',
    'Chapters 1–6 · 203 Questions',
    {
        'values': [203, 6, 'MCQ'],
        'footer': 'Protocols · Networks · Addressing · Wireless'
    },
    '#60a5fa',
    '#ffffff'
)

# CS 241 - Operating Systems
create_course_image(
    'os.png',
    'CS 241',
    'Operating Systems',
    'Lectures 0–8 · 117 Questions',
    {
        'values': [117, 9, 'MC/TF'],
        'footer': 'Dr. Ahmed Hisham Mostafa'
    },
    '#60a5fa',
    '#93c5fd'
)

# HU 323 - Accounting
create_course_image(
    'accounting.png',
    'HU 323',
    'Fundamentals of Accounting',
    'Chapters 1–2 · 47 Questions',
    {
        'values': [47, 2, 'MCQ'],
        'footer': 'Dr. Hamdy Habl'
    },
    '#60a5fa',
    '#fef3c7'
)

# IT 222 - Computer Networks
create_course_image(
    'networks.png',
    'IT 222',
    'Computer Networks 1',
    '90 Questions · Subnetting',
    {
        'values': [90, 'MC/TF', ''],
        'footer': 'Dr. Islam Zakaria'
    },
    '#60a5fa',
    '#ffe4e6'
)

# Quiz Hub main
img = Image.new('RGB', (1200, 1200), color='#0f172a')
draw = ImageDraw.Draw(img)

try:
    title_font = ImageFont.truetype("arial.ttf", 140)
    subtitle_font = ImageFont.truetype("arial.ttf", 80)
    label_font = ImageFont.truetype("arial.ttf", 36)
except:
    title_font = ImageFont.load_default()
    subtitle_font = ImageFont.load_default()
    label_font = ImageFont.load_default()

draw.ellipse([800, 0, 1400, 600], fill=(0, 176, 110, 80))

draw.text((80, 150), "CAPITAL UNIVERSITY", fill='#60a5fa', font=label_font)
draw.text((80, 350), "Course", fill='white', font=title_font)
draw.text((80, 550), "Quiz Hub", fill='#99f6e4', font=subtitle_font)
draw.text((80, 850), "Practice quizzes for your courses", fill='rgba(255,255,255,0.7)', font=label_font)

img.save('og-images/quiz-hub.png')
print('Created quiz-hub.png')

print('All PNG images generated successfully!')
