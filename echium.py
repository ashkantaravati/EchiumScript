from utils import EchiumTree


def main():
    f = open('src/render.ech')
    fo = f.read()
    tree = EchiumTree(fo)
    tree.parse()
    output = tree.render()
    new_f = open('src/output.html','w')
    new_f.write(output)


if __name__ == "__main__":
    main()
