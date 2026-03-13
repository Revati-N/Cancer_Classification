import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

# ---- CHANGE THIS to your folder path ----
root_folder = "Data/malignant"   # or "path/to/Malignant"
figure_title = "Example Images — Malignant Classes"  # change for Malignant
save_name = "malignant_samples.png"  # change for Malignant
# -----------------------------------------

subfolders = sorted([f for f in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, f))])

n = len(subfolders)
cols = math.ceil(math.sqrt(n))
rows = math.ceil(n / cols)

fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 4 * rows))
axes = axes.flatten() if n > 1 else [axes]

for i, (ax, folder) in enumerate(zip(axes, subfolders)):
    folder_path = os.path.join(root_folder, folder)
    images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tif'))]
    
    if images:
        img_path = os.path.join(folder_path, images[0])
        img = mpimg.imread(img_path)
        ax.imshow(img)
    
    ax.set_title(folder.replace("_", " ").title(), fontsize=13, fontweight='bold', pad=8)
    ax.axis('off')

# Hide any leftover empty axes
for ax in axes[n:]:
    ax.axis('off')

plt.suptitle(figure_title, fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(save_name, dpi=300, bbox_inches='tight')
plt.show()