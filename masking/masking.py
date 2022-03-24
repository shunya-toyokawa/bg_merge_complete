from rembg.bg import remove
import numpy as np
import io
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

input_path = 'input.png'
output_path = 'cutout.png'

f = np.fromfile(input_path)
result = remove(f,
                alpha_matting=True,
                alpha_matting_foreground_threshold=240,
                alpha_matting_background_threshold=10,
                alpha_matting_erode_structure_size=10)
img = Image.open(io.BytesIO(result)).convert("RGBA")
img.save(output_path)
