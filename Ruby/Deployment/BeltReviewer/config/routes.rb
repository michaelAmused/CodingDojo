Rails.application.routes.draw do
  root 'users#index'
  post '/users' => 'users#register'
  post '/users/login' => 'users#login'
  get '/users/:id/edit' => 'users#edit'
  patch '/users/:id/update' => 'users#update'
  get '/users/logout' => 'users#logout'
  resources :events
  patch '/events/guest_lists' => 'guest_lists#join'
  #
  # get 'events/new'
  #
  # get 'users/index'
  #
  # get 'users/new'
  # resources :users only []
  # resources :users do
  #   resources :events
  # end

  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
