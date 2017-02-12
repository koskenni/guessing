import sys, fileinput, io, hfst
s2e_file = hfst.HfstInputStream("s2m.fst")
s2e = s2e_file.read()
# print(s2e.number_of_states())

def print_results(paths):
    for path in paths.strip().split('\n'):
        print("\t" + path.split(':')[0])

while True:
    res = hfst.regex("?*")
    # print(res)
    print("Enter forms of the next lemma")
    while True:
        try:
            line = input()
        except EOFError:
            sys.exit()
        l = " ".join(list(line.strip()))
        # print("word = " + l)
        a = hfst.regex(l)
        a.compose(s2e)
        a.output_project()
        a.minimize()
        a.extract_paths(max_number=10)
        a.minimize()
    
        nps = a.extract_paths(output='text')
        # print("    tentative new entries = ")
        # print_results(nps)
        
        # res.conjunct(a)
        res.intersect(a)
        res.minimize()
        paths = res.extract_paths(output='text')
        print("    remaining possible entries = ")
        print_results(paths)

        n = paths.count(':')
        if n == 0:
            print("conflicting forms")
            break
        if n == 1:
            print("entry now fully determined")
            break

