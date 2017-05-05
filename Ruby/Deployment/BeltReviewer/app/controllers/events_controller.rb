class EventsController < ApplicationController
  def index
    @user = User.find(session[:user_id])
    User.joins(:events)
    @events = Event.all
  end

  def new
  end

  def create
    @event = Event.new(event_params)
    if @event.save
      redirect_to "/events"
    else
      flash[:errors] = @event.errors.full_messages
      redirect_to "/events"
    end
  end

  def show
    User.joins(:events)
    @event = Event.find(params[:id])
    puts '*************'
    puts @event.user.all
    puts '*************'
    # @joiners = Event.
  end

  def edit
    @event = Event.find(params[:id])
  end

  def update
    @event = Event.find(params[:id])
    if @event.update(update_params)
      redirect_to events_path
    else
      flash[:errors] = @user.errors.full_messages
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
