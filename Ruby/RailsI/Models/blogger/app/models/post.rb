class Post < ActiveRecord::Base
    has_many :messages
    belongs_to :blog

    validates :content, presence: true
    validates :title, length: { minimum: 7 }
end
