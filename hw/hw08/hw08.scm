(define (rle s)
  (define (helper value times rest)
    (cond ((null? rest) (cons-stream (list value times) nil))
            ((= value (car rest)) (helper value (+ times 1) (cdr-stream rest)))
            (else (cons-stream (list value times) (rle rest)))
    )
  )
  (if (null? s) nil
        (helper (car s) 1 (cdr-stream s)))
)



(define (group-by-nondecreasing s)
    (define (helper lst curr rest)
        (cond ((null? rest) (cons-stream lst nil))
                ((<= curr (car rest)) (helper (append lst (list (car rest))) (car rest) (cdr-stream rest)))
                (else (cons-stream lst (group-by-nondecreasing rest)))
        )
    )
    (helper (list (car s)) (car s) (cdr-stream s))
)


(define finite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 3
                (cons-stream 1
                    (cons-stream 2
                        (cons-stream 2
                            (cons-stream 1 nil))))))))

(define infinite-test-stream
    (cons-stream 1
        (cons-stream 2
            (cons-stream 2
                infinite-test-stream))))

