class Project
  attr_accessor :name, :description, :owner

  def initialize name, desc
    @name = name
    @description = desc
  end

  def elevator_pitch
    "#{@name}, #{@description}"
  end
end
