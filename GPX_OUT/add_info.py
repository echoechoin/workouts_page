#!/usr/bin/python3
import click
from xml.dom.minidom import parse

@click.command()
@click.option('-g', '--gpx', help='gpx file path', type=click.Path(exists=True))
@click.option('-n', '--name', help='name of the gpx file', type=str)
def add_name(gpx, name):
    DOMTree = parse(gpx)
    collection = DOMTree.documentElement
    if collection.hasAttribute("name"):
        print("Root element : %s" % collection.getAttribute("name"))
    # 在集合中获取所有track
    tracks = collection.getElementsByTagName("trk")
    for track in tracks:
        name_tag = track.getElementsByTagName('name')
        if not name_tag:
            # add name tag
            name_tag = DOMTree.createElement('name')
            track.appendChild(name_tag)
            name_tag.appendChild(DOMTree.createTextNode(name))
        else:
            name_tag[0].firstChild.data = name
        
    with open(gpx, 'w') as f:
        DOMTree.writexml(f, encoding='utf-8')

if __name__ == '__main__':
    add_name()
