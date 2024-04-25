from lxml import etree

def loadFile(): 
    # loadfile
    return etree.parse ( 'TestXML.xml' )

 
def main(): 
    # Load the file
    file = loadFile() 
  
    # Update the file
    stringTag = file.xpath('//String')    

    for e in stringTag:
        key = e.find('Key')
        if key.text == 'URL':
            value = e.find('Value')
            print('URLFound: Update text to "cseo.genmills.com"')
            value.text = 'cseo.genmills.com'
            
    # write the file
    file.write('testOutput.xml')


if __name__ == "__main__": 
  
    # calling main function 
    main() 