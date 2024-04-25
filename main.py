from lxml import etree

def loadFile(): 
    #loadfile
    doc = etree.parse ( 'test.xml' )
 
def main(): 
    # load rss from web to update existing xml file 
    loadRSS() 

if __name__ == "__main__": 
  
    # calling main function 
    main() 