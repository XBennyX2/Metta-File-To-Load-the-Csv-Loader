! (register-module! ../wrapper)
! (import! &self wrapper:func)


!(bind! &some (new-space))

(=(Loader $t $y) (let $x (load_csv $t) (add-atom $y $x)))

!(Loader truth_large.csv &some)

!(match &some (True $x $Y $c $v) ($v))
