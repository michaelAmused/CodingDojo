require_relative 'human'
require_relative 'wizard'
require_relative 'ninja'
require_relative 'samurai'

h = Human.new
w = Wizard.new
n = Ninja.new
s1 = Samurai.new
s2 = Samurai.new
s3 = Samurai.new

puts h.attack(w)
puts w.health
puts w.heal.health
puts w.fireball(h)
puts h.health

puts n.steal(w).health
puts w.health
puts n.get_away.health

puts s1.how_many
puts s1.death_blow(s2).health
puts s2.health
puts s2.meditate.health
