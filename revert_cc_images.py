import re

import subprocess

curr_path = r"D:\Plastroots_Website\src\data\ProductsServicesData.js"
orig_content = subprocess.check_output(['git', 'show', 'HEAD:src/data/ProductsServicesData.js']).decode('utf-8')

with open(curr_path, "r", encoding="utf-8") as f:
    curr_content = f.read()

sections = ["epr", "carbon-market", "esg-consulting"]

def extract_images(content, sec_id):
    pattern = r'("id"\s*:\s*"' + sec_id + r'")'
    parts = re.split(pattern, content)
    if len(parts) < 3: return None
    post = parts[2]
    
    # get overview image
    img_match = re.search(r'"imagePath"\s*:\s*"([^"]+)"', post)
    overview_img = img_match.group(1) if img_match else None
    
    # get gallery images
    gallery_match = re.search(r'"gallery"\s*:\s*\[(.*?)\]', post, flags=re.DOTALL)
    gallery_imgs = []
    if gallery_match:
        gallery_block = gallery_match.group(1)
        gallery_imgs = re.findall(r'"img"\s*:\s*"([^"]+)"', gallery_block)
        
    return overview_img, gallery_imgs

for sec in sections:
    orig_overview, orig_gallery = extract_images(orig_content, sec)
    
    # Now replace in curr_content
    pattern = r'("id"\s*:\s*"' + sec + r'")'
    parts = re.split(pattern, curr_content)
    if len(parts) > 2:
        pre = parts[0]
        id_str = parts[1]
        post = parts[2]
        
        # replace overview image
        if orig_overview:
            post = re.sub(r'"imagePath":\s*"[^"]+"', f'"imagePath": "{orig_overview}"', post, count=1)
            
        # replace gallery images
        # We need to replace them one by one in order
        if orig_gallery:
            def replacer(match):
                replacer.count += 1
                if replacer.count <= len(orig_gallery):
                    return f'"img": "{orig_gallery[replacer.count - 1]}"'
                return match.group(0)
            replacer.count = 0
            
            # extract gallery block to avoid replacing outside of gallery
            gallery_match = re.search(r'"gallery"\s*:\s*\[.*?\]', post, flags=re.DOTALL)
            if gallery_match:
                gallery_block = gallery_match.group(0)
                new_gallery_block = re.sub(r'"img"\s*:\s*"[^"]+"', replacer, gallery_block, count=len(orig_gallery))
                post = post.replace(gallery_block, new_gallery_block, 1)
                
        curr_content = pre + id_str + post

with open(curr_path, "w", encoding="utf-8") as f:
    f.write(curr_content)

print("Corporate compliance images reverted successfully!")
