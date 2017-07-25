class Comment < ApplicationRecord
  belongs_to :users
  belongs_to :events

  validates :message, presence: true, length: { minimum: 5 }
end
