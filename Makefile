all: r-resseug.entries

s2m.fst : m2s.fst
	hfst-invert -i $< -o $@

lex.m2m.fst : lex.m2m.lexc
	hfst-lexc -o $@ < $<

m2s.fst : lex.m2m.fst rul.m2s.fst delete.fst
	hfst-compose-intersect -1 lex.m2m.fst -2 rul.m2s.fst | hfst-compose -2 delete.fst -o $@

rul.m2s.fst : rul.m2s.twolc
	hfst-twolc -i $< -o $@

delete.fst :
	echo 'Ø -> 0' | hfst-regexp2fst > $@

sktp-r.words: sktp-all.words
	egrep '^r[a-zäöšž]+$' sktp-all.words > sktp-r.words

sktp-r.fst:
	hfst-strings2fst -j -i sktp-r.words > sktp-r.fst

r-guesser.fst: sktp-r.fst ../twolex/fin-guess.fst ../twolex/guesser.fst Makefile
	hfst-compose -2 sktp-r.fst -1 ../twolex/fin-guess.fst -o r-guesser.fst

unique-words.fst: unique.words
	hfst-strings2fst -j -i $< > $@

unique-guesser.fst: unique-words.fst ../twolex/fin-guess.fst ../twolex/guesser.fst Makefile
	hfst-compose -2 $< -1 ../twolex/fin-guess.fst -o $@

#r-resseug.fst: r-guesser.fst Makefile
#	hfst-invert -i r-guesser.fst | hfst-minimize -o r-resseug.fst

r-guesser.entries: r-guesser.fst Makefile
	hfst-project -p input -i $< | hfst-minimize | hfst-fst2strings | sort | uniq > $@
