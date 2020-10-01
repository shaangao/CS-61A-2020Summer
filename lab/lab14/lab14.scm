(define (split-at lst n)
  (cond ((= n 0) (cons nil lst))
  		((null? lst) (cons lst nil))
		(else (cons 
				(cons (car lst) (car (split-at (cdr lst) (- n 1)))) 
				(cdr (split-at (cdr lst) (- n 1)))
				)
		)
  )
)


(define-macro (switch expr cases)
	(cons `cond
		(map (lambda (case) (cons `(equal? ,expr (quote ,(car case))) (cdr case)))
    			cases))		; returns a list of pairs, with the first element of each pair being a boolean value and the second being (cdr case); every pair is a clause for "cond"
)

