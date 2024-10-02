#map ve lambda
liste = [4000,3000,5400,6500,2500]
list(map(lambda deger:deger+deger *20/100,liste))
#filter
liste = [4000,3000,5400,6500,2500]
list(filter(lambda deger:deger>3000,liste))