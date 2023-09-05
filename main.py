import fitz

doc = fitz.open()
page = doc.new_page()

order = ''
adress = ''
nl='\n'
text = f'{nl*5}{order}{nl*5}{adress}'
page.add_freetext_annot(
    page.rect+20,
    text,
    fontsize = 20,
    fontname = 'helv',
    rotate = 270
)


doc.save('test.pdf')
doc.close()