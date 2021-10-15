import xml.etree.ElementTree as ET
from cairosvg import svg2png
import concurrent.futures
from itertools import groupby
def createSVG(pathElement, name):
    # create an SVG file from a path
    aspect_ratio = 915.30658 / 1460.156
    width = 500
    height = width * aspect_ratio
    svgString = f" <svg id=\"map\" width=\"{width}\" height=\"{height}\" version=\"1\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:svg=\"http://www.w3.org/2000/svg\" xmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\" viewBox=\"0 0 {width} {height}\" preserveAspectRatio=\"xMinYMin\" data-originalStrokeWidth=\"0.3\">\n\t{pathElement}\n</svg>"
    dil = name.find('__')
    try:
        if(dil != -1):
            svg2png(bytestring=svgString, write_to=f"counties/{name[dil+2:]}_{name[:dil]}.png")
        else:
            svg2png(bytestring=svgString, write_to=f"counties/{name}.png")
    except(e):
        print(name)

def process(child):
    #i = 0
    #for child in root:
    if(child.tag == "{http://www.w3.org/2000/svg}path"):
        createSVG("<" + ET.tostring(child).decode()[5:], child.attrib['id'])
            # i+=1
            # print(i)

def loadSVG(xmlfile):
    # loads an SVG File and parses

    tree = ET.parse(xmlfile)
    root = tree.getroot()
    return root



def main():
    root = loadSVG("./map.svg")
    executor = concurrent.futures.ProcessPoolExecutor()
    futures = [executor.submit(process, element) for element in root]
    concurrent.futures.wait(futures)   

if __name__ == "__main__":
    main()
