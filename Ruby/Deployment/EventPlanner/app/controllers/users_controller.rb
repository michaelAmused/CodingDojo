class UsersController < ApplicationController
  def index
  end

  def register
    user = User.new(user_params)
    if user.save
      session[:user_id] = user.id
      redirect_to events_path
    else
      flash[:errors] = user.errors.full_messages
      redirect_to root_path
    end
  end

  def login
    user = User.find_by_email(params[:email])
    if user && user.authenticate(params[:password])
      session[:user_id] = user.id
      redirect_to events_path
    else
      flash[:errors] = ["Invalid Combination"]
      redirect_to root_path
    end
  end

  def logout
    session.clear
    redirect_to root_path
  end

  def edit
    @user = User.find(params[:id])
  end

  def update
    @user = User.find(params[:id])
    if @user.update(update_params)
      redirect_to events_path
    else
      flash[:errors] = @user.errors.full_messages
      redirect_to :back
    end
  end

  private
    def user_params
      params.require(:user).permit(:first_name, :last_name, :email, :city, :state, :password, :password_confirmation)
    end

    def update_params
      params.require(:user).permit(:first_name, :last_name, :email, :city, :state)
    end
end
