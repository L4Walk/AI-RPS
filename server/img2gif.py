from PIL import Image
import os

# 获取所有图片的文件路径
img_dir = "G:/BlueShirt/AI-RPS/web/rps-web/src/assets/img"
img_files = [os.path.join(img_dir, img_file) for img_file in os.listdir(img_dir) if img_file.endswith(".png")]

# 打开所有图片
imgs = [Image.open(img_file) for img_file in img_files]

# 保存图片为 GIF
output_gif_path = "G:/BlueShirt/AI-RPS/web/rps-web/src/assets/gif.gif"
imgs[0].save(output_gif_path, save_all=True, append_images=imgs[1:], loop=0, duration=50)
