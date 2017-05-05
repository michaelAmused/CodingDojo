a = [1,2,3,4,5,6,7,8,9,0]
b = ['a','e','i','o','u']
c = ['dog', 'cat', 'horse', 'chicken']

puts a.at(3) #=> 4

puts b.fetch(11, "cat") #=> cat
puts b.fetch(2, "dog") #=> i

puts a.delete(6)

puts a.reverse

puts b.length

puts c.sort

puts a.slice(4..7)

puts b.shuffle

puts c.join(" and a ")

puts c.insert(2, "leopard")

d = %w{cat dog bear}
puts d.values_at(1,2).join(' and ')
