.PHONY: all audit
all:
	lake build

audit: all
	lake env lean evidence/final-library-axioms.lean
	lake env lean evidence/exported-correspondence-axioms.lean
