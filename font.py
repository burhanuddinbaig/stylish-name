import os
from fontTools.ttLib import TTFont

def get_glyphs_from_text(text, font_path):
    font = TTFont(font_path)
    cmap = font['cmap']
    unicode_map = cmap.getBestCmap()
    glyphs = []
    for char in text:
        code_point = ord(char)
        if code_point in unicode_map:
            glyphs.append((char, f"U+{code_point:04X}", unicode_map[code_point]))
        else:
            glyphs.append((char, f"U+{code_point:04X}", None))
    return glyphs

def process_fonts(directory, text):
    font_data = {}
    for root, dirs, files in os.walk(directory):
        category = os.path.basename(root)
        if category not in font_data:
            font_data[category] = []
        for filename in files:
            if filename.endswith('.ttf') or filename.endswith('.otf'):
                font_path = os.path.join(root, filename)
                glyphs = get_glyphs_from_text(text, font_path)
                font_info = {
                    'font': filename,
                    'glyphs': glyphs
                }
                font_data[category].append(font_info)
    return font_data