class GuestListsController < ApplicationController
  def create
    @guest_list = GuestList.create(user_id: "params[:user_id]", event_id: "params[:id]")
    redirect_to :back
  end

  def destroy
  end
end
