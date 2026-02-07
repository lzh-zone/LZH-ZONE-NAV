import json
import os

# Updated Icon Mapping
ICON_MAP = {
    # Main Categories
    "Home": "fa-home",
    "Ai-stuff": "fa-robot",
    "Cloud": "fa-cloud",
    "Container": "fa-box-open",
    "Software": "fa-compact-disc",
    "Tools": "fa-tools",
    "Mail & Domain": "fa-envelope",
    "Dev": "fa-code",
    
    # Subcategories (mapped by full name)
    "Container - Game Server": "fa-gamepad",
    "Software - Proxy": "fa-globe",
    "Software - Macos": "fa-apple",
    "Tools - Free SMS": "fa-sms",
    "Tools - Other": "fa-ellipsis-h",
    "Server": "fa-server",
    "Monitor": "fa-chart-line"
}

DEFAULT_ICON = "fa-folder"
DEFAULT_LOGO = "../assets/images/favicon.png" # Fallback if no logo

def get_icon(category):
    return ICON_MAP.get(category, DEFAULT_ICON)

def generate_html():
    json_path = r"c:\Users\24415\Desktop\github\WebStackPage.github.io\cn\links_output.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} not found.")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    html = []
    html.append('<!DOCTYPE html>')
    html.append('<html lang="zh-CN">')
    html.append('<head>')
    html.append('    <meta charset="UTF-8">')
    html.append('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
    html.append('    <title>LZH-ZONE - 个人导航</title>')
    html.append('    <link rel="shortcut icon" href="../assets/images/favicon.png">')
    html.append('    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">')
    html.append('    <link rel="stylesheet" href="../assets/css/lzh-modern.css">')
    html.append('    <style>')
    html.append('        /* Brief inline fix if card-content was missing but used in previous iterations */')
    html.append('        /* We are using card-header now, so this is just cleanup */') 
    html.append('    </style>')
    html.append('</head>')
    html.append('<body>')
    html.append('')
    html.append('    <!-- Mobile Header -->')
    html.append('    <header class="mobile-header">')
    html.append('        <div class="logo">LZH-ZONE</div>')
    html.append('        <button class="menu-toggle" aria-label="Toggle Menu"><i class="fas fa-bars"></i></button>')
    html.append('    </header>')
    html.append('')
    html.append('    <div class="app-container">')
    html.append('        <!-- Sidebar -->')
    html.append('        <aside class="sidebar">')
    html.append('            <div class="sidebar-header">')
    html.append('                <div class="logo">LZH-ZONE</div>')
    html.append('            </div>')
    html.append('            <nav class="sidebar-nav">')
    html.append('                <ul>')
    
    # Generate Sidebar Links
    for cat in data:
        cat_name = cat['category']
        icon = get_icon(cat_name)
        # Use only the last part of "A - B" for display if it's too long? 
        # Actually user might prefer full name for clarity. 
        # But "Container - Game Server" is long.
        display_name = cat_name.split(' - ')[-1] if ' - ' in cat_name else cat_name
        
        # Use the full name for ID to avoid collisions
        html.append(f'                    <li><a href="#{cat_name}"><i class="fas {icon}"></i> <span>{display_name}</span></a></li>')
    
    html.append('                </ul>')
    html.append('            </nav>')
    html.append('        </aside>')
    html.append('')
    html.append('        <!-- Main Content -->')
    html.append('        <main class="main-content">')
    
    # Generate Sections
    for cat in data:
        cat_name = cat['category']
        items = cat['items']
        icon = get_icon(cat_name)
        display_name = cat_name # Full name in header is fine
        
        html.append(f'            <section id="{cat_name}" class="content-section">')
        html.append(f'                <h2 class="section-title"><i class="fas {icon}"></i> {display_name}</h2>')
        html.append('                <div class="grid-container">')
        
        for item in items:
            title = item.get('title', 'No Title')
            url = item.get('url', '#')
            desc = item.get('desc', '') or ''
            logo = item.get('logo', '')
            
            if not logo:
                logo = DEFAULT_LOGO
                
            # Fallback for logo error handled by onerror
            
            html.append(f'                    <a href="{url}" target="_blank" class="card">')
            html.append('                        <div class="card-header">')
            html.append('                            <div class="card-icon">')
            html.append(f'                                <img src="{logo}" alt="{title}" onerror="this.src=\'{DEFAULT_LOGO}\'">')
            html.append('                            </div>')
            html.append(f'                            <h3 class="card-title">{title}</h3>')
            html.append('                        </div>')
            html.append(f'                        <p class="card-desc">{desc}</p>')
            html.append('                    </a>')
            
        html.append('                </div>')
        html.append('            </section>')
    
    html.append('        </main>')
    html.append('    </div>')
    html.append('')
    html.append('    <script src="../assets/js/lzh-main.js"></script>')
    html.append('</body>')
    html.append('</html>')

    output_path = r"c:\Users\24415\Desktop\github\WebStackPage.github.io\cn\index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write('\n'.join(html))
    print(f"Generated {output_path} with {len(data)} categories.")

if __name__ == "__main__":
    generate_html()
