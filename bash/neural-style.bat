docker run -it -v /c/Users/hschoonjans/Documents/GitHub/data/neural-style/:/root/input-images/ heschoon/neural-style /bin/bash
cd ~/neural-style/
time th neural_style.lua -gpu -1 -style_image ../input-images/style.jpg -content_image ../input-images/content.jpg -image_size 256