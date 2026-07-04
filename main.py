import PySimpleGUI as sg
import os
import json
import requests
import subprocess
import threading
from pathlib import Path
import webbrowser

# Initialize GUI
sg.theme('DarkBlue2')
sg.set_options(font=('Helvetica', 10))

# App data file
APP_DATA_FILE = 'apps_database.json'
DOWNLOADS_DIR = 'Downloads'

if not os.path.exists(DOWNLOADS_DIR):
    os.makedirs(DOWNLOADS_DIR)

# Default apps database
DEFAULT_APPS = {
    "apps": [
        {
            "name": "VLC Media Player",
            "category": "Media",
            "description": "Multimedia player for various formats",
            "link": "https://www.videolan.org/vlc/",
            "versions": ["3.0.16", "3.0.15", "3.0.14"]
        },
        {
            "name": "7-Zip",
            "category": "Utilities",
            "description": "File archiver with high compression ratio",
            "link": "https://www.7-zip.org/",
            "versions": ["23.01", "22.01", "21.07"]
        },
        {
            "name": "Notepad++",
            "category": "Development",
            "description": "Advanced text editor for coding",
            "link": "https://notepad-plus-plus.org/",
            "versions": ["8.5.4", "8.5.3", "8.5.2"]
        },
        {
            "name": "Blender",
            "category": "Graphics",
            "description": "3D modeling and animation software",
            "link": "https://www.blender.org/",
            "versions": ["3.6.1", "3.6.0", "3.5.1"]
        },
        {
            "name": "OBS Studio",
            "category": "Media",
            "description": "Open source streaming and recording software",
            "link": "https://obsproject.com/",
            "versions": ["30.0.2", "30.0.1", "29.1.3"]
        },
        {
            "name": "Audacity",
            "category": "Audio",
            "description": "Audio editing software",
            "link": "https://www.audacityteam.org/",
            "versions": ["3.4.1", "3.4.0", "3.3.3"]
        },
        {
            "name": "GIMP",
            "category": "Graphics",
            "description": "Image editor for photo retouching and manipulation",
            "link": "https://www.gimp.org/",
            "versions": ["2.10.36", "2.10.34", "2.10.32"]
        },
        {
            "name": "Python",
            "category": "Development",
            "description": "Python programming language",
            "link": "https://www.python.org/",
            "versions": ["3.12.0", "3.11.5", "3.10.13"]
        }
    ]
}

def load_apps_database():
    if os.path.exists(APP_DATA_FILE):
        with open(APP_DATA_FILE, 'r') as f:
            return json.load(f)
    else:
        save_apps_database(DEFAULT_APPS)
        return DEFAULT_APPS

def save_apps_database(data):
    with open(APP_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def download_app(app_name, version, link):
    """Simulate app download and open the link"""
    try:
        webbrowser.open(link)
        return True, f"Opening {app_name} v{version} download page"
    except Exception as e:
        return False, f"Error: {str(e)}"

def create_main_window():
    apps_data = load_apps_database()
    apps_list = [app['name'] for app in apps_data['apps']]
    
    layout = [
        [sg.Text('ThePancakeMEsiropi - App Store', font=('Helvetica', 16, 'bold'), text_color='#FFD700')],
        [sg.Text('_' * 80)],
        
        [sg.Text('Browse Apps:', font=('Helvetica', 12, 'bold'))],
        [sg.Listbox(apps_list, size=(50, 8), key='APP_LIST', enable_events=True)],
        
        [sg.Text('App Details:', font=('Helvetica', 12, 'bold'))],
        [sg.Multiline(size=(50, 4), key='APP_DETAILS', disabled=True, text_color='#00FF00', background_color='#000000')],
        
        [sg.Text('Select Version:', font=('Helvetica', 10, 'bold'))],
        [sg.Combo([], key='VERSION_COMBO', readonly=True, size=(30, 1))],
        
        [sg.Button('Download App', size=(15, 1), button_color=('white', '#0066CC')), 
         sg.Button('Refresh', size=(15, 1))],
        
        [sg.Text('_' * 80)],
        [sg.Text('Add Custom App Link:', font=('Helvetica', 12, 'bold'))],
        [sg.Text('App Name:'), sg.Input(key='CUSTOM_NAME', size=(30, 1))],
        [sg.Text('App Link:'), sg.Input(key='CUSTOM_LINK', size=(30, 1))],
        [sg.Text('Category:'), sg.Combo(['Games', 'Media', 'Development', 'Utilities', 'Graphics', 'Audio', 'Other'], 
                                        key='CUSTOM_CATEGORY', readonly=True, size=(28, 1))],
        [sg.Text('Version (comma-separated):'), sg.Input(key='CUSTOM_VERSION', size=(30, 1))],
        [sg.Button('Add Custom App', size=(15, 1), button_color=('white', '#00AA00')), 
         sg.Button('Exit', size=(15, 1), button_color=('white', '#CC0000'))],
        
        [sg.Text('_' * 80)],
        [sg.Multiline(size=(50, 3), key='STATUS', disabled=True, text_color='#FFFF00', background_color='#000000')]
    ]
    
    return sg.Window('ThePancakeMEsiropi App Store', layout, finalize=True)

def main():
    window = create_main_window()
    apps_data = load_apps_database()
    
    while True:
        event, values = window.read()
        
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        
        elif event == 'APP_LIST':
            if values['APP_LIST']:
                selected_app_name = values['APP_LIST'][0]
                for app in apps_data['apps']:
                    if app['name'] == selected_app_name:
                        details = f"Name: {app['name']}\n"
                        details += f"Category: {app['category']}\n"
                        details += f"Description: {app['description']}\n"
                        details += f"Link: {app['link']}"
                        window['APP_DETAILS'].update(details)
                        window['VERSION_COMBO'].update(values=app['versions'], value=app['versions'][0] if app['versions'] else '')
                        break
        
        elif event == 'Download App':
            if values['APP_LIST'] and values['VERSION_COMBO']:
                selected_app_name = values['APP_LIST'][0]
                selected_version = values['VERSION_COMBO']
                
                for app in apps_data['apps']:
                    if app['name'] == selected_app_name:
                        success, message = download_app(app['name'], selected_version, app['link'])
                        status_msg = f"✓ {message}" if success else f"✗ {message}"
                        window['STATUS'].update(status_msg)
                        break
            else:
                window['STATUS'].update('✗ Please select an app and version')
        
        elif event == 'Add Custom App':
            name = values['CUSTOM_NAME'].strip()
            link = values['CUSTOM_LINK'].strip()
            category = values['CUSTOM_CATEGORY'].strip()
            versions_str = values['CUSTOM_VERSION'].strip()
            
            if name and link and category and versions_str:
                versions = [v.strip() for v in versions_str.split(',')]
                new_app = {
                    "name": name,
                    "category": category,
                    "description": f"Custom app: {name}",
                    "link": link,
                    "versions": versions
                }
                apps_data['apps'].append(new_app)
                save_apps_database(apps_data)
                
                window['CUSTOM_NAME'].update('')
                window['CUSTOM_LINK'].update('')
                window['CUSTOM_CATEGORY'].update('')
                window['CUSTOM_VERSION'].update('')
                window['STATUS'].update(f"✓ App '{name}' added successfully!")
                
                window.close()
                window = create_main_window()
            else:
                window['STATUS'].update('✗ Please fill all fields')
        
        elif event == 'Refresh':
            apps_data = load_apps_database()
            apps_list = [app['name'] for app in apps_data['apps']]
            window['APP_LIST'].update(values=apps_list)
            window['STATUS'].update('✓ App list refreshed')
    
    window.close()

if __name__ == '__main__':
    main()
