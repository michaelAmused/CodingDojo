class Project
    def initialize(name, description)
        @name = name
        @description = description
    end
    def elevator_pitch
        puts "#{@name}, #{@description}"
    end
    def name
        puts @name
    end

end
project1 = Project.new("Project 1", "Description 1")
puts project1.name
project1.elevator_pitch
