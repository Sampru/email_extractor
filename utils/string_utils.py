
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

def create_output(emails):
    file = open('testfile.txt', 'w')
    for em in sorted(set(emails)):
        print('%s ' % em)
        file.write('%s; ' % em)
    file.close()
