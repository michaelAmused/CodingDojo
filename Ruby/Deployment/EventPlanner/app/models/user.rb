class User < ApplicationRecord
  has_secure_password

  has_many :events

  has_many :guest_lists
  has_many :functions, through: :guest_lists, source: :event

  has_many :comments

  EMAIL_REGEX = /\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, :city, presence: true, length: { minimum: 2 }
  validates :state, presence: true, length: { is: 2 }
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }

  before_save :email_lowercase

  def email_lowercase
    email.downcase!
  end
end
