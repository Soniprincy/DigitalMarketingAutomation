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

# app.py
import os
import io
import zipfile
import textwrap
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from moviepy.editor import ImageClip, concatenate_videoclips
import streamlit as st

# ---------------------------
# Configuration / Theme
# ---------------------------
THEME = {
    "name": "Modern Blue Gradient",
    "colors": [(25, 118, 210), (3, 169, 244)],  # top -> bottom
    "image_size": (1280, 720),
    "banner_size": (1200, 600)
}

# ---------------------------
# Robust font loader (works on Streamlit Cloud)
# ---------------------------
def load_font(size: int):
    """Try Arial, then DejaVu, then fall back to PIL default."""
    try:
        return ImageFont.truetype("arial.ttf", size)
    except Exception:
        try:
            return ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size)
        except Exception:
            try:
                return ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", size)
            except Exception:
                return ImageFont.load_default()

# ---------------------------
# Utilities: gradient & contrast
# ---------------------------
def vertical_gradient(size, top_color, bottom_color):
    """Return an Image with vertical gradient from top_color to bottom_color."""
    w, h = size
    base = Image.new('RGB', size, top_color)
    top = Image.new('RGB', size, bottom_color)
    mask = Image.new('L', (1, h))
    for y in range(h):
        mask.putpixel((0, y), int(255 * (y / (h - 1))))
    mask = mask.resize(size)
    return Image.composite(top, base, mask)

def relative_luminance(rgb):
    """Calculate relative luminance (0..1)."""
    r, g, b = [v / 255.0 for v in rgb]
    def lin(c):
        return c / 12.92 if c <= 0.03928 else ((c + 0.055)/1.055) ** 2.4
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)

def pick_text_colors(bg_top, bg_bottom):
    """Return (fill_color, outline_color) chosen for contrast against gradient midpoint."""
    mid = tuple(int((a + b) / 2) for a, b in zip(bg_top, bg_bottom))
    lum = relative_luminance(mid)
    # If background is dark (lum < 0.5) use white fill with dark outline; otherwise dark fill with light outline
    if lum < 0.5:
        return ("white", "black")
    else:
        return ("black", "white")

# ---------------------------
# Text drawing helpers
# ---------------------------
def draw_text_with_outline(draw, position, text, font, fill, outline, outline_width=3):
    x, y = position
    # draw outline
    for ox in range(-outline_width, outline_width + 1):
        for oy in range(-outline_width, outline_width + 1):
            if ox == 0 and oy == 0:
                continue
            draw.text((x + ox, y + oy), text, font=font, fill=outline)
    # main text
    draw.text((x, y), text, font=font, fill=fill)

def fit_font_for_multiline(draw, text_lines, font_name_loader, max_width, max_font_size, min_font_size=20, line_spacing=8):
    """
    Find largest font size such that all lines fit within max_width.
    font_name_loader: function(size)->ImageFont
    """
    size = max_font_size
    while size >= min_font_size:
        font = font_name_loader(size)
        too_big = False
        for line in text_lines:
            bbox = draw.textbbox((0,0), line, font=font)
            if bbox[2] - bbox[0] > max_width:
                too_big = True
                break
        if not too_big:
            return font
        size -= 2
    return font_name_loader(min_font_size)

def wrap_to_lines(text, max_chars=24):
    return textwrap.wrap(text, width=max_chars)

# ---------------------------
# Banner / Poster generation
# ---------------------------
def create_poster(text, filename, outdir, size=None, top_color=None, bottom_color=None):
    os.makedirs(outdir, exist_ok=True)
    if size is None:
        size = THEME["image_size"]
    if top_color is None or bottom_color is None:
        top_color, bottom_color = THEME["colors"]

    bg = vertical_gradient(size, top_color, bottom_color)
    draw = ImageDraw.Draw(bg)

    # pick colors for text/outline
    fill_color, outline_color = pick_text_colors(top_color, bottom_color)

    # prepare lines
    lines = wrap_to_lines(text, max_chars=20)
    # fit font
    max_width = int(size[0]*0.85)
    # start with a large font and shrink to fit
    font = fit_font_for_multiline(draw, lines, load_font, max_width, max_font_size=int(size[1]*0.14))

    # compute total height
    heights = [draw.textbbox((0,0), line, font=font)[3] - draw.textbbox((0,0), line, font=font)[1] for line in lines]
    total_h = sum(heights) + (len(lines)-1) * 12

    y = (size[1] - total_h) // 2
    for line in lines:
        bbox = draw.textbbox((0,0), line, font=font)
        text_w = bbox[2] - bbox[0]
        x = (size[0] - text_w) // 2
        draw_text_with_outline(draw, (x, y), line, font, fill_color, outline_color, outline_width=max(2, int(font.size * 0.04)))
        y += (bbox[3] - bbox[1]) + 12

    # save jpg + png
    jpg_path = os.path.join(outdir, f"{filename}.jpg")
    png_path = os.path.join(outdir, f"{filename}.png")
    bg.save(jpg_path, quality=90)
    bg.save(png_path)
    return jpg_path, png_path

# ---------------------------
# Create multiple outputs
# ---------------------------
def create_text_files(topic, outdir):
    os.makedirs(outdir, exist_ok=True)
    tagline = f"Empower yourself with {topic} — from basics to mastery!"
    description = (
        f"The {topic} program introduces learners to fundamentals of data science: "
        "data collection, exploration, visualization, and simple ML. Hands-on projects included."
    )
    keywords = "Data Science, Machine Learning, AI, Python, Training, Beginners, Career"

    with open(os.path.join(outdir, "tagline.txt"), "w", encoding="utf-8") as f:
        f.write(tagline)
    with open(os.path.join(outdir, "description.txt"), "w", encoding="utf-8") as f:
        f.write(description)
    with open(os.path.join(outdir, "keywords.txt"), "w", encoding="utf-8") as f:
        f.write(keywords)

def create_blog(topic, outdir):
    os.makedirs(outdir, exist_ok=True)
    blog_text = f"""# {topic}

The {topic} is a beginner-friendly program that introduces you to practical data skills...
(Use this as a starter — edit as needed.)
"""
    with open(os.path.join(outdir, "blog.txt"), "w", encoding="utf-8") as f:
        f.write(blog_text)

def create_linkedin_post(topic, link, outdir):
    os.makedirs(outdir, exist_ok=True)
    post = f"""🚀 Launching: {topic}!

Learn Data Science step-by-step with hands-on projects.
Register: {link}

#DataScience #AI #Learning
"""
    with open(os.path.join(outdir, "linkedin_post.txt"), "w", encoding="utf-8") as f:
        f.write(post)

# ---------------------------
# Video generation (short promo ≈ 8s)
# ---------------------------
def create_short_video(topic, outdir):
    os.makedirs(outdir, exist_ok=True)
    size = THEME["image_size"]
    top_color, bottom_color = THEME["colors"]
    fill_color, outline_color = pick_text_colors(top_color, bottom_color)

    slides_text = [
        f"🚀 {topic}",
        "📊 Learn Data Science Step-by-Step",
        "💡 Build Real Projects & Master ML",
        "✨ Start Your Data Journey Today!"
    ]

    clips = []
    # create images for slides
    for idx, text in enumerate(slides_text, start=1):
        bg = vertical_gradient(size, top_color, bottom_color)
        draw = ImageDraw.Draw(bg)
        # use slightly smaller font for video
        lines = wrap_to_lines(text, max_chars=24)
        font = fit_font_for_multiline(draw, lines, load_font, int(size[0]*0.9), max_font_size=int(size[1]*0.12))
        # center vertically
        heights = [draw.textbbox((0,0), line, font=font)[3] - draw.textbbox((0,0), line, font=font)[1] for line in lines]
        total_h = sum(heights) + (len(lines)-1)*10
        y = (size[1] - total_h)//2
        for line in lines:
            bbox = draw.textbbox((0,0), line, font=font)
            text_w = bbox[2] - bbox[0]
            x = (size[0] - text_w)//2
            draw_text_with_outline(draw, (x, y), line, font, fill_color, outline_color, outline_width=max(2, int(font.size * 0.04)))
            y += (bbox[3] - bbox[1]) + 10

        img_path = os.path.join(outdir, f"video_slide_{idx}.png")
        bg.save(img_path)
        clip = ImageClip(img_path).set_duration(2)  # 2s per slide
        clips.append(clip)

    final = concatenate_videoclips(clips, method="compose")
    video_path = os.path.join(outdir, "short_promo.mp4")
    # write video (MoviePy will use ffmpeg; ensure ffmpeg available on host)
    final.write_videofile(video_path, fps=24, audio=False, verbose=False, logger=None)
    return video_path

# ---------------------------
# Offer banners (4 variants)
# ---------------------------
def create_offer_banners(topic, outdir):
    os.makedirs(outdir, exist_ok=True)
    offers = [
        ("🎉 Flat 50% Off — Enroll Today!", (255, 87, 34), (255, 152, 0)),
        ("🔥 Early Bird — Limited Seats!", (77, 182, 172), (0, 150, 136)),
        ("🚀 Join Now — Free Templates!", (63, 81, 181), (3, 169, 244)),
        ("🎓 Student Special — Discount!", (156, 39, 176), (103, 58, 183))
    ]
    for i, (offer_text, c1, c2) in enumerate(offers, start=1):
        # make gradient per-offer: top c1, bottom c2
        create_poster(f"{topic}\n{offer_text}", f"offer_{i}", outdir, size=(1200, 600), top_color=c1, bottom_color=c2)

# ---------------------------
# Master generator + ZIP builder (in-memory)
# ---------------------------
def generate_all_assets(topic, link):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    outdir = os.path.join("output", f"{topic.replace(' ', '_')}_{stamp}")
    os.makedirs(outdir, exist_ok=True)

    # 1. Main banner (large)
    create_poster(topic, "main_banner", outdir, size=THEME["banner_size"], top_color=THEME["colors"][0], bottom_color=THEME["colors"][1])

    # 2. Text files
    create_text_files(topic, outdir)

    # 3. Short video (~8s)
    create_short_video(topic, outdir)

    # 4. Blog + LinkedIn
    create_blog(topic, outdir)
    create_linkedin_post(topic, link, outdir)

    # 5. Offer posters
    create_offer_banners(topic, outdir)

    # 6. Make ZIP in-memory
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
        for foldername, _, filenames in os.walk(outdir):
            for fname in filenames:
                fullpath = os.path.join(foldername, fname)
                arcname = os.path.relpath(fullpath, outdir)
                zipf.write(fullpath, arcname)
    zip_buffer.seek(0)
    # Optionally: cleanup outdir (keep if you want)
    try:
        # remove created files to keep workspace clean
        for foldername, _, filenames in os.walk(outdir):
            for fname in filenames:
                os.remove(os.path.join(foldername, fname))
        os.rmdir(outdir)
    except Exception:
        pass

    return zip_buffer

# ---------------------------
# Streamlit UI (minimal: only download)
# ---------------------------
st.set_page_config(page_title="Digital Marketing Automation", page_icon="🎯", layout="centered")
st.title("🎯 Digital Marketing Automation App")
st.write("Generates banners, posters, short promo video, blog & LinkedIn post — then packages everything into a single ZIP for download.")

topic = st.text_input("Enter your campaign topic:", "Data Science Basic Training Program for Everyone")
link = st.text_input("Enter registration / campaign link:", "https://example.com")

if st.button("Generate & Download ZIP"):
    with st.spinner("Generating visuals — this may take a few seconds..."):
        zip_buffer = generate_all_assets(topic, link)
    st.success("✅ ZIP ready — click to download.")
    st.download_button(
        label="⬇️ Download All Marketing Assets (ZIP)",
        data=zip_buffer.getvalue(),
        file_name=f"marketing_assets_{topic.replace(' ','_')}.zip",
        mime="application/zip"
    )
