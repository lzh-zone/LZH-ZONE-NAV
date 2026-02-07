import re
import json
import os

file_path = r"c:\Users\24415\Desktop\github\WebStackPage.github.io\cn\index.html"

encodings = ['utf-8', 'gb18030', 'utf-16', 'cp936']

content = ""
used_encoding = ""

for enc in encodings:
    try:
        with open(file_path, "r", encoding=enc) as f:
            content = f.read()
            used_encoding = enc
            break
    except Exception:
        continue

if not content:
    print(json.dumps({"error": "Failed to read file with any encoding"}))
    exit()

# Parse
try:
    cat_pattern = re.compile(r'<h4 class="text-gray">.*?id="([^"]+)".*?</h4>(.*?)(?=<h4|$)', re.DOTALL)
    # Updated regex to handle onclick URLs
    # Structure: <div class="xe-widget ... onclick="window.open('URL'..."> ... <strong>Title</strong> ... <p>Desc</p>
    
    # We first split by xe-widget to get individual items
    widget_pattern = re.compile(r'<div class="xe-widget(.*?)</div>\s*</div>\s*</div>', re.DOTALL)
    
    # Inside a widget, find URL, Title, Desc
    url_pattern = re.compile(r"onclick=\"window\.open\('([^']+)'")
    title_pattern = re.compile(r'<strong>(.*?)</strong>', re.DOTALL)
    desc_pattern = re.compile(r'<p.*?>(.*?)</p>', re.DOTALL)

    matches = cat_pattern.findall(content)
    
    data = []
    
    for cat_name, cat_html in matches:
        items = []
        # Find all widgets in this category block
        widgets = widget_pattern.findall(cat_html)
        
        # If widget_pattern fails (nested divs are tricky with regex), let's try a simpler approach text-stream approach
        # or just find all matches of the parts in sequence.
        
        # Let's try finding all occurrences of the patterns in the category HTML chunk
        # But we need to keep them grouped.
        
        # Alternative: The structure is consistent.
        # <div class="xe-widget ... onclick="..."> ... <strong> ... <p>
        
        # Let's use a combined pattern for the widget block
        # Note: the closing </div>s might be irregular.
        # Let's search for the start "xe-widget" and capture until the recognized end or next widget.
        
        # Actually, let's just find all matches of the "onclick" and then the next "strong" and "p".
        # This assumes strictly ordered HTML which seems true here.
        
        # Regex: onclick="window.open('URL'...).*?<strong>Title</strong>.*?<p...>Desc</p>
        item_full_pattern = re.compile(r"onclick=\"window\.open\('([^']+)'[^>]*>.*?<strong>(.*?)</strong>.*?<p.*?>(.*?)</p>", re.DOTALL)
        
        item_matches = item_full_pattern.findall(cat_html)
        
        for url, title, desc in item_matches:
            items.append({
                "title": title.strip(),
                "url": url.strip(),
                "desc": desc.strip()
            })
        
        if items:
            data.append({
                "category": cat_name.strip(),
                "items": items
            })

    with open(r"c:\Users\24415\Desktop\github\WebStackPage.github.io\cn\links_output.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

except Exception as e:
    with open(r"c:\Users\24415\Desktop\github\WebStackPage.github.io\cn\links_output.json", "w", encoding="utf-8") as f:
        json.dump({"error": str(e)}, f)
