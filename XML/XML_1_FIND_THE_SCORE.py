import sys
import xml.etree.ElementTree as etree


def get_attr_number(root):
    count = len(root.attrib)
    for child in root:
        count += get_attr_number(child)
    return count


if __name__ == "__main__":
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
