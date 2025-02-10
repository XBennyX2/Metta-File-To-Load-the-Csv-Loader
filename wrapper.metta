! (register-module! ../wrapper)
! (import! &self wrapper:func)

; ! (bind! load_csv (py-atom load_csv (-> String String List)))
; ! (get-type load_csv)
!(let $x (load_csv truth.csv) (add-atom &self (collapse (superpose $x))))
; (load_csv "truth_large.csv" "mySpace")

(match )