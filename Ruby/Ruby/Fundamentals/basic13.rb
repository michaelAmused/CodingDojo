# (1..255).each {|i| puts i}

# (1..255).step(2).each {|i| puts i}

# sum=0
# (1..255).each {|i| puts "New number: #{i} Sum: #{sum+=i}"}

# x = [1,3,5,7,9,13]
# x.each {|i| puts i}

# x = [-15,-4,0,1,3,5,7,9,13]
# puts x.max

# x = [2,10,3]
# sum = 0
# x.each {|i| sum+=i}
# puts sum/x.length

# x = (1..255).step(2).to_a
# puts x.to_s

# y = 3
# array = [1,3,5,7]
# puts array.count {|i| i>y}

# x = [1,5,10,-2]
# x.map! {|i| i*i}
# puts x.to_s


(1..255).each { |i| puts i }



(1..255).each { |i| puts i if i.odd? }


sum = 0
(0..255).each { |i| puts "New Number: #{i} Sum: #{sum += i}"}



[1,3,5,7,9,13].each { |elem| puts elem }


puts [-3,-5,-7].max


arr = [2,10,3]
puts arr.reduce(:+) / arr.length.to_f


y = []
(1..255).each { |i| y << i if i.odd? }



arr = [1, 3, 5, 7]
y = 3
puts arr.count { |elem| elem > y }


arr = [1, 5, 10, -2]
puts arr.map! { |elem| elem * elem }


arr = [1, 5, 10, -2]
puts arr.each_index { |index| arr[index] = 0 if arr[index] < 0 }


arr = [1, 5, 10, -2]
{ max: arr.max, min: arr.min, average: arr.reduce(:+) / arr.length.to_f }


arr = [1, 5, 10, 7, -2]
arr.rotate!(1)[arr.length-1] = 0


arr = [-1, -3, 2]
puts arr.each_index { |index| arr[index] = "Dojo" if arr[index] < 0 }
