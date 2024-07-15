from imarkdown import MdFile, LocalFileAdapter, MdImageConverter

def main():
    adapter = LocalFileAdapter()
    converter = MdImageConverter(adapter=adapter)
    
    md_file = MdFile(name="GRID-VISUALIZER-rawimages.md")
    converter.convert(md_file)

if __name__ == '__main__':
    main()
