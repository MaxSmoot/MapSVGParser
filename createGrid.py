from PIL import Image
import json
import os
import concurrent.futures

def hash(table: "list[list[str]]", filename):
    if not filename.endswith(".png"):
        return
    im = Image.open(f"counties/{filename}")
    rgb_im = im.convert('RGB')
    # new_im = Image.new(mode = "RGB", size = (len(table),len(table[0])), color = (0,0,0))
    # pixels = new_im.load()
    for i in range(len(table)):
        for j in range(len(table[0])):
            r, g, b = rgb_im.getpixel((i,j))
            if(r+g+b > 0):
                table[i][j] = filename[:filename.find('.')]
                # pixels[i,j] = (255,255,255)
    # new_im.save("recreated.png")

def main():
    im = Image.open("counties/AL_Bibb.png")
    Matrix = [["" for x in range(im.height)] for y in range(im.width)]
    # executor = concurrent.futures.ProcessPoolExecutor()
    # futures = [executor.submit(hash, Matrix, filename) for filename in os.listdir("counties")]
    # concurrent.futures.wait(futures)   
    for filename in os.listdir("counties"):
        hash(Matrix, filename)
        
    json_string = json.dumps(Matrix)

    print(json_string)

if __name__ == "__main__":
    main()