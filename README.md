# guessing (obsolete)

This repository is now **obsolete and will be deleted in near future**. The relevant stuff can be found in either *pytwolc* or in *twolex* repository.

Guessing lexicon entries using an open lexicon using regular expressions

Using hfst-lexc one can create a lexicon which has regular expressions instead of explicit root or stems. Such an open lexicon will produce ambiguous analyses, i.e. often several possible entries which could exist but not necessarily do exist. Such an open lexicon is operational with a rule grammar just as a normal lexicon.

One may use such an open lexicon for deducing word entries for unknown words. Feeding one form of the unknown word, one usually gets several possible entries. Feding another form of the same word will produce another set of possible entries. The intersection of those sets is relevant. If only one entry is left, then that is the desired result. Otherwise the user has to give yet another form.

This mechanism is language independent, and can be implemented using the HFST-Python interface. For each language, the open lexicon and rules are needed. Essentially, one often has a lexicon for model words and the rules. The task is then to modify such a lexicon into an open lexicon.
