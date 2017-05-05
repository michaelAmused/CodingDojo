a = {first_name: "Michael", last_name: "Choi"}
b = {first_name: "John", last_name: "Doe"}
c = {first_name: "Jane", last_name: "Doe"}
d = {first_name: "James", last_name: "Smith"}
e = {first_name: "Jennifer", last_name: "Smith"}
f = {}

e.delete(:last_name)
puts e # => {:first_name => "Coding"}
puts f.empty?
puts c.empty?

puts b.has_key?("first_name")
puts c.has_value?("Jane")
