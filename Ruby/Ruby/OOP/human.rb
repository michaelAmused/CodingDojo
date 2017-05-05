class Human
    attr_accessor :strength, :intelligence, :stealth, :health
    def initialize
        @strength = 3
        @intelligence = 3
        @stealth = 3
        @health = 100
    end
    def attack(obj)
        if obj.class.ancestors.include?(Human)
            obj.health-=10
            true
        else
            false
        end
    end
end

person1 = Human.new
person2 = Human.new
puts person1.attack(person2)
puts person1.attack("Not a Human")
puts person2.health
