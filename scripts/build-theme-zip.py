#!/usr/bin/env python3
"""Build a complete, uploadable copy of the UMS theme: stock Dawn v16.0.0 plus this repo's theme/ overlay.

Usage:  python3 scripts/build-theme-zip.py /path/to/dawn-v16.0.0-checkout out/ums-theme.zip

Then: upload the zip to the store's Files (stagedUploadsCreate + fileCreate), run themeCreate with the
file's CDN URL, wait for processing to finish, read every file back (checksums for code, parsed content
for JSON), and publish from admin. See README, "Pushing theme files".
"""
import json, os, shutil, sys, tempfile, zipfile

DAWN, OUT = sys.argv[1], sys.argv[2]
REPO = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'theme')
FOLDERS = ['assets', 'config', 'layout', 'locales', 'sections', 'snippets', 'templates']

def strip_header(text):
    """Shopify prefixes JSON it has written with a /* ... */ comment; the importer wants plain JSON."""
    if text.lstrip().startswith('/*') and '*/' in text:
        text = text[text.index('*/') + 2:].lstrip('\n')
    return text

with tempfile.TemporaryDirectory() as tmp:
    root = os.path.join(tmp, 'ums-theme')
    for folder in FOLDERS:
        shutil.copytree(os.path.join(DAWN, folder), os.path.join(root, folder))
    count = 0
    for base, _, files in os.walk(REPO):
        for name in files:
            src = os.path.join(base, name)
            rel = os.path.relpath(src, REPO)
            dst = os.path.join(root, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            body = open(src, encoding='utf-8').read()
            if rel.endswith('.json') and not rel.startswith('locales/') and rel != 'config/settings_schema.json':
                body = strip_header(body)
                json.loads(body)
            open(dst, 'w', encoding='utf-8').write(body)
            count += 1
    with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as zf:
        for base, _, files in os.walk(root):
            for name in sorted(files):
                path = os.path.join(base, name)
                zf.write(path, os.path.relpath(path, tmp))
    print(f'{OUT}: Dawn v16.0.0 plus {count} repo files')
