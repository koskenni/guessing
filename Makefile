s2m.fst : m2s.fst
	hfst-invert -i $< -o $@

lex.m2m.fst : lex.m2m.lexc
	hfst-lexc -o $@ < $<

m2s.fst : lex.m2m.fst rul.m2s.fst
	hfst-compose-intersect -1 lex.m2m.fst -2 rul.m2s.fst | hfst-compose -2 delete.fst -o $@

