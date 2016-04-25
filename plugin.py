#! /usr/bin/env python3

from tkinter import Tk
import sys, re
import sigil_bs4

def href_to_basename(href, ow=None):
    if href is not None:
        return href.split('/')[-1]
    return ow

def files_iter(bk, on_selected):
    if on_selected:
        for file_type, file_id in bk.selected_iter():
            if file_type == 'manifest' and \
                    bk.id_to_mime(file_id) == 'application/xhtml+xml':
                yield file_id, bk.id_to_href(file_id)
    else:
        for file_id, file_href in bk.text_iter():
            yield file_id, file_href
            
def run(bk):
    title_regex = Tk().clipboard_get()
    if any(bk.selected_iter()):
        on_selected = True
    else:
        on_selected = False
    for file_id, file_href in files_iter(bk, on_selected):
        xhtml_file = bk.readfile(file_id)
        xhtml_soup = sigil_bs4.BeautifulSoup(xhtml_file, 'lxml')
        # There's a typo in bk.href_to_basename until version 0.9.5 of Sigil
        if bk.launcher_version() <= 20160325:
            file_name = href_to_basename(file_href)
        else:
            file_name = bk.href_to_basename(file_href)
        file_name = file_name[:file_name.rindex(".")]
        try:
            title_string = re.search(title_regex, file_name).group()
        except AttributeError:
            title_string = file_name
        if not xhtml_soup.head.title:
            title = xhtml_soup.new_tag("title")
            xhtml_soup.head.append(title)
        xhtml_soup.head.title.string = title_string
        bk.writefile(file_id, xhtml_soup.prettyprint_xhtml(indent_chars="  "))
    return 0

def main():
    print("I reached main when I should not have\n")
    return -1

if __name__ == "__main__":
    sys.exit(main())