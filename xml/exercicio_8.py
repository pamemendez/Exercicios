import xml.etree.ElementTree as ET
tree = ET.parse('elementos.xml')
root = tree.getroot()
for elemento in root.findall('elemento'):
    nome = elemento.get('nome')
    detalhes = elemento.text
    print(f'Elemento: {nome}, Detalhes: {detalhes}')
