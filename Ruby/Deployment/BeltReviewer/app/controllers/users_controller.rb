class UsersController < ApplicationController
  # skip_before_action :require_login, only: [:index, :register]
  # before_action :require_correct_user, only: [:edit, :update, :logout]
  def index
  end

  def login
    user = User.find_by_email(params[:email])
    if user && user.authenticate(params[:password])
      session[:user_id] = user.id
      redirect_to events_path user
    else
      flash[:errors] = ["Invalid Combination"]
      redirect_to root_path
    end
  end

  def register
    user = User.new(user_params)
    if user.save
      session[:user_id] = user.id
      redirect_to events_path user
    else
      flash[:errors] = user.errors.full_messages
      redirect_to root_path
    end
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

  def logout
    session.clear
    redirect_to '/'
  end

  private

    def require_correct_user
      if current_user != User.find(params[:id])
        redirect_to "/events/"
      end
    end

    def user_params
      params.require(:user).permit(:first_name, :last_name, :email, :city, :state, :password, :password_confirmation)
    end

    def update_params
      params.require(:user).permit(:first_name, :last_name, :email, :city, :state)
    end
end
