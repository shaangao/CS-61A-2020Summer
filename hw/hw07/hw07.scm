(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cdr (cdr s))))

(define (sign num) (cond ((< num 0) -1) ((= num 0) 0) ((> num 0) 1)))

(define (square x) (* x x))

(define (pow x y) 
  (cond
    ((= y 0) 1)
    ((even? y) (pow (square x) (/ y 2)))
    ((odd? y) (* x (pow (square x) (/ (- y 1) 2))))))

(define (unique s) 
  (if (null? s) nil
      (cons (car s) (unique (filter (lambda (x) (not (eq? x (car s)))) (cdr s))))))

(define (replicate x n)
  (define (helper x n lst)
    (if (= n 0) lst 
        (helper x (- n 1) (append (list x) lst))))
  (helper x n nil))

(define (accumulate combiner start n term)
  (if (= n 0) start
      (combiner (term n) (accumulate combiner start (- n 1) term))))

(define (accumulate-tail combiner start n term)
  (define (helper combiner n term sofar) 
    (if (= n 0) sofar
        (helper combiner (- n 1) term (combiner sofar (term n)))))
  (helper combiner n term start))

(define-macro
 (list-of map-expr for var in lst if filter-expr)
 (list `map (list `lambda (list var) map-expr) (list `filter (list `lambda (list var) filter-expr) lst)))
