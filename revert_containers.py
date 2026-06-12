import os
files = ['templates/About.html', 'templates/Contact.html', 'templates/features.html', 'templates/index.html']
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('class="container premium-footer py-5"', 'class="container-fluid premium-footer py-5 px-sm-3 px-md-5"')
    content = content.replace('class="container bg-dark py-4"', 'class="container-fluid bg-dark py-4 px-sm-3 px-md-5"')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Reverted!')
