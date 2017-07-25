class GuestListsController < ApplicationController

  def join
    @guest_list = GuestList.new(params[:user_id], params[:event_id])
    @guest.save
    redirect_to :back
  end
end