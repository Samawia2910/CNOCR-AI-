from cnocr import CnOcr
img_fp = 'cnocr.jpg'
ocr = CnOcr()  # Use default values for all parameters
out = ocr.ocr(img_fp)
print(out)