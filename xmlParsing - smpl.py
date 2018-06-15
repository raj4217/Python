# import xml.sax
import xml.etree.ElementTree as et


tree = et.parse('smpl.xml')
root = tree.getroot()
# [print(child.tag,child.attrib) for child in root]
for child in root:
    for elm in child:
        print(elm.tag, ':', elm.text)
