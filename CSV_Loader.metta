! (register-module! ../wrapper)
! (import! &self wrapper:func)


!(bind! &some (new-space))

;The Loader Takes as an Input $t which is the location of the csv file that is going to be loaded and $y is the space name that is created above
; it takes $t and $y as an argument and calls the load_csv function then add the converted csv files to the new created space which is $y
;Note that when passing the space name dont forget to add & at the beggining of your new space name.

(=(Loader $t $y) (let $x (load_csv $t) (add-atom $y $x)))

;Make sure The Truth.csv file has a format of A,B,C,D,TruthValue

!(unify (False (A False) (B True) (C True) (D True) (E True)) ($truth-val ($A $T1)($B $T2)($C $T3)($D $T4)($E $T5)) True False)

!(Loader truth.csv &some)

; !(assertEqual
;     (match &some ($tv $a $b $c $d) ($tv $a $b $c $d))
;     (match &some ($tv $a $b $c $d) ($tv $a $b $c $d))
; )

!(match &some $x $x)
