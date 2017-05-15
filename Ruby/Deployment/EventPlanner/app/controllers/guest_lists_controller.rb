class GuestListsController < ApplicationController
  def create
    @guest_list = GuestList.new(guest_params)
    if @guest_list.save
      redirect_to events_path
    else
      redirect_to events_path, notice: "Didn't Join"
    end
  end

  def destroy
  end

  private
    def guest_params
      params.require(:guest_list).permit(:user_id, :event_id)
    end
end
