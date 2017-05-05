require_relative 'human'
class Samurai < Human
    @@how_many  = 0
    def initialize
        super
        @@how_many +=1
        @health = 200
    end
    def death_blow(obj)
        if obj.class.ancestors.include?(Human)
            obj.health = 0
            true
        else
            false
        end
        self
    end
    def meditate
        @health = 200
        self
    end
    def how_many
        @@how_many
    end
end
