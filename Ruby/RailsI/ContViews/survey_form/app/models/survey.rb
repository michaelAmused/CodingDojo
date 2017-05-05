class Survey < ActiveRecord::Base
    validates :name, :location, :language, presence: true
    validates :name, length: { minimum: 2 }
end
