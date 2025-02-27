! (register-module! ../CSV_Loader)
! (import! &self CSV_Loader:func)


!(bind! &some (new-space))

;The Loader Takes as an Input $t which is the location of the csv file that is going to be loaded and $y is the space name that is created above
; it takes $t and $y as an argument and calls the load_csv function then add the converted csv files to the new created space which is $y
;Note that when passing the space name dont forget to add & at the beggining of your new space name.

(=(Loader $t $y) (let $x (load_csv $t) (add-atom $y $x)))

;Make sure The Truth.csv file has a format of A,B,C,D,....TruthValue
!(Loader truth.csv &some)


!(match &some (True $x $Y $c $v $b) ($v))
