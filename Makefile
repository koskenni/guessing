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
