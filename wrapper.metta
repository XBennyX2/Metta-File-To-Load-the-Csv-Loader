! (register-module! ../wrapper)
! (import! &self wrapper:func)

; ! (bind! load_csv (py-atom load_csv (-> String String List)))
; ! (get-type load_csv)
!(bind! &some (new-space))
!(let $x (load_csv truth.csv) (add-atom &some ($x)))
; (load_csv "truth_large.csv" "mySpace")

!(match &some (True $x $Y $c $v) ($v))