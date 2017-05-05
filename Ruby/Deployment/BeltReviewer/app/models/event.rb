class Event < ApplicationRecord
  belongs_to :user
  has_many :users, through: :guest_lists
  has_many :messages, through: :comments

  validates :name, presence: true
  validates :date, presence: true
  validates :city, presence: true
  validates :state, presence: true, length: { is: 2 }
end
