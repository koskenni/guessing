# entryharvester.py

copyright = """Copyright © 2017, Kimmo Koskenniemi

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import hfst, sys, argparse

argparser = argparse.ArgumentParser("python3 entryharvester.py",
                                    description="Extracts lexicon entries from corpus data")
argparser.add_argument("-g", "--guesser", default="../twolex/fin-guess.fst")
argparser.add_argument("-r", "--restrictions", default="r-guesser.fst")
argparser.add_argument("-m", "--minimum_forms", type=int, default=8)
args = argparser.parse_args()

gfil = hfst.HfstInputStream(args.guesser)
gfst = gfil.read()
gfst.invert()
gfst.lookup_optimize()

def unique_entry(word_forms):
    remaining = set()
    first = True
    for word_form in word_forms:
        entries_and_weights = gfst.lookup(word_form, output="tuple")
        entries = set()
        for e,w in entries_and_weights:
            entries.add(e)
        if first:
            first = False
            remaining = entries
        else:
            remaining = remaining & entries
        if len(remaining) <= 1:
            break
    return remaining

pfil = hfst.HfstInputStream(args.restrictions)
pfst = pfil.read()
pfst.minimize()
pfst.lookup_optimize()

efil = open("r-guesser.entries", 'r')
for entry in efil:
    entry = entry.strip()
    # print("\n\n" + entry) ##
    result = pfst.lookup(entry, output="tuple")
    if len(result) <= args.minimum_forms:
        continue
    word_forms = [wd for wd,wg in result]
    entries = unique_entry(word_forms)
    if len(entries) == 1:
        print("---", entry, " ".join(word_forms))
    #else:
    #    print("\t\t", entry, " ".join(word_forms))
