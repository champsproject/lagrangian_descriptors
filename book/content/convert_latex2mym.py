
def replace_citation_syntax(citations_matched_raw, item):
    item_modified = item
    for match in citations_matched_raw:
        bib_tags_raw = re.split(",", match)
        bib_tags_clean = [x.strip() for x in bib_tags_raw]
        #############################################
        # Replace LaTeX syntax with jekyll's in cell items
        #############################################
#         jekyll_syntax_items = ["{% cite"]+bib_tags_clean+['--file '+bib_filename]+["%}"]
        jekyll_syntax_items = ["{cite}`"]+[",".join(bib_tags_clean)]+["`"]
        separator = ''
        chunk_new = separator.join(jekyll_syntax_items)
        chunk_original = '\cite{'+match+'}'
        item_modified = item_modified.replace(chunk_original, chunk_new)
    return item_modified

def replace_bibliography_syntax(bibliography_matched_raw, item):
    # Only one single bibliography line exists
    bib_tags_raw = re.split(",", bibliography_matched_raw[0])
    bib_tags_clean = [x.strip() for x in bib_tags_raw]
    separator = ' '
    jekyll_syntax_items = ["{% bibliography"]+[separator.join(['--file', x]) for x in bib_tags_clean]+["--cited %}"]
    chunk_new = separator.join(jekyll_syntax_items)
    chunk_original = r'\bibliography{'+bibliography_matched_raw[0]+'}'
    item_modified = item.replace(chunk_original, chunk_new)
    return item_modified

def latex_to_jekyll_bib(nb):
    for i in range(len(nb['cells'])):
        cell = nb['cells'][i]
        for j in range(len(cell['source'])):
            item = cell['source'][j]

            citations_matched_raw = re.findall(citations_pattern,item)
            bibliography_matched_raw = re.findall(bibliography_pattern,item)

            if citations_matched_raw:
                item_modified = replace_citation_syntax(citations_matched_raw, item)
                nb['cells'][i]['source'][j] = item_modified

            elif bibliography_matched_raw:
                item_modified = replace_bibliography_syntax(bibliography_matched_raw, item)
                nb['cells'][i]['source'][j] = item_modified
                
            else:
                pass
    #############################################
    # Modify cell content with new syntax accordingly
    #############################################
    return nb
    

if __name__ == "__main__":
    import re
    import sys
    import json
    #############################################
    # Settings
    #############################################
    citations_pattern = re.compile(r'\\cite\{(.+?)\}')
    bibliography_pattern = re.compile(r'\\bibliography\{(.+?)\}')
    #############################################
    # Script input arguments (self-explanatory)
    #############################################
    nb_infile = sys.argv[1] 
    nb_outfile = sys.argv[2]
    bib_filename = sys.argv[3]
    #############################################
    # Load Jupyter Notebook as Dictionary
    #############################################
    try:
        with open(nb_infile,'r') as fp:
            nb = json.load(fp)
        fp.close()
        #############################################
        # Turn LaTeX label/ref syntax in Jupyter Noteboks into MD syntax
        #############################################
        nb_modified = latex_to_jekyll_bib(nb)
        
        with open(nb_outfile,'w') as fp:
            json.dump(nb_modified, fp)
            fp.close()
            print("New Notebook successfully generated")
    except:
        print("Couldn't find Jupyter Notebook. Check your input path")