# Security

# The solution of CTF proplem Genfei


## **Description of solution process**

## First:
 we will not change anything in the imports or the function F() which do xor operation then it's the reverse of itself

## Second:
 We will start from the function encrypt and try to understand how it works 

 As we see we start by  unpack the 2 byte block using "<4I" format which stands for leaving the first 4 bits as it's and forming the rest in  4 byte.

 Then analysing encryption stage two
 starting of `<a>, <b>, <c>, <d>` the result of second stage as we will do the reverse of encrypt down to up.

 `a, b, c, d = c ^ F(d | F(b ^ F(a)) ^ F(d | b) ^ a), b ^ F(d ^ F(a) ^ (d | a)), a ^ F(d | F(d) ^ d), d ^ 1337`

 From first stage decryption  we will obtain `<d> -> <a> -> <b> -> <c>` obtained from secand stage of encrypt

 #### note:
 `<a>`(encrypted version) in obtaining `<c>` at te end
 but we will over write it so we store it in (temp)

 Finally,Decryption of stage two

 `temp = a`
 
 `d = d ^ 1337  # 0000 0101 0011 1001`
 
 `a = c ^ (F(d | F(d) ^ d))`
 
 `b = b ^ (F(d ^ F(a) ^ (d | a)))`
 
 `c = temp ^ (F(d | F(b ^ F(a)) ^ F(d | b) ^ a))`

## Third:

 Analysing encryption stage one
 assuming starting of `<a>, <b>, <c>, <d>` resultant of first stage

 `a, b, c, d = b ^ F(a | F(c ^ F(d)) ^ F(a | c) ^ d), c ^ F(a ^ F(d) ^ (a | d)), d ^ F(a | F(a) ^ a), a ^ 31337`

 Second stage decryption #obtain `<a> -> <d> -> <c> -> <b> `obtained from first stage
#### note:
 `<a>`(encrypted version) in obtaining `<c>` at te end
 but we will over write it so we store it in (temp)

 Finally,Decryption of stage one

 `temp = a`
 
 `a = d ^ 31337  # 0111 1010 0110 1001`
 
 `d = c ^ (F(a | F(a) ^ a))`
 
 `c = b ^ (F(a ^ F(d) ^ (a | d)))`
 
 `b = temp ^ (F(a | F(c ^ F(d)) ^ F(a | c) ^ d))`

## Fourth:
After reversing the two stages we will do it for 32 round
then we pach the result of `<a>, <b>, <c>, <d>` using the same format at unpacking

## Finally:
the flag appears and remove the extra `<#>` then submit.
