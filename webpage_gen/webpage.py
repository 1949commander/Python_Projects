import dominate
from dominate.tags import *


def create_page():
    doc = dominate.document(title='Example Table')

    with doc.head:
        link(rel='stylesheet', href='style.css')

    with doc:
        with div(cls='container'):
            body('Stay tuned for our amazing summer sale!')
    with open('index.html', 'w') as file:
        file.write(doc.render())

create_page()
