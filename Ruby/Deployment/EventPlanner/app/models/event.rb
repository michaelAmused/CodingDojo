class Event < ApplicationRecord
  belongs_to :user

  has_many :guest_lists, dependent: :destroy
  has_many :guests, through: :guest_lists, source: :user

  has_many :comments, dependent: :destroy

  validates :name, :city, presence: true, length: { minimum: 2 }
  validates :state, presence: true, length: { is: 2 }
  validates_date :date, :after => lambda { Date.current }
end
