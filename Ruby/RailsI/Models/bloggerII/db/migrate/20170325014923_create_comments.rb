class CreateComments < ActiveRecord::Migration
  def change
    create_table :comments do |t|
      t.string :commentable
      t.string :references

      t.timestamps null: false
    end
  end
end
