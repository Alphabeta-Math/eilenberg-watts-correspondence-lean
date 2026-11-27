# Eilenberg–Watts correspondence

The correspondence identifies bimodules over arbitrary associative unital rings with additive functors between module categories that preserve finite colimits and arbitrary coproducts in the stated universes. Tensoring with a bimodule gives the forward functor; evaluation at the lifted regular module gives the explicit inverse, with right action induced by right multiplication. Natural transformations correspond to bimodule maps.

```lean
import EilenbergWatts

#check NotesProofs.General.ConcreteBimodule.eilenbergWattsCanonical
#check NotesProofs.General.ConcreteBimodule.eilenbergWattsCanonical_inverse
#check NotesProofs.General.originalWattsWithEvaluation
#check NotesProofs.General.originalWatts_inverse_forget
#check NotesProofs.General.originalWatts_inverse_right
#check EilenbergWatts
#check BimoduleFunctorHomEquivalence
#check ReviewedOriginalWattsConnection
```

All 35 reviewed lecture-note results, including the categorical bimodule dictionary and generator reconstruction, are exported by `import EilenbergWatts`. Their exact statements and source locations are in [PROJECT.md](PROJECT.md). The same import exports the checked original-form correspondence adapter with its tensor, unit, composition and regular-evaluation formulas.

This development uses ordinary classical choice. Historical namespace names containing `ChoiceFreeWatts` do not assert a choice-free theorem; the allowed axiom policy is `propext`, `Classical.choice`, and `Quot.sound`.
