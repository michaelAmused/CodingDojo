class CreateFriendships < ActiveRecord::Migration
  def change
    create_table :friendships do |t|
      t.string :references

      t.timestamps null: false
    end
  end
end
