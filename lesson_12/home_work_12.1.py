
#  12.1. Очистити текст від html-тегів

import codecs

def delete_html_tags(html_file, result_file='cleaned.txt', remove_empty_lines=True):

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()

    result = []
    inside_tag = False

    for ch in html:
        if ch == '<':
            inside_tag = True
            continue
        if ch == '>':
            inside_tag = False
            continue

        if not inside_tag:
            result.append(ch)
    clean_text = ''.join(result)


    if remove_empty_lines:
        lines = clean_text.splitlines()
        lines = [line.strip() for line in lines if line.strip()]
        clean_text = '\n'.join(lines)


    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(clean_text)

if __name__ == "__main__":
    delete_html_tags('draft.html')
    print("OK: cleaned.txt created")


import codecs

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as f:
        html = f.read()

    result = []
    inside_tag = False

    for ch in html:
        if ch == '<':
            inside_tag = True
            result.append(' ')
            continue
        if ch == '>':
            inside_tag = False
            continue

        if not inside_tag:
            result.append(ch)

    clean_text = ''.join(result)

    with codecs.open(result_file, 'w', 'utf-8') as f:
        f.write(clean_text)


if __name__ == "__main__":
    delete_html_tags("draft.html", "cleaned.txt")
    print("OK")