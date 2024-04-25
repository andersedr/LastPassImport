from lxml import etree

def loadFile(): 
    # loadfile
    return etree.parse('TestXML.xml')

 
def main(): 
    # Load the file
    file = loadFile() 
  
    # Update the file
    stringTag = file.xpath('//String')    

    for e in stringTag:
        key = e.find('Key')
        if key.text == 'URL':
            value = e.find('Value')
            if value.text is None:
                print('URLFound Empty: Update text to "cseo.genmills.com"')
                value.text = 'CSEO.Import.genmills.com'
            else:
                value.text = value.text
        if key.text == 'UserName':
            value = e.find('Value')
            if value.text is None:
                print('UserName Found Empty: Update text to "cseo"')
                value.text = 'CSEO-import'
            else:
                value.text = value.text
            
    # write the file
    file.write('testOutput.xml')


if __name__ == "__main__": 
  
    # calling main function 
    main() 