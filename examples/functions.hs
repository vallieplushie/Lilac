# File format has to be .hs so that nvim doesn't mess it up, should be .lilac

I number: 4
I dub: double number

# functions are like lambdas
S double: (I num) => (num * 2)

# First class citizen
S doubleWithPrint: (I num) => (
  I dub: num * 2
  print dub
  dub
  )
