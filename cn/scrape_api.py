import requests
import json
import time

BASE_URL = "https://nav.eooce.com/api"

def get_menus():
    try:
        response = requests.get(f"{BASE_URL}/menus")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching menus: {e}")
        return []

def get_cards(menu_id, submenu_id=None):
    try:
        params = {}
        if submenu_id:
            params['subMenuId'] = submenu_id
        
        response = requests.get(f"{BASE_URL}/cards/{menu_id}", params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching cards for menu {menu_id} submenu {submenu_id}: {e}")
        return []

def scrape():
    menus = get_menus()
    all_data = []

    print(f"Found {len(menus)} top-level menus.")

    for menu in menus:
        menu_id = menu['id']
        menu_name = menu['name']
        submenus = menu.get('subMenus', [])

        if submenus:
            print(f"Processing menu: {menu_name} (Has submenus)")
            for sub in submenus:
                sub_id = sub['id']
                sub_name = sub['name']
                full_category_name = f"{menu_name} - {sub_name}"
                
                print(f"  Fetching submenu: {sub_name} (ID: {sub_id})")
                cards = get_cards(menu_id, sub_id)
                
                if cards:
                    # Transform to our format
                    items = []
                    for card in cards:
                        items.append({
                            "title": card.get('title', 'No Title'),
                            "url": card.get('url', '#'),
                            "desc": card.get('desc', ''),
                            "logo": card.get('logo_url', '') or card.get('custom_logo_path', '') # Handle logo if present
                        })
                    
                    all_data.append({
                        "category": full_category_name,
                        "items": items
                    })
                    time.sleep(0.5) # Be nice to the server
        else:
            print(f"Processing menu: {menu_name} (No submenus)")
            cards = get_cards(menu_id)
            if cards:
                items = []
                for card in cards:
                    items.append({
                        "title": card.get('title', 'No Title'),
                        "url": card.get('url', '#'),
                        "desc": card.get('desc', ''),
                        "logo": card.get('logo_url', '') or card.get('custom_logo_path', '')
                    })
                
                all_data.append({
                    "category": menu_name,
                    "items": items
                })
                time.sleep(0.5)

    with open(r"c:\Users\24415\Desktop\github\WebStackPage.github.io\cn\links_output.json", "w", encoding="utf-8") as f:
        json.dump(all_data, f, ensure_ascii=False, indent=2)

    print("Scraping complete. Data saved to links_output.json")

if __name__ == "__main__":
    scrape()
