# import streamlit as st
# import os
# import textwrap
# from PIL import Image, ImageDraw, ImageFont
# from moviepy.editor import ImageClip
# from docx import Document
# import shutil  # for zipping
# import io

# # ================================
# # FUNCTIONS
# # ================================

# def create_banner(text, filename, color=(25, 90, 200), outdir="output"):
#     os.makedirs(outdir, exist_ok=True)
#     img = Image.new('RGB', (1200, 600), color=color)
#     draw = ImageDraw.Draw(img)
#     try:
#         font = ImageFont.truetype("arial.ttf", 50)
#     except:
#         font = ImageFont.load_default()

#     lines = textwrap.wrap(text, width=20)
#     y_text = 200
#     for line in lines:
#         bbox = draw.textbbox((0, 0), line, font=font)
#         w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
#         draw.text(((1200 - w) / 2, y_text), line, fill="white", font=font)
#         y_text += h + 10

#     img.save(os.path.join(outdir, filename + ".jpg"))
#     img.save(os.path.join(outdir, filename + ".png"))


# def create_text_files(topic, outdir):
#     tagline = f"Empower yourself with {topic} — from basics to mastery!"
#     description = (
#         f"The {topic} is designed to introduce learners to the core concepts of data science. "
#         f"From understanding data to building models, this program helps everyone get started "
#         f"with real-world insights. Learn, explore, and transform your future!"
#     )
#     keywords = "Data Science, Machine Learning, AI, Python, Training, Basics, Beginners, Career"

#     with open(os.path.join(outdir, "tagline.txt"), "w", encoding="utf-8") as f:
#         f.write(tagline)
#     with open(os.path.join(outdir, "description.txt"), "w", encoding="utf-8") as f:
#         f.write(description)
#     with open(os.path.join(outdir, "keywords.txt"), "w", encoding="utf-8") as f:
#         f.write(keywords)


# def create_video(topic, outdir):
#     os.makedirs(outdir, exist_ok=True)
#     img = Image.new('RGB', (1280, 720), color=(30, 30, 90))
#     draw = ImageDraw.Draw(img)
#     try:
#         font = ImageFont.truetype("arial.ttf", 60)
#     except:
#         font = ImageFont.load_default()

#     text = topic
#     bbox = draw.textbbox((0, 0), text, font=font)
#     w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
#     draw.text(((1280 - w) / 2, (720 - h) / 2), text, fill="white", font=font)

#     img_path = os.path.join(outdir, "video_slide.png")
#     img.save(img_path)

#     clip = ImageClip(img_path).set_duration(10)  # shorter duration for demo
#     clip.write_videofile(os.path.join(outdir, "short_video.mp4"), fps=24, verbose=False, logger=None)


# def create_blog(topic, outdir):
#     blog = Document()
#     blog.add_heading(f"{topic}", level=1)
#     blog.add_paragraph(
#         f"The {topic} introduces you to key data science concepts — "
#         "from data collection to visualization and machine learning. "
#         "A complete beginner-friendly roadmap to mastering data science."
#     )
#     blog.add_paragraph("\nKey Learning Points:")
#     blog.add_paragraph("• Introduction to Data Science Concepts")
#     blog.add_paragraph("• Data Cleaning and Exploration")
#     blog.add_paragraph("• Visualization Techniques")
#     blog.add_paragraph("• Simple Machine Learning Models")
#     blog.add_paragraph("\nEnroll today to start your Data Science journey!")
#     blog.save(os.path.join(outdir, "blog.docx"))


# def create_linkedin_post(topic, link, outdir):
#     post = f"""
# 🚀 Excited to share our latest launch — {topic}! 🎯

# 📊 Learn how to collect, clean, and analyze data.
# 💡 Build a strong foundation in data science and machine learning.
# 🎓 Perfect for beginners looking to start their data career.

# Register now 👉 {link}
# #DataScience #AI #Learning #Education #CareerGrowth
# """
#     with open(os.path.join(outdir, "linkedin_post.txt"), "w", encoding="utf-8") as f:
#         f.write(post)


# def create_offer_banners(topic, outdir):
#     offer_texts = [
#         "🎉 Flat 50% Off – Enroll Today!",
#         "🔥 Early Bird Offer – Limited Seats!",
#         "🚀 Learn Data Science Now – Pay Later!",
#         "💻 Master Data Science in 30 Days!"
#     ]
#     colors = [(200, 50, 50), (50, 150, 50), (50, 80, 200), (220, 140, 0)]
#     for i, (text, color) in enumerate(zip(offer_texts, colors)):
#         create_banner(f"{topic}\n{text}", f"offer_banner_{i+1}", color=color, outdir=outdir)


# def generate_all(topic, link):
#     outdir = "output"
#     os.makedirs(outdir, exist_ok=True)

#     create_banner(topic, "main_banner", color=(25, 90, 200), outdir=outdir)
#     create_text_files(topic, outdir)
#     create_video(topic, outdir)
#     create_blog(topic, outdir)
#     create_linkedin_post(topic, link, outdir)
#     create_offer_banners(topic, outdir)

#     # Create ZIP file in memory
#     zip_buffer = io.BytesIO()
#     shutil.make_archive("marketing_assets", 'zip', outdir)
#     with open("marketing_assets.zip", "rb") as f:
#         zip_buffer.write(f.read())

#     zip_buffer.seek(0)
#     return zip_buffer


# # ================================
# # STREAMLIT UI
# # ================================
# st.set_page_config(page_title="Digital Marketing Automation", page_icon="🎯", layout="centered")

# st.title("🎯 Digital Marketing Automation Tool")
# st.write("Automatically generate banners, videos, blogs, LinkedIn posts, and offer posters for your marketing campaign.")

# topic = st.text_input("Enter Topic:", "Data Science Basic Training Program for Everyone")
# link = st.text_input("Enter Link:", "https://example.com")

# if st.button("🚀 Generate & Download Files"):
#     with st.spinner("✨ Generating all marketing materials... please wait."):
#         zip_data = generate_all(topic, link)
#         st.success("✅ All files generated successfully!")

#         st.download_button(
#             label="⬇️ Download All Marketing Files (ZIP)",
#             data=zip_data,
#             file_name="marketing_assets.zip",
#             mime="application/zip"
#         )

# st.markdown("---")
# st.caption("All generated files are packaged as a downloadable ZIP.")

import os
import textwrap
import io
import shutil
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, concatenate_videoclips
from matplotlib import font_manager
import streamlit as st

# ----------------------------- FONT SETUP -----------------------------
def load_font(size):
    """Load a scalable cross-platform font."""
    try:
        return ImageFont.truetype("arial.ttf", size)
    except:
        font_path = font_manager.findfont("DejaVuSans-Bold")
        return ImageFont.truetype(font_path, size)


# ----------------------------- OUTLINED TEXT -----------------------------
def draw_outlined_text(draw, position, text, font, fill="white", outline="black", outline_width=4):
    x, y = position
    for ox in range(-outline_width, outline_width + 1):
        for oy in range(-outline_width, outline_width + 1):
            draw.text((x + ox, y + oy), text, font=font, fill=outline)
    draw.text((x, y), text, font=font, fill=fill)


# ----------------------------- POSTER CREATION -----------------------------
def create_banner(text, filename, color=(25, 90, 200), outdir="output"):
    os.makedirs(outdir, exist_ok=True)
    img = Image.new('RGB', (1280, 720), color=color)
    draw = ImageDraw.Draw(img)
    font = load_font(90)

    lines = textwrap.wrap(text, width=12)
    total_h = sum([draw.textbbox((0, 0), l, font=font)[3] for l in lines]) + len(lines) * 25
    y_text = (720 - total_h) // 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        x = (1280 - w) / 2
        draw_outlined_text(draw, (x, y_text), line, font, fill="white", outline="black", outline_width=4)
        y_text += bbox[3] + 25

    img.save(os.path.join(outdir, f"{filename}.jpg"))
    img.save(os.path.join(outdir, f"{filename}.png"))
    return os.path.join(outdir, f"{filename}.jpg")


# ----------------------------- VIDEO CREATION -----------------------------
def create_video(topic, outdir):
    os.makedirs(outdir, exist_ok=True)
    slides = [
        f"🚀 Welcome to {topic}",
        "📊 Learn Data Science Step-by-Step",
        "💡 Build Real Projects & Master ML",
        "✨ Start Your Data Journey Today!"
    ]

    clips = []
    for i, text in enumerate(slides):
        img = Image.new("RGB", (1280, 720))
        draw = ImageDraw.Draw(img)

        # Gradient background
        for y in range(720):
            color = (int(30 + y/4), int(90 + y/8), int(180 + y/6))
            draw.line([(0, y), (1280, y)], fill=color)

        font = load_font(70)
        lines = textwrap.wrap(text, width=14)
        total_h = sum([draw.textbbox((0, 0), l, font=font)[3] for l in lines]) + len(lines) * 25
        y_text = (720 - total_h) // 2

        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=font)
            w = bbox[2] - bbox[0]
            x = (1280 - w) / 2
            draw_outlined_text(draw, (x, y_text), line, font, fill="white", outline="black", outline_width=4)
            y_text += bbox[3] + 25

        img_path = os.path.join(outdir, f"slide_{i+1}.png")
        img.save(img_path)
        clip = ImageClip(img_path).set_duration(5)  # short slide (5s per slide)
        clips.append(clip)

    final = concatenate_videoclips(clips, method="compose")
    video_path = os.path.join(outdir, "promo_video.mp4")
    final.write_videofile(video_path, fps=24, verbose=False, logger=None)
    return video_path


# ----------------------------- CONTENT GENERATION -----------------------------
def generate_text_files(topic, outdir):
    tagline = f"Empowering your future with {topic}!"
    desc = f"The {topic} is a beginner-friendly program designed to help you learn data analysis, visualization, and machine learning — step by step with real-world insights."
    keywords = "Data Science, AI, Machine Learning, Analytics, Python, Online Learning, Upskill"

    with open(os.path.join(outdir, "tagline.txt"), "w", encoding="utf-8") as f:
        f.write(tagline)
    with open(os.path.join(outdir, "description.txt"), "w", encoding="utf-8") as f:
        f.write(desc)
    with open(os.path.join(outdir, "keywords.txt"), "w", encoding="utf-8") as f:
        f.write(keywords)


# ----------------------------- BLOG + LINKEDIN POST -----------------------------
def generate_blog_and_post(topic, outdir):
    blog = f"""# {topic}: Start Your Data Journey

The {topic} is designed to introduce you to core data concepts, hands-on tools, and real-world insights.

### What You’ll Learn:
- Data analysis with Python
- Visualization with Power BI & Matplotlib
- Basic Machine Learning models
- Real-world project experience

Learn, apply, and grow — your data career starts here!
"""
    linkedin_post = f"""🚀 Launching: **{topic}!**

Master the essentials of Data Science — from data collection to machine learning.  
Perfect for beginners looking to upskill and boost their career!  

#DataScience #AI #Learning #CareerGrowth
"""
    with open(os.path.join(outdir, "blog.txt"), "w", encoding="utf-8") as f:
        f.write(blog)
    with open(os.path.join(outdir, "linkedin_post.txt"), "w", encoding="utf-8") as f:
        f.write(linkedin_post)


# ----------------------------- OFFER POSTERS -----------------------------
def create_offer_posters(topic, outdir):
    offers = [
        "🔥 50% OFF - Limited Time!",
        "🎯 Enroll Now & Get Free Certification!",
        "🚀 Start Learning Today!",
        "🎓 Special Offer for Students!"
    ]
    colors = [(255, 87, 51), (60, 179, 113), (65, 105, 225), (218, 112, 214)]
    for i, offer in enumerate(offers):
        create_banner(f"{topic}\n{offer}", f"offer_banner_{i+1}", colors[i], outdir)


# ----------------------------- MAIN GENERATION -----------------------------
def generate_all(topic):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = os.path.join("output", f"{topic.replace(' ', '_')}_{timestamp}")
    os.makedirs(outdir, exist_ok=True)

    create_banner(topic, "main_banner", (30, 90, 160), outdir)
    generate_text_files(topic, outdir)
    create_video(topic, outdir)
    generate_blog_and_post(topic, outdir)
    create_offer_posters(topic, outdir)

    # Create ZIP for download
    zip_path = f"{outdir}.zip"
    shutil.make_archive(outdir, "zip", outdir)
    return zip_path


# ----------------------------- STREAMLIT UI -----------------------------
st.set_page_config(page_title="Digital Marketing Automation", layout="centered")
st.title("🎯 Digital Marketing Automation App")
st.write("Generate professional marketing assets in one click — banners, offers, video, blog & more!")

topic = st.text_input("Enter your campaign topic:", "Data Science Basic Training Program for Everyone")

if st.button("🚀 Generate & Download"):
    with st.spinner("✨ Generating all marketing materials... please wait."):
        zip_path = generate_all(topic)
    with open(zip_path, "rb") as f:
        st.download_button(
            label="⬇️ Download All Files (ZIP)",
            data=f,
            file_name=os.path.basename(zip_path),
            mime="application/zip"
        )
    st.success("✅ All files generated successfully!")
