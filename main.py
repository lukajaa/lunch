import os
from PyPDF2 import PdfReader

menus = os.listdir('assets/menus')

excluded_words = ['M:', 'T:', 'W:', 'Th:', 'F:', '', 'with', 'and', 'or', '&', 'No', 'School']

lunches = []
words = {}

for menu in menus:
    if menu == '.DS_Store':
        continue
    reader = PdfReader('assets/menus/' + menu)
    for page in reader.pages:
        text = page.extract_text()
        for line in text.split('\n'):
            if "M:" in line or "T:" in line or "W:" in line or "Th:" in line or "F:" in line:
                lunches.append(line)
                for word in line.split(' '):
                    if word not in words:
                        words[word] = 1
                    else:
                        words[word] += 1

# sort words by frequency
sorted_words = sorted(words.items(), key=lambda x: x[1], reverse=True)

n = 1
for word in sorted_words:
    if word[0] not in excluded_words:
        print('{}. {}: {}'.format(n, word[0], words[word[0]]))
        n += 1
    if n > 75:
        break
