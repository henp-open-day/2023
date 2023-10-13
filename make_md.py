import glob
import os

def main():
    md_str = '''# HENP Open Day 2023

顕微鏡の画像は以下からダウンロード頂けます。

'''

    files =  sorted([file for file in glob.glob('images/*')])
    toc_str = ''
    image_str = ''
    for file in files:
        filepath = os.path.dirname(file)
        name, ext = os.path.splitext(os.path.basename(file))
        toc_str += f"- [{name}](#{name})\n"
        image_str += f"""## {name}

![]({file})
"""
    md_str += toc_str + "\n" + image_str + "\n"

    print(md_str)
    with open('index.md', 'w') as f:
        f.write(md_str)


if __name__ == '__main__':
    main()
