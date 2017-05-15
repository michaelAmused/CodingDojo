class EventsController < ApplicationController
  def index
    @user = User.find(session[:user_id])
    @events = Event.all
    @guests = GuestList.find_by_user_id(session[:user_id])
  end

  def new
  end

  def create
    @event = Event.new(event_params)
    if @event.save
      redirect_to '/events'
    else
      flash[:errors] = @event.errors.full_messages
      redirect_to '/events'
    end
  end

  def show
    @event = Event.find(params[:id])
    @guests = Event.find(params[:id]).guests
  end

  def edit
    @event = Event.find(params[:id])
  end

  def update
    @event = Event.find(params[:id])
    if @event.update(update_params)
      redirect_to events_path
    else
      flash[:errors] = @event.errors.full_messages
      redirect_to :back
    end
  end

  def destroy
    @event = Event.find(params[:id])
    @event.destroy
    redirect_to events_path
  end

  private
    def event_params
      params.require(:event).permit(:user_id, :name, :date, :city, :state)
    end

    def update_params
      params.require(:event).permit(:name, :date, :city, :state)
    end
end
