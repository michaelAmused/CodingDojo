class Friendship < ActiveRecord::Base
    has_many :friendships, class_name: "Friendship", foreign_key: "user_id"

    belongs_to :users, class_name: "Friendship"
end
