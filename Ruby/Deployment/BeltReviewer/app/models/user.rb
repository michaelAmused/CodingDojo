class User < ApplicationRecord
  has_many :events, through: :guest_lists
  has_many :messages, through: :comments

  has_secure_password

  EMAIL_REGEX =/\A([^@\s]+)@((?:[-a-z0-9]+\.)+[a-z]+)\z/i
  validates :first_name, :last_name, :city, presence: true
  validates :email, presence: true, uniqueness: { case_sensitive: false }, format: { with: EMAIL_REGEX }
  validates :state, presence: true, length: { is: 2 }

  before_save :email_lowercase

  def email_lowercase
    email.downcase!
  end
end
